'''
MAIN API
'''
import pandas as pd
import json
from intr_sql import top_10
from datetime import datetime

def articles_and_ranks():
    '''
    This takes 2 long-format tables, and merges them.

    This also finds two articles under the same rank. If there are two, it indents them in the json.

    :param article database path:
    :param rank database path:
    :return python dictionary:
    '''
    #load from paths
    #df_articles = pd.read_csv(art_path)
    #df_rank = pd.read_csv(rank_path)

    # data operation
    #df = df_rank.merge(df_articles,how='left',on='key_id')

    df,lst_ = top_10()


    out= df.to_dict(orient='records')

    json_out = {}
    # If one Rank has multiple articles, make them to a list
    for row in out:
        rank,article = row['main_rank'],row['article']

        # Add the value to the dictionary entry
        if rank not in json_out:
            json_out[rank] = []
        json_out[rank].append(row['article'])

    tup_art_lst = list(json_out.items())

    json_out = {}
    # If one Rank has multiple articles, make them to a list
    for row in out:
        rank, article = row['main_rank'], row['gist1']

        # Add the value to the dictionary entry
        if rank not in json_out:
            json_out[rank] = []
        json_out[rank].append(row['gist1'])

    tup_gist1_lst = list(json_out.items())

    json_out = {}
    # If one Rank has multiple articles, make them to a list
    for row in out:
        rank, article = row['main_rank'], row['gist1']

        # Add the value to the dictionary entry
        if rank not in json_out:
            json_out[rank] = []
        json_out[rank].append(row['gist2'])

    tup_gist2_lst = list(json_out.items())

    json_out = {}
    # If one Rank has multiple articles, make them to a list
    for row in out:
        rank, article = row['main_rank'], row['gist1']

        # Add the value to the dictionary entry
        if rank not in json_out:
            json_out[rank] = []
        json_out[rank].append(row['gist3'])

    tup_gist3_lst = list(json_out.items())

    json_out = {}
    # If one Rank has multiple articles, make them to a list
    for row in out:
        rank, article = row['main_rank'], row['date']

        # Add the value to the dictionary entry
        if rank not in json_out:
            json_out[rank] = []
        json_out[rank].append(row['date'].to_pydatetime().strftime('%Y-%m-%d %H:%M:%S'))

    tup_dte_lst = list(json_out.items())


    json_data = {"articles":[]}
    for row in out:
        art = [y for x, y in tup_art_lst if x == row['main_rank']]
        gist1_ = [y for x, y in tup_gist1_lst if x == row['main_rank']]
        gist2_ = [y for x, y in tup_gist2_lst if x == row['main_rank']]
        gist3_ = [y for x, y in tup_gist3_lst if x == row['main_rank']]
        dte = [y for x, y in tup_dte_lst if x == row['main_rank']]
        json_fnl = {
            'rank': row['main_rank'],
            'key_id': row['key_id'],
            'title': row['headline'],
            'gist1': gist1_[0],
            'gist2': gist2_[0],
            'gist3': gist3_[0],
            'category': row['cat'],
            'created_at': row['date'].to_pydatetime().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': dte[0],
            'body': art[0],
            'img': row['img']
        }
        json_data["articles"].append(json_fnl)

    return json_data


