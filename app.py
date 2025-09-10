from flask import Flask, request, render_template
from transformers import pipeline

# Initialize Flask
app = Flask(__name__)

# Load summarization model
summarizer = pipeline("summarization")

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        text = request.form["text"]
        if text.strip():
            summary_output = summarizer(text, max_length=100, min_length=30, do_sample=False)
            summary = summary_output[0]["summary_text"]
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
