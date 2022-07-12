#!/bin/python3
import psycopg2
import api_connect
import database_connect
#this file updates all the channels in our DB
connection = database_connect.get_connection()

def get_channels(connection):
    cur = connection.cursor()
    cur.execute("SELECT ucid FROM channel")
    li = cur.fetchall()
    cur.close()
    lit = [item[0] for item in li]
    return lit


def get_channel_data(id):
    statistics = api_connect.get_channel_stats(id)
    return statistics
def run_channel_update(id :str, connection, statistics):
    cur = connection.cursor()
    cur.execute("INSERT INTO channel_ts (date, channel, viewcount, subscribercount, videocount) VALUES (NOW(), %s, %s, %s, %s)", (id, statistics['viewCount'], statistics['subscriberCount'],statistics['videoCount']))
    connection.commit()
    cur.close()

channellist = get_channels(connection)
for id in channellist:
    statistics = get_channel_data(id)
    run_channel_update(id, connection, statistics)

connection.close()