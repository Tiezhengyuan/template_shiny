import seaborn as sns
from shiny import render
from shared import df

def Server(input, output, session):

    @render.plot
    def hist():
        hue = "species" if input.species() else None
        sns.kdeplot(df, x=input.var(), hue=hue)
        if input.show_rug():
            sns.rugplot(
                df, x=input.var(), hue=hue, color="black", alpha=0.25
            )

