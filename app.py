from recommendation.Movie_Similarity import Recommendation
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from tensor import Inference

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
        return str(name.similar_movie(str(request.form.get("movie"))))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)