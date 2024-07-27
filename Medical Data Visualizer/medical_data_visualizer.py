import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
# Reading the CSV file and importing it as a dataframe
df = pd.read_csv('medical_examination.csv')

# 2
# Creating a new column named BMI to calculate the BMI by dividing the people's weight in kilograms by the square of their height in meters
df['BMI'] = df['weight'] / (df['height'] / 100)**2

# If the BMI's value is > 25 then the person is overweight, we assign the value 1 to the new column we created named "overweight".
# If it's not greater than 25, then we assign the value 0 to the new column stating that the person is not overweight.
df['overweight'] = df['BMI'].apply(lambda x: 1 if x > 25 else 0)

# We don't need this column anymore after setting the overweight column, so we delete it
del df['BMI']

# 3
#We are normalizing the data by making 0 always good and 1 always bad.
# If the value of cholesterol or gluc is 1, we assign the value 0. If the value is more than 1, we assign the value 1.
good = 0
bad = 1

# lambda x: is used to apply the condition. If it's equal to 1, then apply 0. If not then 1.
# We are updating the values of the columns cholesterol and gluc.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4
# We are going to draw a cat plot.
def draw_cat_plot():
    # 5

    # First, we will only use the values of the columns cholesterol, gluc, smoke, alco, active, and overweight.
    # So we filter the dataframe to only include those values, and apply it in the variable df_cardios.
    # We are using .melt to do this.

    # We specify df as the data.
    # id_vars states by which column should we apply the id as. We are going to do this based off the values in the column
    # cardio, so this automatically inserts the cardio column as a separate column.

    # the value_vars will be stored as a separate column named "variable", and the "value" column will store each value of the
    # items in the "variable" column.
    # It is only limited to the columns we specified above. So if we have
    # cardio | gluc | smoke
    # 1      | 1    | 1
    # 0      | 0    | 1

    # This will do:
    # cardio | variable | value
    # 1      | gluc     | 1
    # 1      | smoke    | 1
    # 0      | gluc     | 0
    # 0      | gluc     | 1
    
    df_cat = pd.melt(df, id_vars='cardio', value_vars=["cardio", "cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # 6 skipped because it can be done by catplot immiedtaly without grouping


    # 7
    # We are converting the df_cat to a Dataframe, and sorting the values by variable so it would be shown alphabetically.
    df_cat = pd.DataFrame(df_cat).sort_values('variable')

    # This is where the plot is created.
    # data: points to the data frame
    # kind: what the plot should be of type, in this case we are going to count. Here are the options:
        #Categorical scatterplots:
        #stripplot() (with kind="strip"; the default)
        #swarmplot() (with kind="swarm")
    
        #Categorical distribution plots:
        #boxplot() (with kind="box")
        #violinplot() (with kind="violin")
        #boxenplot() (with kind="boxen")

        #Categorical estimate plots:
        #pointplot() (with kind="point")
        #barplot() (with kind="bar")
        #countplot() (with kind="count") <=

    # x: what to display on the x-axis, in this case the variable values which are cholesterol, gluc, smoke...
    # hue: what to separate the bars as, in this case we have the column "value" which holds either 0 or 1. We use that.
    # col: what to use as a separator column. This is used to create different charts based off the values under the column cardio, in this case 0 or 1.

    fig = sns.catplot(data=df_cat,kind='count',x='variable',hue='value',col='cardio').set_ylabels('total').fig

   
    # 9 saving as png file
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    # First we are cleaning the data before presenting it as a heatmap chart. The following are the conditions for incorrect data:
        #diastolic pressure is higher than systolic 
        #height is less than the 2.5th percentile 
        #height is more than the 97.5th percentile
        #weight is less than the 2.5th percentile
        #weight is more than the 97.5th percentile

    
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    # We are creating the correlation matrix of the dataset using the
    # function .corr() with the default method pearson
    corr = df_heat.corr()

    # 13
    # We are creating a mask of the upper triangle of the corr dataframe
    # We will be replicating the dimensions of the df by using .ones_like 
    # so the default values won't be used and we will use np.triu to create the
    # upper triangle.
    mask = np.triu(np.ones_like(corr))
    


    # 14
    # we are preparing the figure and the axis with an appropriate size that's easily viewable.
    # Now if we draw the heatmap it will be added on this plot
    fig, ax = plt.subplots(figsize=(14,10))

    # 15
    # Here we are creating the actual heatmap with some configurations.
    # First, corr is the provided dataset that includes the correlated dataframe
    # Second, we are specifying the mask which would show how we want the heatmap to look like. Data will not be shown in cells where mask is True (1).
    # Cells with missing values are automatically masked.
    #Third, we are specifying annot=True so we would see the values in each cell in the heatmap.
    # Fourth, we are specifying a format to be used. Which only shows 1 digit after the decimal point.
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')



    # 16
    # export it as a png file.
    fig.savefig('heatmap.png')
    return fig

