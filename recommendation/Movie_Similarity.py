#!/usr/bin/env python
# coding: utf-8

# In[138]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[139]:
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

# In[140]:


# In[169]:


    def index_to_title(self, index):
        return ''.join(self.df.loc[index, ['title']].tolist())


# In[172]:


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


# In[ ]:
