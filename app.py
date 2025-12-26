from flask import Flask, render_template
from pathlib import Path

BASE = Path(__file__).resolve().parent
app = Flask(
    __name__,
    template_folder=str(BASE / "src" / "templates"),
    static_folder=str(BASE / "src" / "static"),
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/examples")
def examples():
    return render_template("examples.html")

if __name__ == "__main__":
    app.run(debug=True)  # 기본 포트 5000
