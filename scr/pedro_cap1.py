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
#merging emotions dataset with acoustic cues dataset

emo_cue = pd.merge(emotions, emotions_meta, on = 'Nro')

#clean up column names. All lower case.
emo_cue.rename(columns={'Soundlevel':'dynamics'}, inplace = True)
emo_cue.rename(str.lower, axis='columns', inplace=True)

#Metadata from top 100/week billboard chards from 1999-2019. Spotift API Library.
#Used for comparison
hello = atributes_song.loc[atributes_song['Name'] == 'Hello']
hello_adele = hello.loc[hello['Artist'] == 'Adele']
#print(hello_adele)
heyjude = top20.loc[top20['Name'] == 'Hey Jude']
# print(heyjude)

#plotting relationships - illustrate the relationships between emotion and cues. # refer to plotting in scr folder

# Happy, Sad, Mode

# Happy, Sad, Mode

emo_cue_msort = emo_cue.sort_values(['mode', 'happy', 'sad'], ascending = [True, False, False])
emo_cue_msort['mode'].iloc[93], emo_cue_msort['mode'].iloc[94]


hm = emo_cue['happy'].mean()
t = np.linspace(0,200,200)
h = emo_cue_msort['happy']
s = (emo_cue_msort['sad'])*-1
sm=s.mean()

fig, ax1 = plt.subplots(figsize = (24,10), dpi=300)

ax1.bar(t, h, color='r', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Happy')
ax1.bar(t, s, color='b', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Sad')
# ax1.plot(m, c = 'black',alpha=0.8, linewidth =4, label = "Mode")

ax1.set_title('Musical Mode', fontdict = {'fontsize': 38,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)

ax1.set_ylabel('Emotion Reading', fontsize= 33, weight = 'light')
ax1.set_xlabel('Songs',fontsize=30, weight = 'light')

ax1.tick_params(axis='both', which='major', labelsize=30)
plt.xticks(t, [""]*len(t))

ax1.axhline(sm, c='darkblue', label = '"Sad" Mean')
ax1.axhline(hm, c='maroon', label = '"Happy" Mean')

ax1.axvline(94, ymin=0, ymax=1, c='black')

ax1.text(100, 4,'--> Musical Mode = 2', fontsize=19)
ax1.text(55, 4,'Musical Mode = 1 <--', fontsize=19)


ax1.legend(fontsize=19, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol = 6, loc = 0)

# plt.show()

#illustrative plotting -> remaining cues

emo_cue_1sort = emo_cue.sort_values(['register', 'happy', 'sad'], ascending = [True, False, False])
emo_cue_2sort = emo_cue.sort_values(['tempo', 'happy', 'sad'], ascending = [True, False, False])
emo_cue_3sort = emo_cue.sort_values(['dynamics', 'happy', 'sad'], ascending = [True, False, False])
emo_cue_4sort = emo_cue.sort_values(['articulation', 'happy', 'sad'], ascending = [True, False, False])
emo_cue_5sort = emo_cue.sort_values(['timbre', 'happy', 'sad'], ascending = [True, False, False])
emo_cue_6sort = emo_cue.sort_values(['melody', 'happy', 'sad'], ascending = [True, False, False])


#parameters ax1
t = np.linspace(0,200,200)
h = emo_cue_1sort['happy']
s = (emo_cue_1sort['sad'])*-1
sm = s.mean()
hm = h.mean()
m = emo_cue_1sort['register']

#parameters ax2
t2 = np.linspace(0,200,200)
h2 = emo_cue_2sort['happy']
s2 = (emo_cue_2sort['sad'])*-1
sm2=s2.mean()
hm2 = h2.mean()
m2 = emo_cue_2sort['tempo']

#parameters ax3
t3 = np.linspace(0,200,200)
h3 = emo_cue_3sort['happy']
s3 = (emo_cue_3sort['sad'])*-1
sm3=s3.mean()
hm3 = h3.mean()
m3 = emo_cue_3sort['dynamics']

#parameters ax4
t4 = np.linspace(0,200,200)
h4 = emo_cue_4sort['happy']
s4 = (emo_cue_4sort['sad'])*-1
sm4=s4.mean()
hm4 = h4.mean()

m4 = emo_cue_4sort['articulation']

#parameters ax5
t5 = np.linspace(0,200,200)
h5 = emo_cue_5sort['happy']
s5 = (emo_cue_5sort['sad'])*-1
sm5=s5.mean()
hm5 = h5.mean()

m5 = emo_cue_5sort['timbre']

#parameters ax6
t6 = np.linspace(0,200,200)
h6 = emo_cue_6sort['happy']
s6 = (emo_cue_6sort['sad'])*-1
sm6=s6.mean()
hm6 = h6.mean()
m6 = emo_cue_6sort['melody']

fig, ((ax1, ax2), (ax3,ax4),(ax5,ax6)) = plt.subplots(3,2,figsize = (45,55), sharey=True, sharex = True)

# ax1 register
ax1.bar(t, h, color='r', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Happy')
ax1.bar(t, s, color='b', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Sad')

ax1.set_title('Register (Key)', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax1.set_ylabel('Emotion Reading', fontsize= 50, weight = 'light')
ax1.tick_params(axis='both', which='major', labelsize=40)
ax1.legend(fontsize=40, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol = 6, loc = 0)

ax1.axhline(sm, c='darkblue', label = '"Sad" Mean')
ax1.axhline(hm, c='maroon', label = '"Happy" Mean')

#ax2 tempo
ax2.bar(t, h2, color='r', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Happy')
ax2.bar(t, s2, color='b', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Sad')

ax2.set_title('Tempo (bpm)', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax2.set_ylabel('Emotion Reading', fontsize= 50, weight = 'light')
ax2.tick_params(axis='both', which='major', labelsize=40)
ax2.legend(fontsize=40, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol = 6, loc = 0)

ax2.axhline(sm, c='darkblue', label = '"Sad" Mean')
ax2.axhline(hm, c='maroon', label = '"Happy" Mean')

#ax3 dynamics
ax3.bar(t, h, color='r', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Happy')
ax3.bar(t, s, color='b', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Sad')

ax3.set_title('Dynamics', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax3.set_ylabel('Emotion Reading', fontsize= 50, weight = 'light')
ax3.tick_params(axis='both', which='major', labelsize=40)
ax3.legend(fontsize=40, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol = 6, loc = 0)

ax3.axhline(sm, c='darkblue', label = '"Sad" Mean')
ax3.axhline(hm, c='maroon', label = '"Happy" Mean')

#ax4 articulation
ax4.bar(t, h, color='r', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Happy')
ax4.bar(t, s, color='b', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Sad')

ax4.set_title('Articulation', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax4.set_ylabel('Emotion Reading', fontsize= 50, weight = 'light')
ax4.tick_params(axis='both', which='major', labelsize=40)
ax4.legend(fontsize=40, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol = 6, loc = 0)

ax4.axhline(sm, c='darkblue', label = '"Sad" Mean')
ax4.axhline(hm, c='maroon', label = '"Happy" Mean')

#ax5 timbre
ax5.bar(t, h, color='r', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Happy')
ax5.bar(t, s, color='b', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Sad')

ax5.set_title('Timbre', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax5.set_ylabel('Emotion Reading', fontsize= 50, weight = 'light')
ax5.tick_params(axis='both', which='major', labelsize=40)
ax5.legend(fontsize=40, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol = 6, loc = 0)

ax5.axhline(sm, c='darkblue', label = '"Sad" Mean')
ax5.axhline(hm, c='maroon', label = '"Happy" Mean')

#ax6 melody
ax6.bar(t, h, color='r', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Happy')
ax6.bar(t, s, color='b', edgecolor = 'black', width = 1, alpha= 0.4, label = 'Sad')

ax6.set_title('Melody', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax6.set_ylabel('Emotion Reading', fontsize= 50, weight = 'light')
ax6.tick_params(axis='both', which='major', labelsize=40)
ax6.legend(fontsize=40, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol = 6, loc = 0)

ax6.axhline(sm, c='darkblue', label = '"Sad" Mean')
ax6.axhline(hm, c='maroon', label = '"Happy" Mean')
plt.tight_layout()
# plt.show()

#example

gravity = atributes_song.loc[atributes_song['Name'] == 'Gravity']
gravity_jm = gravity.loc[gravity['Artist']=='John Mayer']
# print(gravity_jm)

mysherona = top20.loc[top20['Name']=='My Sharona']
# print(mysherona)

#clean top20 column names

top20.rename(str.lower, axis='columns', inplace=True)
top201=top20[[
    'name','artist','decade','rank','key','tempo','duration_ms','danceability','energy',
    'loudness','speechiness','acousticness','instrumentalness','valence','time_signature']]

#duration from miliseconds to minutes
top201['duration_ms'] = top201['duration_ms'].map(lambda x: x/60000).round(2)
top201.rename(columns={'duration_ms':'duration_m'}, inplace = True)


top20_70 = top201.loc[top20['decade'] == 70]
top20_80 = top201.loc[top20['decade'] == 80]
top20_90 = top201.loc[top20['decade'] == 90]
top20_00 = top201.loc[top20['decade'] == 2000]
top20_60=top201.loc[top20['decade'] == 60]

x = ["60's","70's","80's","90's","00's"]
f = dict(marker='o', markerfacecolor='green', markersize=15,
                  linestyle='none', markeredgecolor='black')
m = dict(marker='D', markeredgecolor = 'black', markerfacecolor='black', markersize=15) 

keys = [top20_60['key'],top20_70['key'],top20_80['key'],top20_90['key'],top20_00['key']]
tempo = [top20_60['tempo'],top20_70['tempo'],top20_80['tempo'],top20_90['tempo'],top20_00['tempo']]
duration_m = [top20_60['duration_m'],top20_70['duration_m'],top20_80['duration_m'],top20_90['duration_m'],top20_00['duration_m']]
danceability = [top20_60['danceability'],top20_70['danceability'],top20_80['danceability'],top20_90['danceability'],top20_00['danceability']]
energy = [top20_60['energy'],top20_70['energy'],top20_80['energy'],top20_90['energy'],top20_00['energy']]
loudness = [top20_60['loudness'],top20_70['loudness'],top20_80['loudness'],top20_90['loudness'],top20_00['loudness']]
speechiness = [top20_60['speechiness'],top20_70['speechiness'],top20_80['speechiness'],top20_90['speechiness'],top20_00['speechiness']]
acousticness = [top20_60['acousticness'],top20_70['acousticness'],top20_80['acousticness'],top20_90['acousticness'],top20_00['acousticness']]
instrumentalness = [top20_60['instrumentalness'],top20_70['instrumentalness'],top20_80['instrumentalness'],top20_90['instrumentalness'],top20_00['instrumentalness']]
valence = [top20_60['valence'],top20_70['valence'],top20_80['valence'],top20_90['valence'],top20_00['valence']]
time_sig = [top20_60['time_signature'],top20_70['time_signature'],top20_80['time_signature'],top20_90['time_signature'],top20_00['time_signature']]


# fig, ax1 = plt.subplots(figsize=(10,6))
fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8),(ax9,ax10),(ax11,ax12)) = plt.subplots(6,2,figsize=(45,100))
fig.delaxes(ax12)


#keys
ax1.boxplot(keys, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'},
            flierprops = f, 
            showmeans = True,meanprops = m
           )

ax1.set_title('Key Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax1.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax1.set_xlabel('Keys', fontsize= 50, linespacing = 10)
ax1.tick_params(axis='y', which='major', labelsize=40)

ax1.set_yticklabels(["60's","70's","80's","90's","00's"])

# plt.show()

#'tempo',
ax2.boxplot(tempo, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f,
            showmeans = True,meanprops = m
           )

ax2.set_title('Tempo Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax2.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax2.set_xlabel('Tempo (bpm)', fontsize= 50, linespacing = 10)
ax2.tick_params(axis='both', which='major', labelsize=40)
ax2.set_yticklabels(["60's","70's","80's","90's","00's"])

#  'duration_m',
ax3.boxplot(duration_m, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f,
            showmeans = True,meanprops = m
           )

ax3.set_title('Duration Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax3.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax3.set_xlabel('Duration (min)', fontsize= 50, linespacing = 10)
ax3.tick_params(axis='both', which='major', labelsize=40)
ax3.set_yticklabels(["60's","70's","80's","90's","00's"])

#  'danceability',

ax4.boxplot(danceability, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f,
            showmeans = True,meanprops = m
           )

ax4.set_title('Danceability Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax4.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax4.set_xlabel('Danceability', fontsize= 50, linespacing = 10)
ax4.tick_params(axis='both', which='major', labelsize=40)
ax4.set_yticklabels(["60's","70's","80's","90's","00's"])

#  'energy',

ax5.boxplot(energy, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f,
            showmeans = True,meanprops = m
           )

ax5.set_title('Energy Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax5.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax5.set_xlabel('Energy', fontsize= 50, linespacing = 10)
ax5.tick_params(axis='both', which='major', labelsize=40)
ax5.set_yticklabels(["60's","70's","80's","90's","00's"])

#  'loudness',
ax6.boxplot(loudness, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f,
            showmeans = True,meanprops = m
           )

ax6.set_title('Loudness Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax6.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax6.set_xlabel('Loudness', fontsize= 50, linespacing = 10)
ax6.tick_params(axis='both', which='major', labelsize=40)
ax6.set_yticklabels(["60's","70's","80's","90's","00's"])

#  'speechiness',
ax7.boxplot(speechiness, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f,
            showmeans = True,meanprops = m
           )

ax7.set_title('Speechiness Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax7.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax7.set_xlabel('Speechiness', fontsize= 50, linespacing = 10)
ax7.tick_params(axis='both', which='major', labelsize=40)
ax7.set_yticklabels(["60's","70's","80's","90's","00's"])

#  'acousticness',

ax8.boxplot(acousticness, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f,
            showmeans = True,meanprops = m
           )

ax8.set_title('Acousticness Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax8.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax8.set_xlabel('Acousticness', fontsize= 50, linespacing = 10)
ax8.tick_params(axis='both', which='major', labelsize=40)
ax8.set_yticklabels(["60's","70's","80's","90's","00's"])

#  'instrumentalness',

ax9.boxplot(instrumentalness, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f,
            showmeans = True,meanprops = m
           )

ax9.set_title('Instrumentalness Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax9.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax9.set_xlabel('Instrumentalness', fontsize= 50, linespacing = 10)
ax9.tick_params(axis='both', which='major', labelsize=40)

ax9.set_yticklabels(["60's","70's","80's","90's","00's"])

#  'valence',

ax10.boxplot(valence, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f, 
            showmeans = True,meanprops = m
           )

ax10.set_title('Valence Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax10.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax10.set_xlabel('Valence', fontsize= 50, linespacing = 10)
ax10.tick_params(axis='both', which='major', labelsize=40)

ax10.set_yticklabels(["60's","70's","80's","90's","00's"], fontsize=40)


#  'time_signature'

ax11.boxplot(time_sig, vert = False, patch_artist=True, 
            boxprops={'linewidth': 3,'facecolor':'g','color':'black','alpha':0.2},
            medianprops={'color':'black'}, flierprops = f,
            showmeans = True,meanprops = m
           )

ax11.set_title('Time Signature Distribution per Decade', fontdict = {'fontsize': 60,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax11.set_ylabel('Decades', fontsize= 50, linespacing = 10)
ax11.set_xlabel('Time Signature', fontsize= 50, linespacing = 10)
ax11.tick_params(axis='both', which='major', labelsize=40)

ax11.set_yticklabels(["60's","70's","80's","90's","00's"])

plt.tight_layout()
# plt.show()

sx_mean=top20_60.mean().round(2)
sv_mean=top20_70.mean().round(2)
e_mean=top20_80.mean().round(2)
n_mean=top20_90.mean().round(2)
t_mean=top20_00.mean().round(2)


fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8),(ax9,ax10),(ax11,ax12)) = plt.subplots(6,2,figsize=(22,28))
fig.delaxes(ax12)


# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
ykey = [sx_mean[2],sv_mean[2],e_mean[2],n_mean[2],t_mean[2]]


# fig, ax = plt.subplots(figsize=(9,5))

ax1.bar(x, ykey, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax1.set_title('Mean Key Value', fontdict = {'fontsize': 25,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax1.set_ylabel('Mean Key Value', fontsize= 17, linespacing = 10)
ax1.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax1.tick_params(axis='x', rotation = 45)
ax1.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(ykey):
    ax1.text(i, 
              v/ykey[i]+0.7, 
              ykey[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()

# ax2
# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
ytempo = [sx_mean[3],sv_mean[3],e_mean[3],n_mean[3],t_mean[3]]


# fig, ax = plt.subplots(figsize=(9,4))

ax2.bar(x, ytempo, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax2.set_title('Mean Tempo Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax2.set_ylabel('Tempo (bpm)', fontsize= 17, linespacing = 10)
ax2.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax2.tick_params(axis='x', rotation = 45)
ax2.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(ytempo):
    ax2.text(i, 
              v/ytempo[i]+60, 
              ytempo[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()

#ax3

# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
yduration = [sx_mean[4],sv_mean[4],e_mean[4],n_mean[4],t_mean[4]]


# fig, ax = plt.subplots(figsize=(9,5))

ax3.bar(x, yduration, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax3.set_title('Mean Duration Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax3.set_ylabel('Mean Duration (min)', fontsize= 17, linespacing = 10)
ax3.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax3.tick_params(axis='x', rotation = 45)
ax3.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(yduration):
    ax3.text(i, 
              v/yduration[i], 
              yduration[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()

#ax4
# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
ydanceability = [sx_mean[5],sv_mean[5],e_mean[5],n_mean[5],t_mean[5]]


# fig, ax = plt.subplots(figsize=(9,5))

ax4.bar(x, ydanceability, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax4.set_title('Mean Danceability Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax4.set_ylabel('Mean Danceability', fontsize= 17, linespacing = 10)
ax4.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax4.tick_params(axis='x', rotation = 45)
ax4.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(ydanceability):
    ax4.text(i, 
              v/ydanceability[i]-0.8, 
              ydanceability[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()

#ax5

# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
yenergy = [sx_mean[6],sv_mean[6],e_mean[6],n_mean[6],t_mean[6]]


# fig, ax = plt.subplots(figsize=(9,5))

ax5.bar(x, yenergy, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax5.set_title('Mean Energy Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax5.set_ylabel('Mean Energy', fontsize= 17, linespacing = 10)
ax5.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax5.tick_params(axis='x', rotation = 45)
ax5.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(yenergy):
    ax5.text(i, 
              v/yenergy[i]-0.8, 
              yenergy[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()

#ax6

# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
yloudness = [sx_mean[7],sv_mean[7],e_mean[7],n_mean[7],t_mean[7]]


# fig, ax = plt.subplots(figsize=(9,5))

ax6.bar(x, yloudness, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax6.set_title('Mean Loudness Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax6.set_ylabel('Mean Loudness (dB)', fontsize= 17, linespacing = 10)
ax6.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax6.tick_params(axis='x', rotation = 45)
ax6.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(yloudness):
    ax6.text(i, 
              v/yloudness[i]-6, 
              yloudness[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()

#ax7

# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
yspeechiness = [sx_mean[8],sv_mean[8],e_mean[8],n_mean[8],t_mean[8]]


# fig, ax = plt.subplots(figsize=(9,5))

ax7.bar(x, yspeechiness, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax7.set_title('Mean Speechiness Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax7.set_ylabel('Mean Speechiness', fontsize= 17, linespacing = 10)
ax7.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax7.tick_params(axis='x', rotation = 45)
ax7.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(yspeechiness):
    ax7.text(i, 
              v/yspeechiness[i]-0.99, 
              yspeechiness[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()

#ax8


# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
yacousticness = [sx_mean[9],sv_mean[9],e_mean[9],n_mean[9],t_mean[9]]


# fig, ax = plt.subplots(figsize=(9,5))

ax8.bar(x, yacousticness, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax8.set_title('Mean Acousticness Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax8.set_ylabel('Mean Acousticness', fontsize= 17, linespacing = 10)
ax8.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax8.tick_params(axis='x', rotation = 45)
ax8.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(yacousticness):
    ax8.text(i, 
              v/yacousticness[i]-0.94, 
              yacousticness[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()

#ax9

# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
yinstrumentalness = [sx_mean[10],sv_mean[10],e_mean[10],n_mean[10],t_mean[10]]


# fig, ax = plt.subplots(figsize=(9,5))

ax9.bar(x, yinstrumentalness, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax9.set_title('Mean Instrumentalness Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax9.set_ylabel('Mean Instrumentalness', fontsize= 17, linespacing = 10)
ax9.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax9.tick_params(axis='x', rotation = 45)
ax9.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(yinstrumentalness):
    ax9.text(i, 
              v/yinstrumentalness[i]-0.94, 
              yinstrumentalness[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()

#ax10

# ._get_numeric_data()
#plot metadata comparison per decade


x = ["60's","70's","80's","90's","00's"]
yvalence = [sx_mean[11],sv_mean[11],e_mean[11],n_mean[11],t_mean[11]]


# fig, ax = plt.subplots(figsize=(9,5))

ax10.bar(x, yvalence, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax10.set_title('Mean Valence Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax10.set_ylabel('Mean Valence', fontsize= 17, linespacing = 10)
ax10.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax10.tick_params(axis='x', rotation = 45)
ax10.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(yvalence):
    ax10.text(i, 
              v/yvalence[i]-0.85, 
              yvalence[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()

#ax11


x = ["60's","70's","80's","90's","00's"]
ytimesig = [sx_mean[12],sv_mean[12],e_mean[12],n_mean[12],t_mean[12]]


# fig, ax = plt.subplots(figsize=(9,5))

ax11.bar(x, ytimesig, color=['forestgreen','maroon','goldenrod','cyan','fuchsia'], edgecolor = 'black', width = 1, alpha= 0.4)

ax11.set_title('Mean Time Signature Value', fontdict = {'fontsize': 21,
 'fontweight' : 'heavy',
 'verticalalignment': 'baseline'}, family = 'serif', linespacing = 5)
ax11.set_ylabel('Mean Time Signature (measures)', fontsize= 17, linespacing = 10)
ax11.set_xlabel('Decade', fontsize= 17, linespacing = 10)

ax11.tick_params(axis='x', rotation = 45)
ax11.tick_params(axis='both', which='major', labelsize=18)

for i, v in enumerate(ytimesig):
    ax11.text(i, 
              v/ytimesig[i]-0.3, 
              ytimesig[i], 
              fontsize=17, 
              color='black', horizontalalignment='center', alpha=0.8)
    
# ax.legend(fontsize=17, shadow = True, facecolor = 'w', labelspacing = 0.8, ncol=6, loc=0)

plt.tight_layout()
# plt.show()



print(top20_80)
