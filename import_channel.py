#interactive program for adding a channel to the database.
import psycopg2
import api_connect
import database_connect

def update_channel(id :str, connection, statistics):
    cur = connection.cursor()
    cur.execute("INSERT INTO channel_ts (date, channel, viewcount, subscribercount, videocount) VALUES (NOW(), %s, %s, %s, %s)", (id, statistics['viewCount'], statistics['subscriberCount'],statistics['videoCount']))
    connection.commit()
    cur.close()

    connection.close()

def import_channel(id : str, connection, data : tuple):
    cur = connection.cursor()
    snippet, statistics = data
    cur.execute("INSERT INTO channel (name,ucid) VALUES (%s, %s)", (snippet['title'], id))
    connection.commit()
    cur.close()
    update_channel(id, connection, statistics)


if __name__ == "__main__":
    connection = database_connect.get_connection()
    id = input("Channel ID To be imported to the database")
    data = api_connect.get_new_channel_info(id)
    print(data)
    import_channel(id, connection, data)