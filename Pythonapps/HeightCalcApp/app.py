from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("heightForm.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email"]
        height = request.form["height"]
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True, port=4500)