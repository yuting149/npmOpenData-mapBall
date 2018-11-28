from flask_uploads import UploadSet, IMAGES, AUDIO, configure_uploads, ALL
from flask import request, Flask, redirect, url_for, render_template, jsonify
from flask_cors import CORS
import os
# d: \anaconda3\python.exe | d: \anaconda3\lib\site-packages\wfastcgi.py

app = Flask(__name__)
CORS(app)
app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTO_ALLOW'] = AUDIO


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    print('hii')
    wav = request.files['file']
    wav.save('123123.wav')
    return 'aa'


if __name__ == '__main__':
    app.run(debug=True)
