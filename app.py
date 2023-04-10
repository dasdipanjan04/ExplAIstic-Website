from flask import Flask, render_template, request
import os
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def load():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Get the file from the request
        file = request.files['image']

        # Save the file to the upload folder
        UPLOAD_FOLDER = os.path.join(Path.cwd(), "uploaded")
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        success = 'Image uploaded successfully!'
        return render_template('index.html', success=success)
    else:
        return '''
            <form method="post" enctype="multipart/form-data">
              <input type="file" name="image">
              <br>
              <input type="submit" value="Upload">
            </form>
        '''


@app.route('/success')
def success():
    return 'File uploaded successfully!'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
