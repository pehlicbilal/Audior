from gtts import gTTS
import os
from src import readFiles, textToAudio
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def ren_Homepage():
    return render_template("home.html")


app.config["PATH_TO_UPLOAD"] = r"C:\Users\pehli\code\hearapp\app\uploaded_files"
app.config["PATH_TO_AUDIO"] = r"C:\Users\pehli\code\hearapp\app\audio"


@app.route("/text", methods=["POST"])
def text():
    if request.files:
        t = request.files["txt"]
        t.save(os.path.join(app.config["PATH_TO_UPLOAD"], t.filename))
        text = readFiles.openfiles(t.filename)

        audio = textToAudio.covert_to_audio(
            text, app.config["PATH_TO_AUDIO"], t.filename)

        return render_template("text.html", text=text, audio=audio)
    elif 1+1 == 2:
        return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True)


# TO DO
# 0.MAKE TEMPLATE
# 1.UPLOAD FILES
# 2.WRITE FILES
# 3.CONVERT FILES TO AUDIO
