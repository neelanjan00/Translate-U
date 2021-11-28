# import the dependency libraries
from flask import Flask, request, redirect
import cv2
import numpy as np
import os
from google.cloud import translate_v2 as translate
import six
import easyocr

# replace the empty string with the relative file path of your gcp service account key 
gcp_service_key_path = ""

# set the GCP service key JSON file path in the ENV
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = gcp_service_key_path

# allowed file extensions for uploaded image file
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# initialize the client for google translate api 
translate_client = translate.Client()

# map the language names to their corresponding ISO-639-1 identifiers
map_lang = {"Afrikaans" : "af", "Arabic" : "ar",\
                        "Azerbaijani" : "az", "Belarusian" : "be", "Bulgarian" : "bg",\
                        "Bengali" : "bn", "Bosnian" : "bs", "Simplified Chinese" : "ch_sim", "Traditional Chinese" : "ch_tra",\
                        "Czech" : "cs", "Welsh" : "cy", "Danish" : "da", "German" : "de", "English" : "en", "Spanish" : "es",\
                        "Estonian" : "et", "Persian (Farsi)" : "fa", "French" : "fr", "Irish" : "ga", "Hindi": "hi",\
                        "Croatian" : "hr", "Hungarian" : "hu", "Indonesian" : "id", "Icelandic" : "is", "Italian" : "it",\
                        "Japanese" : "ja", "Kannada" : "kn", "Korean" : "ko", "Kurdish" : "ku",\
                        "Lithuanian" : "lt", "Latvian" : "lv","Maori" : "mi","Mongolian" : "mn",\
                        "Marathi" : "mr", "Malay" : "ms", "Maltese" : "mt", "Nepali" : "ne", "Dutch" : "nl", "Norwegian" : "no",\
                        "Polish" : "pl", "Portuguese" : "pt", "Romanian" : "ro", "Russian" : "ru",\
                        "Slovenian" : "sl", "Albanian" : "sq", "Swedish" : "sv",\
                        "Swahili" : "sw", "Tamil" : "ta", "Telugu" : "te", "Thai" : "th", "Tajik" : "tjk", "Tagalog" : "tl",\
                        "Turkish" : "tr", "Uyghur" : "ug", "Ukranian" : "uk", "Urdu" : "ur", "Uzbek" : "uz", "Vietnamese" : "vi"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'

# check if the image file type is valid
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload():
    if request.method == 'POST':

        # return error if image file is missing
        if 'image' not in request.files:
            print("No file part")
            return redirect(request.url)

        file = request.files['image']

        # return error if filename is missing
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):

            # extract source and target language fields
            source_language = request.form['sourceLanguage']
            target_language = request.form['targetLanguage']
            
            # download detection and recognition model for the source language
            reader = easyocr.Reader([map_lang[source_language]])

            # extract image np array from multipart file
            multipart_image = request.files['image']
            image_array = np.fromfile(multipart_image, np.uint8)
            image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            numpy_image = np.asarray(image)

            # extract the words from the image 
            output = reader.readtext(numpy_image, detail = 0)

            # form a sentence out of the extracted words
            sentence = ' '.join(output)

            # check if sentence needs to be decoded in the utf-8 format
            if isinstance(sentence, six.binary_type):
                sentence = sentence.decode("utf-8")

            # map the target language identifier
            target_identifier = None

            if target_language == "Simplified Chinese":
                target_identifier = "zh-CN"
            elif target_language == "Traditional Chinese":
                target_identifier = "zh-TW"
            else:
                target_identifier = map_lang[target_language]

            # translate the sentence into the target language
            translation_result = translate_client.translate(sentence, target_language=target_identifier)

        return translation_result["translatedText"]
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
