'''
MAIN API
'''
import pandas as pd
import os
import sys
print(sys.version)

from api_polypinion import articles_and_ranks
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from intr_sql import commit_cmnts, art_scres

#get pathways
path = os.getcwd() +'/data/'
art_path,rank_path = path+'articles.csv', path+'rank.csv'

app = Flask(__name__)
api = Api(app)

class GetNewsStream(Resource):
    def get(self):
        out = articles_and_ranks()
        return out

class Cmnts(Resource):
    def put(self):
        if request.form['pswd'] == 'tereces_repus':
            commit_cmnts(request.form["key_id"],request.form["cmt_id"],request.form["user"],request.form["cmnt"],request.form["date"])
        print("big success!")
        return 200

class ArtPuts(Resource):
    def put(self):
        if request.form['pswd'] == 'tereces_repus':
            art_scres(request.form["key_id"],request.form["cmt_id"],request.form["user"],request.form["cmnt"],request.form["date"])
        print("big success!")
        return 200


api.add_resource(GetNewsStream,"/get-news-stream")
api.add_resource(Cmnts,"/cmnts_postsed")
api.add_resource(ArtPuts,"/article_postsed")

if __name__ == "__main__":
    app.run(debug=True,port=8080)
