#!/usr/bin/env python
# coding: utf-8

# In[138]:


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[139]:


df = pd.read_csv('data/movie_dataset.csv')
df.head()


# In[140]:


features = df.loc[:, ['genres', 'keywords', 'cast', 'director']]
df['features'] = df.genres + ' ' + df.keywords + \
    ' ' + df.cast + ' ' + df.director
df.columns
text = df.features.fillna('')
cv = CountVectorizer()
count_matrix = cv.fit_transform(text)
similarity_score = cosine_similarity(count_matrix)


# In[169]:


def index_to_title(index):
    return ''.join(df.loc[index, ['title']].tolist())


# In[172]:


def similar_movie(movie):
    movie_id = df.title[df.title == movie].index.tolist()
    if not movie_id:
        return 'Movie not found'
    movie_id = movie_id[0]
    similar_movies = enumerate(similarity_score[movie_id])
    output = []
    sorted_similar_movies = sorted(
        similar_movies, key=lambda x: x[1], reverse=True)[1:]
    for i, movie in enumerate(sorted_similar_movies):
        output.append(index_to_title(movie[0]))
        if i > 50:
            break
    return output


# In[ ]:
