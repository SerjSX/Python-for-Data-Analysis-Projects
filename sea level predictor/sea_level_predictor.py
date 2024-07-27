import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df_data = pd.read_csv('epa-sea-level.csv')
    print(df_data)


    # Create scatter plot
    plt.scatter(df_data['Year'], df_data['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    first_line = linregress(df_data['Year'], df_data['CSIRO Adjusted Sea Level'])
    print(first_line)
    # We use arange to fill numbers from the lowest Year in the dataset up to 2050 (we type 2051 since it would not be included)
    # the 1 states to increase by 1.
    till_2050 = np.arange(df_data["Year"].min(),2051,1)
    print(till_2050)
    plt.plot(till_2050, first_line.intercept + first_line.slope*till_2050, color='r')
    


    # Create second line of best fit
    data_2000 = df_data[df_data.Year >= 2000]
    till_2050_from_2000 = np.arange(data_2000["Year"].min(),2051,1)
    second_line = linregress(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'])

    
    plt.plot(till_2050_from_2000, second_line.intercept + second_line.slope*till_2050_from_2000, color='b')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
