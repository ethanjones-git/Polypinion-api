'''
MAIN API
'''
import pandas as pd
import os
from api_polypinion import articles_and_ranks
from flask import Flask, request, jsonify


#get pathways
path = os.getcwd() +'/data/'
art_path,rank_path = path+'articles.csv', path+'rank.csv'

app = Flask(__name__)

@app.route("/get-news-stream",methods = ["GET"])
def home():
    out = jsonify(articles_and_ranks(art_path,rank_path))
    return out, 200



if __name__ == "__main__":
    app.run(debug=True,port=8000)