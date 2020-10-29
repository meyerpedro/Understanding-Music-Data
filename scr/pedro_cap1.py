import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
plt.style.use('ggplot')
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import numpy as np # linear algebra
import os # accessing directory structure

#data
emotions = pd.read_csv('data/dataverse_files/mean_emotion_ratings.csv')
emotions_meta = pd.read_csv('data/dataverse_files/design_matrix.csv')
atributes_song = pd.read_csv('data/BillboardFromLast20/songAttributes_1999-2019.csv')
artist = pd.read_csv('data/BillboardFromLast20/artistDf.csv')
top20 = pd.read_csv('data/Top20AllDecades.csv')

#Metadata from top 100/week billboard chards from 1999-2019. Spotift API Library.
#Used for comparison

#Metadata from top 100/week billboard chards from 1999-2019. Spotift API Library.
#Used for comparison
print(atributes_song.loc[atributes_song['Name'] == 'Gravity'])


#merging emotions dataset with acoustic cues dataset

emo_cue = pd.merge(emotions, emotions_meta, on = 'Nro')
# emo_cue.head(50)

#clean up column names. All lower case.
emo_cue.rename(columns={'Soundlevel':'dynamics'}, inplace = True)
emo_cue.rename(str.lower, axis='columns', inplace=True)
# emo_cue.max()

