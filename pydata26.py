# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:35:42 2016

@author: FANG
"""
import pandas as pd
unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('C:/Users/FANG/Anaconda3/ch02/movielens/users.dat', sep='::', engine='python', header=None,names=unames)
rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('C:/Users/FANG/Anaconda3/ch02/movielens/ratings.dat',sep='::', header=None, engine='python',names=rnames)
mnames=['movie_id','title','genres']
movies=pd.read_table('C:/Users/FANG/Anaconda3/ch02/movielens/movies.dat',sep='::',header=None, names=mnames, engine='python')
data=pd.merge(pd.merge(ratings,users),movies)
mean_ratings = data.pivot_table('rating', index='title', columns='gender',aggfunc='mean')
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >=250]
mean_ratings=mean_ratings.ix[active_titles]
top_female_ratings=mean_ratings.sort_values(by='F',ascending=False)
mean_ratings['diff']=mean_ratings['M']-mean_ratings['F']
sorted_by_diff=mean_ratings.sort_values(by='diff')
rating_std_by_title=data.groupby('title')['rating'].std()
rating_std_by_title= rating_std_by_title.ix[active_titles]