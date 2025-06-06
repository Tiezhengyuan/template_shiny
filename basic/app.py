# from shiny import render, ui
# from shiny.express import input

# ui.panel_title("Hello Shiny!")
# ui.input_slider("n", "N", 0, 100, 20)


# @render.text
# def txt():
#     return f"n*2 is {input.n() * 2}"


from shiny import App, ui, render
from shinywidgets import output_widget, render_widget
import plotly.figure_factory as ff
import numpy as np
np.random.seed(1)

# Sample data
X = np.random.rand(10, 10)  # Replace with your own data

app_ui = ui.page_fluid(
    output_widget("dendrogram"),  # Container for the dendrogram
)

def server(input, output, session):
    @render_widget
    def dendrogram():
        fig = ff.create_dendrogram(X)  # Create the dendrogram
        fig.update_layout(width=800, height=500)
        return fig

app = App(app_ui, server)

