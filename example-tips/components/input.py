from shiny import ui
from shinywidgets import output_widget

from .icons import bill_rng

def bill_amount():
    return ui.input_slider(
        "total_bill",
        "Bill amount",
        min=bill_rng[0],
        max=bill_rng[1],
        value=bill_rng,
        pre="$",
    )

def service_time():
    return ui.input_checkbox_group(
        "time",
        "Food service",
        choices=["Morning", "Lunch", "Dinner"],
        selected=["Lunch", "Dinner"],
        inline=True,
    )

def export_format():
    return ui.input_select(
        'export_format',
        'Choose export format',
        {'xlsx':'excel', 'csv': 'csv', 'txt': 'text'},
    )

# def select_columns():
#     return ui.input_checkbox_group(
#         "selected_columns",
#         "Select Columns",
#         choices=[],
#         selected=[],
#     )