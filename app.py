from flask import Flask , render_template
import os

app = Flask(__name__, static_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/disclaimer")
def dis():
    return render_template("disclaimer.html")
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)