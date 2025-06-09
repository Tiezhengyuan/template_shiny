from shiny import render, reactive
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from data.compare import *

def Server(input, output, session):
  
    @reactive.calc
    def models():
        '''
        reactive Calc that runs LASSO, Ridge, and Linear models on generated data
        '''
        # data
        nsims = 100
        sim = [simulate_data(n=1000) for i in range(0, nsims)]
        sim_alpha = [compare(df, alpha=input.alpha()) for df in sim]
        sim_alpha = pd.concat(sim_alpha)
        return sim_alpha
    
    @render.plot
    def plot_coef():
        '''
        output plot of all simulation coefficients
        '''
        # get data from reactive Calc
        sim_alpha = models()

        # create plot and manage aesthetics
        fig, ax = plt.subplots()
        xticks = ["A", "E", "I", "O", "U", "Y", "W", "B", "C", "D",
            "G","H", "J", "K",]
        ax2 = sns.boxplot(
            data=sim_alpha,
            x="conames",
            y="coefs",
            hue="model",
            ax=ax,
            order=xticks,
        )
        tt = "Coefficient Estimates when alpha = " + str(input.alpha())
        ax2.set(xlabel="", ylabel="Coefficient Value", title=tt)
        return fig

    
    @render.plot
    def plot_VOWELS():
        '''
        all simulation coefficients (vowels only)
        '''
        # get data from reactive Calc
        sim_alpha = models()
        features = list('AEIOUYW')
        sim_alpha_V = sim_alpha[sim_alpha['conames'].isin(features)]

        # create plot and manage aesthetics
        fig, ax1 = plt.subplots()
        ax = sns.boxplot(
            x="conames",
            y="coefs",
            hue="model",
            data=sim_alpha_V,
            ax=ax1,
            order=features,
        )
        ax.set(
            xlabel="Features",
            ylabel="Coefficient Value",
            title=f"VOWEL Coefficient Estimates when alpha = {input.alpha()}"
        )
        return fig

    @render.plot
    def plot_CONSONANTS():
        '''
        all simulation coefficients (consonants only)
        '''
        # get data from reactive Calc
        sim_alpha = models()
        features = list('BCDGHJK')
        sim_alpha_C = sim_alpha[sim_alpha['conames'].isin(features)]

        # create plot and manage aesthetics
        fig, ax1 = plt.subplots()
        ax = sns.boxplot(
            x="conames",
            y="coefs",
            hue="model",
            data=sim_alpha_C,
            ax=ax1,
            order=features,
        )
        ax.set(
            xlabel="Features",
            ylabel="Coefficient Value",
            title=f"CONSONANT Coefficient Estimates when alpha = {input.alpha()}"
        )
        return fig

