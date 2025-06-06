from io import BytesIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from ridgeplot import ridgeplot
from shinywidgets import output_widget, render_plotly, render_widget
from plotly.figure_factory import create_dendrogram

from shiny import App, reactive, render, ui

from .retrieve_data import RetrieveData
from .draw_plot import DrawPlot

def ServerTips(input, output, session):

    @reactive.calc
    def data_tips():
        '''
        data table from shared.tips
        '''
        # get bill amount from input
        bill = input.total_bill()
        tips = RetrieveData().tips()
        idx1 = tips.total_bill.between(bill[0], bill[1])
        idx2 = tips.time.isin(input.time())
        return tips[idx1 & idx2]

    @render.ui
    def total_tippers():
        '''
        value box: total tippers
        '''
        return data_tips().shape[0]

    @render.ui
    def average_tip():
        '''
        value box: average tip
        '''
        d = data_tips()
        if d.shape[0] > 0:
            perc = d.tip / d.total_bill
            return f"{perc.mean():.1%}"

    @render.ui
    def average_bill():
        '''
        value box: average bill
        '''
        d = data_tips()
        if d.shape[0] > 0:
            bill = d.total_bill.mean()
            return f"${bill:.2f}"
    
    @render_plotly
    def plot_bill2tip():
        # card.tips_scatter
        df = data_tips()
        fig = DrawPlot.bill2tip(input, df)
        return fig

    @render.download(filename = 'bill2tip.png')
    def save_pic_bill2tip():
        # card.tips_scatter
        df = data_tips()
        fig = DrawPlot.bill2tip(input, df)
        img_bytes = fig.to_image(format="png", width=1600, height=900, scale=3)
        return BytesIO(img_bytes)

    @render_plotly
    def plot_tip_perc():
        # card.tips_percentage
        data = data_tips()
        fig = DrawPlot.tip_perc(input, data)
        return fig
    
    @render.download(filename='tip_percentage.png')
    def save_pic_tip_perc():
        # card.tips_percentage
        data = data_tips()
        fig = DrawPlot.tip_perc(input, data)
        img_bytes = fig.to_image(format="png", width=1600, height=900, scale=3)
        return BytesIO(img_bytes)

    @render_plotly
    def plot_size():
        # barplot: card.count_size
        data = data_tips()
        fig = DrawPlot.size(input, data)
        return fig

    @render_widget
    def plot_clustering():
        cols = ['tip', 'size']
        data = data_tips()
        X = data[cols]
        # X = np.random.rand(10, 10)
        fig = create_dendrogram(X)
        fig.update_layout(width=600, height=400)
        return fig

######################panel: table
    @render.data_frame
    def table():
        return render.DataGrid(
            data_tips(),
            filters=True,
        )

    # Download handler
    @render.download(
        filename = lambda: f"tips.{input.export_format()}"
    )
    def download_tips():
        df = data_tips()
        extension = input.export_format()
        if extension == 'xlsx':
            output = BytesIO()
            df.to_excel(output, index=False)
            output.seek(0)
            yield output.read()
        elif extension == 'txt':
            yield df.to_csv(sep='\t')
        else:
            yield df.to_csv()

