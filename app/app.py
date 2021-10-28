from gtts import gTTS
import os
from src import readFiles, textToAudio
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def ren_Homepage():
    return render_template("home.html")


app.config["PATH_TO_UPLOAD"] = r"..\app\uploaded_files"
app.config["PATH_TO_AUDIO"] = r"..\app\audio"


def extensions(filename):
    name = filename.split(".")
    return name[0]


@app.route("/text", methods=["POST","GET"])
def text():
    if request.files:
        t = request.files["txt"]
        t.save(os.path.join(app.config["PATH_TO_UPLOAD"], extensions(t.filename)))
        text = readFiles.openfiles(extensions(t.filename))

        audio = textToAudio.covert_to_audio(
            text, app.config["PATH_TO_AUDIO"], extensions(t.filename))

        return render_template("text.html", text=text)
    else:
        return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True)
