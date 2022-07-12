import psycopg2
import json
with open ("credentials.json") as jfile:
    pg_creds = json.load(jfile)['PG-CREDS']

def get_connection():
    conn = psycopg2.connect(pg_creds)
    return conn