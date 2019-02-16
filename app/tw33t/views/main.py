from flask import g, Markup
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app
from functools import wraps
from flask import jsonify
from twitter import *
import json, requests, datetime, sys, os, uuid, re, time
from flask.globals import current_app
from werkzeug import responder

@app.route("/", methods=['GET'])
def index():

    return render_template('index.html')


'''

Introduce a "Get tweets" route for the client and log relevant info from each search into a file.

'''

def get_tweet_data(screen_name, count=3):
    data = []
    consumer_key = current_app.config['CONSUMER_KEY']
    consumer_secret = current_app.config['CONSUMER_SECRET']
    access_token = current_app.config['ACCESS_TOKEN']
    access_token_secret = current_app.config['ACCESS_TOKEN_SECRET']
    
    twitter = Twitter(auth=OAuth(access_token,
                                 access_token_secret,
                                 consumer_key,
                                 consumer_secret))
    data = twitter.statuses.user_timeline(screen_name=screen_name, 
                                          count=count)
    
    return data

def api_404(msg):
    resp = jsonify({'status': 'error',
                 'message': msg})
    resp.status_code = 404
    return resp
    
def log_search(screen_name, is_error):
    with open(current_app.config['LOG_PATH'], "a") as fd:
        fd.write("{name}|{error}\n".format(name=screen_name,
                                           error=is_error))
@app.route("/api/v1/get_tweets")
def api_tweets():
    screen_name = request.args.get('screen_name', '')
    if screen_name == '':
        return api_404("screen_name is required!")
    error = False
    try:
        tweets = get_tweet_data(screen_name)
        return jsonify({'status': 'success',
                    'data': tweets})
    except TwitterHTTPError as err:
        print('error:', err)
        error = True
        return api_404(str(err))
    finally:
        log_search(screen_name, error)
        