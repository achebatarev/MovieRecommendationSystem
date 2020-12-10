
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from tensor import Inference


class Recommendation:
    def __init__(self):
        self.df = pd.read_csv('recommendation/data/movie_dataset.csv')
        features = self.df.loc[:, ['genres', 'keywords', 'cast', 'director']]
        self.df['features'] = self.df.genres + ' ' + self.df.keywords + \
            ' ' + self.df.cast + ' ' + self.df.director
        text = self.df.features.fillna('')
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(text)
        self.similarity_score = cosine_similarity(count_matrix)

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
    
    if request.method == 'POST':
        similar_movie("",str(request.form.get("movie")))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)



    def index_to_title(self, index):
        return ''.join(self.df.loc[index, ['title']].tolist())




    def similar_movie(self, movie):
        movie_id = self.df.title[self.df.title == movie].index.tolist()
        if not movie_id:
            return 'Movie not found'
        movie_id = movie_id[0]
        similar_movies = enumerate(self.similarity_score[movie_id])
        output = []
        sorted_similar_movies = sorted(
            similar_movies, key=lambda x: x[1], reverse=True)[1:]
        for i, movie in enumerate(sorted_similar_movies):
            output.append(self.index_to_title(movie[0]))
            if i > 50:
                break
        return output


