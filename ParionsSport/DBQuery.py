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

    def insert_joueur_nba(self, infoJoueur):
        req = "INSERT INTO joueur_nba(idJoueur, nom) VALUES(%s, %s)"
        params = (infoJoueur['PLAYER_ID'], infoJoueur['PLAYER'])
        self._change_query(req, params)
        return

    def insert_match_nba(self, infoMatch, infoResultat):
        req = "INSERT INTO match_nba(idMatch, idEquipeDom, idEquipeExt, saison, date, resultatFinal)" \
              "VALUES(%s, %s, %s, %s, %s, %s)"
        result = 0 if infoResultat[0]['PTS'] > infoResultat[1]['PTS'] else 1
        params = (infoMatch['GAME_ID'], infoMatch['HOME_TEAM_ID'], infoMatch['VISITOR_TEAM_ID'], infoMatch['SEASON'],
                  infoMatch['GAME_DATE_EST'], result)
        self._change_query(req, params)
        return





