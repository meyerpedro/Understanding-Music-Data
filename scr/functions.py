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
emotions = pd.read_csv('../data/dataverse_files/mean_emotion_ratings.csv')
emotions_meta = pd.read_csv('../data/dataverse_files/design_matrix.csv')
atributes_song = pd.read_csv('../data/BillboardFromLast20/songAttributes_1999-2019.csv')
artist = pd.read_csv('../data/BillboardFromLast20/artistDf.csv')
top20 = pd.read_csv('../data/Top20AllDecades.csv')

# cleaned data
#emotions and cues

def lower_col(df):

    return df.rename(str.lower, axis='columns')

emo_cue = pd.merge(emotions, emotions_meta, on = 'Nro')
emo_cue.rename(columns={'Soundlevel':'dynamics'}, inplace = True)


emo_cue_clean = lower_col(emo_cue)    
top20_clean = lower_col(top20)


#duration from miliseconds to minutes
top20_clean['duration_ms'] = top20_clean['duration_ms'].map(lambda x: x/60000).round(2)
top20_clean.rename(columns={'duration_ms':'duration_m'}, inplace = True)


def top20_by_decade(decade):


    x = top20_clean.loc[top20_clean['decade'] == decade]

    return x


top20_70 = top20_by_decade(70)
top20_80 = top20_by_decade(80)
top20_90 = top20_by_decade(90)
top20_00 = top20_by_decade(2000)
top20_60 = top20_by_decade(60)

print(top20_80)
