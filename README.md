<img src="https://firebasestorage.googleapis.com/v0/b/neelanjan-manna.appspot.com/o/project-images%2FTranslate%20U.jpg?alt=media&token=c20235a3-6636-415e-b68f-13a00d0130a8" width="400" />
<h1 align="center">Welcome to Translate U 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://twitter.com/NeelanjanManna" target="_blank">
    <img alt="Twitter: NeelanjanManna" src="https://img.shields.io/twitter/follow/NeelanjanManna.svg?style=social" />
  </a>
</p>

> [This is the backend API of the project, the frontend mobile application can be found <a href="https://github.com/neelanjan00/Translate-U-Frontend"> here</a>] Translate U is capable of translating text given in an image from one language to another. The detection of text in the image is performed by [easyOCR](https://github.com/JaidedAI/EasyOCR) while the translation of the text is performed using the [Google Translate API](https://cloud.google.com/translate/). The application supports translation across 80+ languages, the whole list of which can be accessed [here](https://www.jaided.ai/easyocr/#:~:text=languages%20and%20expanding.-,Supported%20Languages,-Language).

### 🏠 [Homepage](https://github.com/neelanjan00/Translate-U)

## Install

```sh
pip install -r requirements.txt
```

## Usage

```sh
python app.py
```
## API Routes

<table>
	<tr>
		<th>Route</th>
      	<th>Method</th>
        <th>Field Name</th>
        <th>Input Type</th>
        <th>Returns</th>
	</tr>
    <tr>
    	<td>/</td>
        <td>POST</td>
        <td>
        	<table>
            	<tr><td>image</td></tr>
                <tr><td>sourceLanguage</td></tr>
                <tr><td>translatedLanguage</td></tr>
            </table>
        </td>
        <td>
        	<table>
            	<tr><td>Image File (png or jpg or jpeg)</td></tr>
                <tr><td>string</td></tr>
                <tr><td>string</td></tr>
            </table>
        </td>
        <td>
        	Returns a string containing the translated text.
        </td>
    </tr>
</table>

## Author

👤 **Neelanjan Manna**

* Website: https://neelanjanmanna.ml/
* Twitter: [@NeelanjanManna](https://twitter.com/NeelanjanManna)
* Github: [@neelanjan00](https://github.com/neelanjan00)
* LinkedIn: [@neelanjan00](https://linkedin.com/in/neelanjan00)

👤 **Tanisha Banik**

* Website: [tanishabanik.herokuapp.com/](tanishabanik.herokuapp.com/)
* Github: [@26tanishabanik](https://github.com/26tanishabanik)
* LinkedIn: [@tanisha-banik-04b511173](https://www.linkedin.com/in/tanisha-banik-04b511173/)

## Show your support

Give a ⭐️ if this project helped you!
