import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(player_cards):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=player_cards
    )
    return cnx


def get_all_records():
    try:
        db_name = 'player_cards'  # update as required
        db_connection = _connect_to_db(player_cards)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % player_cards)

        query = """SELECT * FROM player_cards"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")