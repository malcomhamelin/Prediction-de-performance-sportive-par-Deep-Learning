from DBQueries.DBQuery import DBQuery
import tensorflow as tf
import keras as k
from keras.layers import Input, Dense
import numpy as np


db = DBQuery() # Base contenant les données d'apprentissage

matchesStats = db.select_matchs_join_stats_match() # Récupération des données d'apprentissage
datasetLearning = [] # Données d'apprentissage
datasetResult = [] # Resultats pour connaitre la précision

# Mise en forme des données d'apprentissage
for match in matchesStats:
    vector = (match['fgm'], match['fga'], match['fg_pct'], match['fg3m'],
              match['fg3a'], match['fg3_pct'], match['ftm'], match['fta'],
              match['ft_pct'], match['oreb'], match['dreb'], match['reb'],
              match['ast'], match['stl'], match['blk'], match['turnover'],
              match['pf'], match['pts'], match['plus_minus'], match['min'])
    vectorRes = match['resultatFinal']
    datasetLearning.append(vector)
    datasetResult.append(vectorRes)

# Conversion en tableaux numpy pour être interprétés correctement par l'algorithme de TensorFlow/Keras
datasetLearning = np.array(datasetLearning)
datasetResult = np.array(datasetResult)

# Création du modèle
input = Input(shape=(20, ), name="input")
pcouche = Dense(16, activation=tf.nn.relu)(input)
dcouche = Dense(16, activation=tf.nn.relu)(pcouche)
output = Dense(2, activation=tf.nn.softmax)(dcouche)
model = k.Model(inputs=[input], outputs=output)

#checkpoint = k.ModelCheckpoint("model_checkpoint", verbose=1, monitor='val_acc', save_best_only=True, mode='auto')

model.compile(optimizer='adam',
              loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])

# Apprentissage par le modèle
model.fit(datasetLearning, datasetResult, epochs=3)
model.save('test_match_nba')
