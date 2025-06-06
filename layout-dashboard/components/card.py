from datetime import date
from shiny import ui
from shinywidgets import output_widget

from .icons import ICONS

def tips_scatter():
    # dot plot
    card_header = ui.card_header(
        "Total bill vs tip",
        ui.popover(
            ICONS["ellipsis"],
            ui.input_radio_buttons(
                "scatter_color",
                None,
                ["none", "sex", "smoker", "day", "time"],
                inline=True,
            ),
            title="Add a color variable",
            placement="top",
        ),
        class_="d-flex justify-content-between align-items-center",
    )
    return ui.card(
        card_header,
        output_widget("plot_bill2tip"),
        # ui.download_button('save_pic_bill2tip', 'Save', width='100px'),
        full_screen=True,
    )

def tips_percentage():
    card_header = ui.card_header(
        "Tip percentages",
        ui.popover(
            ICONS["ellipsis"],
            ui.input_radio_buttons(
                "tip_perc_y",
                "Split by:",
                ["sex", "smoker", "day", "time"],
                selected="day",
                inline=True,
            ),
            title="Add a color variable",
        ),
        class_="d-flex justify-content-between align-items-center",
    )
    return ui.card(
        card_header,
        output_widget("plot_tip_perc"),
        # ui.download_button('save_pic_tip_perc', 'Save', width='100px'),
        full_screen=True,
    )

def count_size():
    card_header = ui.card_header(
        "Count size",
        class_="d-flex justify-content-between align-items-center",
    )
    return ui.card(
        card_header,
        output_widget("plot_size"),
        full_screen=True,
    )

def cluster_samples():
    card_header = ui.card_header(
        "Cluster samples",
        class_="d-flex justify-content-between align-items-center",
    )
    return ui.card(
        card_header,
        output_widget("plot_clustering"),
        full_screen=True,
    )

def operate_data():
    return ui.card(
        ui.card_header("Download"),
        full_screen=True,
    )

def tips_table():
    '''
    table of tips data
    '''
    today = date.today().strftime("%Y-%m-%d")
    return ui.card(
        ui.card_header(
            "Tips",
            class_="table-title",
        ),
        ui.output_data_frame("table"),
        ui.card_footer(
            f"date: {today}",
            class_="table-footer",
        ),
        full_screen=True
    )