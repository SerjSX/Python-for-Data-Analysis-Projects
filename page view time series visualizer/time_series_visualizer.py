# Please note that running it through gitpod.io is showing 4 errors. Please run it locally. I worked on this on my local computer and the tests
# passed with no errors, but on gitpod.io it's showing errors. Thank you!

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data
df = df[(df.value >= df.value.quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

# Seaborn style
sns.set_style("whitegrid")

def draw_line_plot():
    # Draw line plot
    fig,axes = plt.subplots(figsize=(24,8))

    axes.plot(df.index.values, 'value', data=df, color='r')
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    print(df_bar)
    
    # We are creating a new column for Years, and using pd.to_datetime to covnerts dates to a proper
    # date format and then we are using .year to convert the dates to show only the years.
    df_bar['Years'] = pd.to_datetime(df_bar.index.values).year
    df_bar['Months'] = pd.DatetimeIndex(df_bar.index.values).month_name()

    # we need to disable sort so the months would be ordered correctly, because it's sorting them 
    # alphabetically and we are having wrong order of the months.
    df_bar = df_bar.groupby(['Years','Months'], sort=False, as_index=False).mean()
    print(df_bar)

    # We are sorting the Months in such a way that it is correctly January, February, March...
    # I did that by pd.Categorical. Firt you insert the Series that you want to sort, in this case it's the Months from
    # the dataframe df_bar. Then we mention in categories how the order will be, in this case I am refering to the Series of months
    # from the year 2017, since that one is correctly sorted (we disabled sort before in df_bar which fixed this issue) and 
    # it contains all 12 months. So basically we will put the order we want in the categories paremeter, so based off the
    # sorting there it would sort the Months in the dataframe df_bar. 
    # ordered=True will state that we indeed want it to be sorted the exact way as the one provided in categories paremeter.
    df_bar['Months'] = pd.Categorical(df_bar.Months, categories=df_bar[df_bar.Years == 2017].Months, ordered=True)
    print(df_bar)

    # This is used to have the months be shown as separate columns. This way it would correctly create the bar plot with showing the
    # different months as separate colors
    df_bar = df_bar.groupby(['Years', 'Months'])['value'].aggregate('first').unstack()
    print(df_bar)
    

    # Draw bar plot
    fig, axes = plt.subplots(figsize=(24,12))
    df_bar.plot.bar(rot=0, ax=axes)
    axes.set_ylabel('Average Page Views', fontsize=24)
    axes.set_xlabel('Years', fontsize=24)



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    print(df_box)

    # We are using this to correctly sort the Months
    # We are using the values of the months from year 2017 since all of the months are correctly sorted there, then using .unique()
    # to just get the values with no repeats.
    df_box['month'] = pd.Categorical(df_box.month, categories=df_box[df_box.year == 2017].month.unique(), ordered=True)

    print(df_box)


    # Draw box plots (using Seaborn)
    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(24,8))
    # We set hue as the same as the x-axis in order to have separate colors for the boxes, it looks nicer. In order for this to work we have to set legend
    # to False as well, then we can define a palette color.
    sns.boxplot(data=df_box, x=df_box['year'], y=df_box['value'], ax=ax1, hue=df_box['year'],legend=False, palette='Set2')
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(data=df_box, x=df_box['month'], y=df_box['value'], ax=ax2, hue=df_box['month'], legend=False, palette='Set2')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


      
