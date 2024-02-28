from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=["Get", "Post"])
def index():
    if request.method == "Post":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes = notes)

if __name__ == '__main__':
    app.run(debug=True)