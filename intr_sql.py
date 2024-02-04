import mysql.connector
from datetime import date
import pandas as pd

def top_10():
    db = mysql.connector.connect(
        host='20.163.58.138',
        user='dvp',
        port='3306',
        password='Zzb33k23432@#$#@',
        database='test')

    query= """
    SELECT * FROM test.rankingsv5
    LEFT JOIN test.articlesv5
    ON rankingsv5.key_id = articlesv5.key_id
    ORDER BY rankingsv5.main_rank
    LIMIT 10;
    """

    df = pd.read_sql_query(query, db)

    query = """
        SELECT key_id FROM test.rankingsv5
        ORDER BY rankingsv5.main_rank;
        """

    uuid_lst = pd.read_sql_query(query, db)

    db.close()

    return df,uuid_lst['key_id'].tolist()

def commit_cmnts(key_id, cmt_id, user, cmnt, date):
    db = mysql.connector.connect(
        host='20.163.58.138',
        user='dvp',
        port='3306',
        password='Zzb33k23432@#$#@',
        database='test')

    c = db.cursor()
    params = (key_id, cmt_id, user, cmnt, date)
    insert_query = "INSERT INTO cmnts (key_id, cmt_id, user, cmnt, date) VALUES (%s, %s, %s, %s, %s);"

    c.execute(insert_query, params)
    db.commit()
    c.close()
    db.close()

def art_scres(key_id, scre, date):
    db = mysql.connector.connect(
        host='20.163.58.138',
        user='dvp',
        port='3306',
        password='Zzb33k23432@#$#@',
        database='test')

    c = db.cursor()
    insert_query = "INSERT INTO cmnts (key_id, cmt_id, user, cmnt, date) VALUES (%s, %s, %s, %s, %s);"

    """
    add later
    
    
    """

    c.execute(insert_query)
    db.commit()
    c.close()
    db.close()



commit_cmnts('test','test', 'test', 'test', '01/01/01/ 11:11:11')
