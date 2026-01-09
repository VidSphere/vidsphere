from flask import Flask, request, send_file, render_template
import yt_dlp
import os

app = Flask(__name__, template_folder="../frontend")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]

    ydl_opts = {
        "outtmpl": "video.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        filename = ydl.prepare_filename(info)

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    
