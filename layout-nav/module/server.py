
import seaborn as sns
from shiny import render

from .process_data import ProcessData

def Server(input, output, session):
    @render.plot
    def hist():
        df = ProcessData().load_penguins()
        fig = sns.histplot(
            df,
            x=input.var(),
            facecolor="#007bc2",
            edgecolor="white"
        )
        return fig.set(xlabel=None)

    @render.data_frame
    def penguins_data():
        df = ProcessData().load_penguins()
        cols = ["species", "island", input.var()]
        return df[cols]
