import praw
import pandas as pd
import datetime
import os.path as path
import os

reddit = praw.Reddit(client_id='Qrc1CBEtZ7qXttnF7A43vw', client_secret='AZsBWeSY6hFDihOEM_3-NZMauxQFew', user_agent='DCS Capstone WebScrapping')
posts = []
post_path = path.abspath(path.join(__file__ ,os.getcwd() + '/data/'))
#r/fintech community scrape
fintech_subreddit = reddit.subreddit('fintech')
for post in fintech_subreddit.hot(limit=None):
    date = datetime.datetime.fromtimestamp(post.created)
    submission = reddit.submission(post.id)
    submission.comments.replace_more(limit=None)
    comments = []
    for comment in submission.comments.list():
       comments.append(comment.body)
    
    if len(comments) > 0:
        post_info = [post.title, date, post.selftext, comments]
          
    else:
        post_info = [post.title, date, post.selftext]
    
    post_details = pd.DataFrame(post_info)
    post_details.to_csv(os.getcwd() + '/data/' + post.id, index=False)  
    posts.append([post.title, date])     

#r/technology community scrape 
technology_subreddit = reddit.subreddit('technology')
for post in technology_subreddit.search('fintech', time_filter='all', limit=None):
    date = datetime.datetime.fromtimestamp(post.created)
    
    submission = reddit.submission(post.id)
    submission.comments.replace_more(limit=None)
    comments = []
    for comment in submission.comments.list():
        comments.append(comment.body)
    
    if len(comments) > 0:
        post_info = [post.title, date, post.selftext, comments]
             
    else:
        post_info = [post.title, date, post.selftext]

    post_details = pd.DataFrame(post_info)
    post_details.to_csv(os.getcwd() + '/data/' + post.id, index=False)  
    posts.append([post.title, date]) 

posts = pd.DataFrame(posts,columns=['title', 'date_posted'])
posts.to_excel(os.getcwd() + '/DataSet.xlsx')

