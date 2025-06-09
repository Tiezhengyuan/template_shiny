from pathlib import Path
from shiny import ui

# Import helper functions from local modules
from module.shared import data_dir

def get_mathjax():
    # Allow LaTeX to be displayed via MathJax
    _mathjax = ui.head_content(
        ui.tags.script(
        src="https://mathjax.rstudio.com/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
        ),
        ui.tags.script("if (window.MathJax) MathJax.Hub.Queue(['Typeset', MathJax.Hub]);"),
    )
    return _mathjax

def restrict_width(*args, sm=None, md=None, lg=None, pad_y=5, **kwargs):
    '''
    Restrict width of content
    '''
    cls = "mx-auto"
    if sm:
        cls += f" col-sm-{sm}"
    if md:
        cls += f" col-md-{md}"
    if lg:
        cls += f" col-lg-{lg}"

    return ui.div(
        *args,
        {"class": cls},
        {"class": f"py-{pad_y}"},
        **kwargs
    )

def get_h1():
    h1 = ui.h1(
        "How Does Regularization Strength Affect Coefficient Estimates?",
        class_="text-lg-center text-left",
    )
    return restrict_width(h1, sm=10, md=10, lg=8,)

def plot_1():
    p1 = ui.output_plot("plot_coef")
    return restrict_width(p1, lg=11)

def slider_strength():
    '''
    input.alpha()
    '''
    slider = ui.input_slider(
        "alpha",
        "Select a Regularization Strength:",
        0.000000001,
        1,
        0.1,
        step=0.01,
        width="100%",
    )
    tips = ui.p(
        {"class": "pt-4 small"},
        "(Notice how, as the strength increases, lasso coefficients approach 0)",
    )
    return restrict_width(slider, tips, sm=10, md=7, lg=5, pad_y=4,)

def explanation():
    prose = ui.markdown(open(data_dir / "prose.md").read())
    return restrict_width(prose, sm=10, md=10, lg=6)

def get_h2():
    h2 = ui.h2("Plots Separated by Vowels and Consonants", class_="text-center")
    return restrict_width(h2, lg=11)

def plot_23():
    p2 = ui.output_plot("plot_VOWELS")
    p3 = ui.output_plot("plot_CONSONANTS")
    return restrict_width(p2, p3, lg=11, pad_y=0,)