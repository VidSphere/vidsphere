from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route("/")
def home():
    return "Vidsphere backend is running!"

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")

    ydl_opts = {
        "outtmpl": "downloaded_video.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
        filename = ydl.prepare_filename(info)

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
