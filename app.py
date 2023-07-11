from flask import Flask , render_template
import os

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/test_image')
def test_image():
    return app.send_static_file('Gradient.png')

    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)