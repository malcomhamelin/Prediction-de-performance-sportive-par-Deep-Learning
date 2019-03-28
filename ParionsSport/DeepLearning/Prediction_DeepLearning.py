from DBQueries.DBQueryTest import DBQueryTest
import keras as k
import numpy as np

dbTest = DBQueryTest() # Base contenant les données de test

matchesStatsTest = dbTest.select_matchs_join_stats_match() # Récupération des données de test

# Données de test à passer dans le modèle de prédiction
datasetTest = []

# Données triviales pour permettre d'intérpreter les résultats (nom de l'équipe, date du matchs)
datasetInterpretation = []

# Mise en forme des données de test
for match in matchesStatsTest:
    vector = (match['fgm'], match['fga'], match['fg_pct'], match['fg3m'],
              match['fg3a'], match['fg3_pct'], match['ftm'], match['fta'],
              match['ft_pct'], match['oreb'], match['dreb'], match['reb'],
              match['ast'], match['stl'], match['blk'], match['turnover'],
              match['pf'], match['pts'], match['plus_minus'], match['min'])
    datasetTest.append(vector)

    vectorInfos = (match['idMatch'], match['Nom'], match['date'],
                   match['resultatFinal'])
    datasetInterpretation.append(vectorInfos)

# Conversion en tableaux numpy pour être interprétés correctement par l'algorithme de TensorFlow/Keras
datasetTest = np.array(datasetTest)
datasetInterpretation = np.array(datasetInterpretation)

# Recupération du modèle sauvegardé, créé par la classe apprentissage
new_model = k.models.load_model('test_match_nba')
predictions = new_model.predict(datasetTest)

# Affichage des résultats
if len(predictions) == len(datasetInterpretation):
    for i in range(0, len(predictions)):
        print("Equipe : ", datasetInterpretation[i][1], " Prediction : ", np.argmax(predictions[i]),
              " Resultat réel : ", datasetInterpretation[i][3])
