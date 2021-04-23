from flask import Flask, render_template
import model
import load_model
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html')

@app.route("/about")
def about():
    return load_model.code()

if __name__ == '__main__':
    app.run(debug=True)