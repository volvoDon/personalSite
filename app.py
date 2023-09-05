from flask import Flask, render_template, request, redirect, url_for, flash
import os , helpers
app = Flask(__name__, static_folder='static')
app.secret_key = os.getenv("FKEY")
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpeg', 'jpg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/test_image')
def test_image():
    return app.send_static_file('Gradient.png')

@app.route('/resume')
def resume_serve():
    return app.send_static_file('resume.pdf')

@app.route('/waveforecast')
def wave_serve():
    return app.send_static_file('WaveForcasting.pdf')

@app.route('/image-class', methods=['GET', 'POST'])
def upload_file():
    image_class = None  # Initialize the variable outside the if condition
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
        else:
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
            elif file and allowed_file(file.filename):
                file_extension = os.path.splitext(file.filename)[1]
                filename = os.path.join(app.config['UPLOAD_FOLDER'], f'image{file_extension}')
                file.save(filename)
                flash('Image successfully uploaded!')
                image_class = helpers.query(filename)
            else:
                flash('Allowed image type is -> jpg or jpeg')

    return render_template('upload.html', image_class=image_class)

 

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)