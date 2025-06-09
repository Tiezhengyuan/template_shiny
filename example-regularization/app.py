'''
origin code: https://github.com/posit-dev/py-shiny-templates/tree/main/regularization
'''
from shiny import App, ui

from module import *
from component import *
from data import *

# UI components
app_ui = ui.page_fixed(
    get_mathjax(),
    get_h1(),
    slider_strength(),
    plot_1(),
    # Explanation and Explore prose
    explanation(),
    get_h2(),
    # plots separated by real effects (vowels), and zero-effects (consonants)
    plot_23(),
    # add padding to bottom of page
    ui.div(class_="pb-5"),  
)

# server modules
def server(input, output, session):
    Server(input, output, session)

app = App(app_ui, server)
