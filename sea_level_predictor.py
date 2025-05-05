import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = pd.Series(range(1880, 2051))
    y1 = res.intercept + res.slope * x1
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = pd.Series(range(2000, 2051))
    y2 = res_recent.intercept + res_recent.slope * x2
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')
    ax.plot(x1, y1, 'r', label='Best Fit: All Data')
    ax.plot(x2, y2, 'g', label='Best Fit: Since 2000')
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.legend()
    fig.savefig('sea_level_plot.png')
    return fig
