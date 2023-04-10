from flask import Flask, render_template, request, redirect, url_for
import os
from pathlib import Path

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('example.html')

@app.route('/ImageUpload')
def image_upload():
    return 'This is where you will upload your image!!!!'


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Get the file from the request
        file = request.files['image']

        # Save the file to the upload folder
        UPLOAD_FOLDER = os.path.join(Path.cwd(), "uploaded")
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        # Redirect to a success page
        return redirect(url_for('success'))
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
