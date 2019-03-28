import mysql.connector
import sys

# Class permettant d'accéder à la base de données contenant les données de test
class DBQueryTest:
    _db = 0

    def __init__(self):
        if (DBQueryTest._db == 0):
            print
            "Initialisation de la connexion a la BDD"
            DBQueryTest._db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="stats_nba_test")

    def _select_query(self, query_txt, params=()):
        cursor = self._db.cursor(dictionary=True, buffered=True)
        try:
            cursor.execute(query_txt, params)
            results = cursor.fetchall()
            return results
        except Exception as e:
            sys.stderr.write("query error : " + str(e) + " " + query_txt + "\n")
            return None

    def select_matchs_join_stats_match(self):
        req = "SELECT * FROM `match_nba` INNER JOIN `stats_equipe_match_nba` using(idMatch) INNER JOIN " \
              "`equipe_nba` using(idEquipe)"
        params = ()
        res = self._select_query(req, params)
        return res
