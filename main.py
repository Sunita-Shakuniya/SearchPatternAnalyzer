# Importing Modules
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random
# Working with data set 
df_row=pd.read_csv("history.csv")

categories = np.unique(df_row['title'])
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]

# Draw Plot for Each Category
plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')

for i, title in enumerate(categories):
    plt.scatter('visitCount', 'date', 
                data=df_row.loc[df_row.title==title, :], 
                s=20, c=colors[i], label=str(title))

# Decorations
plt.gca().set(xlim=(1, 40),
              xlabel='visitCount', ylabel='date')

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Scatterplot of Searches on different days ", fontsize=22)
plt.legend(fontsize=12, borderpad=2)    
plt.show()    

# Bar Chart To Visualize the data Count
df = df_row.groupby('title').size().reset_index(name='counts')
n = df['title'].unique().__len__()+1
all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)

# Plot Bars
plt.figure(figsize=(16,10), dpi= 80)
plt.bar(df['title'], df['counts'], color=c, width=.5)
for i, val in enumerate(df['counts'].values):
    plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':12})

# Decoration
plt.gca().set_xticklabels(df['title'], rotation=60, horizontalalignment= 'right')
plt.title("Visisted Searches", fontsize=22)
plt.ylabel('# Visited Count')
plt.ylim(1, 200)
plt.show()

#Hence Successfully Implemented

