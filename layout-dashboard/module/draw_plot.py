import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.figure_factory import create_dendrogram
from ridgeplot import ridgeplot

class DrawPlot:

    @staticmethod
    def bill2tip(input, df):
        '''
        scatter plot in card
        '''
        color = input.scatter_color()
        fig = px.scatter(
            df,
            x="total_bill",
            y="tip",
            color=None if color == "none" else color,
            trendline="lowess",
        )
        return fig

    @staticmethod
    def tip_perc(input, data):
        '''
        distribution
        '''
        data["percent"] = data.tip / data.total_bill
        yvar = input.tip_perc_y()
        uvals = data[yvar].unique()
        samples = [[data.percent[data[yvar] == val]] for val in uvals]

        fig = ridgeplot(
            samples=samples,
            labels=uvals,
            bandwidth=0.01,
            colorscale="viridis",
            colormode="row-index",
        )
        fig.update_layout(
            legend=dict(
                orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5
            )
        )
        return fig
    
    @staticmethod
    def size(input, data):
        fig = px.bar(data, y='tip', x='size', barmode='group')
        return fig

    @staticmethod
    def clustering(input, data):
        # cols = ['tip', 'size']
        # X = np.array(data[cols])
        # print(X)
        X = np.random.rand(15, 10)  # 15 samples, 10 features
        fig = create_dendrogram(X)
        fig.update_layout(title='Hierarchical Clustering Dendrogram')
        return fig