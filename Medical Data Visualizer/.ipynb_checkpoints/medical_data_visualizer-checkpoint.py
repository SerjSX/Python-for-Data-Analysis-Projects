import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')
print(df)

# 2
df['BMI'] = df['weight'] / (df['height'] / 100)**2
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)
print(df)

# 3
good = 0
bad = 1

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
print(df)

# 4
def draw_cat_plot():
    # 5
    df_cardios = df[["cardio", "cholesterol", "gluc", "smoke", "alco", "active", "overweight"]]
    df_cat = pd.melt(df_cardios, id_vars=['cardio'], var_name='variable', value_name='value')
    print(df_cat)


    # 6
    df_cat.rename({"variable": "variable", "value": "cardio"}, inplace = True)
    df_cat = df_cat.rename(columns={"variable": "variable", "value": "cardio"})
    df_cat = df_cat.groupby(by='cardio')
    print(df_cat)



    # 7
    df_cat = pd.DataFrame(df_cat.value_counts().unstack())
    print(df_cat)
    print(df_cat.iloc[0])
    print(df_cat.loc[0])
    fig = sns.catplot(data=df_cat)



    # 8
    fig = fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
