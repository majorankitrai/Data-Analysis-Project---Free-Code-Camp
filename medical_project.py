import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv('C:\\Users\\admin\\Desktop\\Data Description\\medical_examination.csv')
#print(df.head())

#df.info()

#Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.

BMI = (df['weight']/(df['height']**2))
df['overweight'] = (BMI>25).astype(int)
    
#print(df.head(2))

#Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.

df['cholesterol'] = np.where(df['cholesterol'] == 1,0,1)
#print(df.head(2))

df['gluc'] = (df['gluc'] >1).astype(int)
#print(df.head(2))

#Draw the Categorical Plot in the draw_cat_plot function.
import seaborn as sns

def draw_cat_plot():
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['active','alco','cholestrol','gluc','overweight','smoke'])
    figure = sns.catplot(x="Variable",kind = 'count',hue = 'value',data=df_cat,col='cardio')
    figure.set_axis_labels('variable','total')
    fig = figure
    fig.savefig('catplot.png')
    return fig

#Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
# Melt the original dataframe
df_cat = pd.melt(df,
                 id_vars=['cardio'],
                 value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

# Group and count the occurrences
df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()

# Rename the 'size' column to 'total' for clarity (required for catplot)
df_cat = df_cat.rename(columns={'size': 'total'})

#Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # Clean the data
    df_heat = df[
         (df['ap_lo'] <= df['ap_hi']) & 
         (df['height'] >= df['height'].quantile(0.025)) & 
         (df['height'] <= df['height'].quantile(0.975)) &
         (df['weight'] >= df['weight'].quantile(0.025)) & 
         (df['weight'] <= df['weight'].quantile(0.975))]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype= bool))


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (12,12))

    # Draw the heatmap with 'sns.heatmap()'
    
    sns.heatmap(corr, vmin=0, vmax= 0.25, fmt='.1f', linewidth = 1, annot = True, square = True, mask=mask, cbar_kws = {'shrink':.82})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

draw_heat_map()
draw_cat_plot()


