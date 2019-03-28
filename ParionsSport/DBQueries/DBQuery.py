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
        params = (infoMatch[0]['GAME_ID'], infoMatch[0]['HOME_TEAM_ID'], infoMatch[0]['VISITOR_TEAM_ID'], infoMatch[0]['SEASON'],
                  infoMatch[0]['GAME_DATE_EST'], result)
        self._change_query(req, params)
        return

    def insert_stats_equipe_match_nba(self, infoMatch):
        req = "INSERT INTO stats_equipe_match_nba(idEquipe, idMatch, fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, " \
              "ft_pct, oreb, dreb, reb, ast, stl, blk, turnover, pf, pts, plus_minus, min) VALUES(%s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        m, s = infoMatch["MIN"].split(":")
        params = (infoMatch['TEAM_ID'], infoMatch['GAME_ID'], infoMatch['FGM'], infoMatch['FGA'], infoMatch['FG_PCT'],
                  infoMatch['FG3M'], infoMatch['FG3A'], infoMatch['FG3_PCT'], infoMatch['FTM'], infoMatch['FTA'],
                  infoMatch['FT_PCT'], infoMatch['OREB'], infoMatch['DREB'], infoMatch['REB'], infoMatch['AST'],
                  infoMatch['STL'], infoMatch['BLK'], infoMatch['TO'], infoMatch['PF'], infoMatch['PTS'],
                  infoMatch['PLUS_MINUS'], int(m))
        self._change_query(req, params)
        return

    def insert_quart_temps_nba(self, numQT, infoTraditionnal, infoAdvanced):
        req = "INSERT INTO quart_temps_nba(numQT, idMatch, idEquipe, idJoueur, positionDepart, tempsDeJeu, fgm, fga, fg_pct, " \
              "fg3m, ftm, fta, ft_pct, oreb, dreb, ast, stl, blk, turnover, pf, pts, plus_minus, " \
              "e_off_rating, off_rating, e_def_rating, def_rating, e_net_rating, net_rating) VALUES(%s, %s, %s, %s, %s, %s, " \
              "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        m, s = infoTraditionnal["MIN"].split(":")
        params = (numQT, infoTraditionnal['GAME_ID'], infoTraditionnal['TEAM_ID'], infoTraditionnal['PLAYER_ID'],
                  infoTraditionnal['START_POSITION'], int(m), infoTraditionnal['FGM'], infoTraditionnal['FGA'],
                  infoTraditionnal['FG_PCT'], infoTraditionnal['FG3M'],
                  infoTraditionnal['FTM'], infoTraditionnal['FTA'], infoTraditionnal['FT_PCT'],
                  infoTraditionnal['OREB'], infoTraditionnal['DREB'], infoTraditionnal['AST'],
                  infoTraditionnal['STL'], infoTraditionnal['BLK'], infoTraditionnal['TO'], infoTraditionnal['PF'],
                  infoTraditionnal['PTS'], infoTraditionnal['PLUS_MINUS'], infoAdvanced['E_OFF_RATING'],
                  infoAdvanced['OFF_RATING'], infoAdvanced['E_DEF_RATING'], infoAdvanced['DEF_RATING'],
                  infoAdvanced['E_NET_RATING'], infoAdvanced['NET_RATING'])
        self._change_query(req, params)
        return

    def select_match(self, game):
        req = "SELECT * FROM `match_nba` WHERE idMatch = %s"
        params = (game, )
        res = self._select_query(req, params)
        return res

    def select_stats_match(self, game):
        req = "SELECT * FROM `quart_temps_nba` WHERE idMatch = %s"
        params = (game, )
        res = self._select_query(req, params)
        return res

    def select_matchs_join_stats_match(self):
        req = "SELECT * FROM `match_nba` INNER JOIN `stats_equipe_match_nba` using(idMatch)"
        params = ()
        res = self._select_query(req, params)
        return res
