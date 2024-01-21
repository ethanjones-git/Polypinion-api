'''
MAIN API
'''
import pandas as pd

def articles_and_ranks(art_path,rank_path):
    #load from paths
    df_articles = pd.read_csv(art_path)
    df_rank = pd.read_csv(rank_path)

    # data operation
    df = df_rank.merge(df_articles,how='left',on='key_id')
    out= df.to_dict(orient='records')
    json_out = {}

    # If one Rank has multiple articles, make them to a list
    for row in out:
        rank,article = row['RANK'],row['ARTICLE']

        # Add the value to the dictionary entry
        if rank not in json_out:
            json_out[rank] = []
        json_out[rank].append(row['ARTICLE'])
    tup_art_lst = list(json_out.items())

    # Same with dates
    json_out = {}

    for row in out:
        rank,article = row['RANK'],row['DATE']

        # Add the value to the dictionary entry
        if rank not in json_out:
            json_out[rank] = []
        json_out[rank].append(row['DATE'])
    tup_dte_lst = list(json_out.items())


    # Create the out
    '''
    
    df__=df.drop_duplicates(subset = 'RANK', keep='first')
    out= df__.to_dict(orient='records')
    new_list = []
    for row in out:
        art = [y for x,y in tup_art_lst if x==row['RANK']]
        dte = [y for x, y in tup_dte_lst if x == row['RANK']]
        json_fnl = {
            'RANK':row['RANK'],
            'KEY' : row['key_id'],
            'HEADLINE': row['TITLE'],
            'GIST': row['GIST'],
            'date': row['DATE'],
            'article': art[0]
        }
        new_list.append(json_fnl)
    '''

    json_data = {"data":[]}
    for row in out:
        art = [y for x, y in tup_art_lst if x == row['RANK']]
        dte = [y for x, y in tup_dte_lst if x == row['RANK']]
        json_fnl = {
            'RANK': row['RANK'],
            'KEY': row['key_id'],
            'HEADLINE': row['TITLE'],
            'GIST': row['GIST'],
            'date': row['DATE'],
            'article': art[0]
        }
        json_data["data"].append(json_fnl)

    return json_data


