from recommendation.Movie_Similarity import Recommendation
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
data = {}
data["content"] = ""


@app.route('/', methods=['GET', 'POST'])
def index():
    if data:
        return render_template('index.html', data=data)
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_text():

    name = Recommendation()

    if request.method == 'POST':
        return jsonify(name.similar_movie(str(request.data.decode("UTF-8"))))


if __name__ == "__main__":
    app.run()
