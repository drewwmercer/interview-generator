from questions import printQuestion
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    questions = printQuestion()
    return render_template("index.html", questions_list=questions)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
