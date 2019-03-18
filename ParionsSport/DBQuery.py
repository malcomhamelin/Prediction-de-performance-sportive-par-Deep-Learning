import mysql.connector
from datetime import datetime
import sys


class DBQuery:
    _db = 0

    def __init__(self):
        if (DBQuery._db == 0):
            print
            "Initialisation de la connexion a la BDD"
            DBQuery._db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="stats_nba")

    def _select_query(self, query_txt, params=()):
        cursor = self._db.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(query_txt, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            sys.stderr.write("query error : " + str(e) + " " + query_txt + "\n")
            return None

    def _change_query(self, query_txt, params):
        cursor = self._db.cursor()
        try:
            cursor.execute(query_txt, params)
            self._db.commit()
            return True
        except Exception as e:
            sys.stderr.write("Change query error : " + str(e) + " " + query_txt + "\n")
            return False

    def insert_equipe_nba(self, infoEquipe):
        req = "INSERT INTO equipe_nba(idEquipe, nom) VALUES(%s, %s)"
        params = (infoEquipe['TEAM_ID'], infoEquipe['TEAM_NAME'])
        self._change_query(req, params)
        return
