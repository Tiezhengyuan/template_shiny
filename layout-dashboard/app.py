from shared import app_dir, tips
from shiny import App, reactive, render, ui

from components import *
from module import *
# from app_server import AppServer


# UI components
# UI: analysis tips
panel_tips = ui.layout_sidebar(
    ui.sidebar(
        bill_amount(),
        service_time(),
        reset(),
        open="desktop",
    ),
    ui.layout_columns(
        total_tippers(),
        average_tip(),
        avarage_bill(),
        fill=False,
    ),
    ui.layout_columns(
        # tips_scatter(),
        # tips_percentage(),
        # count_size(),
        cluster_samples(),
        # col_widths=[6, 6, 6, 6],
    ),
)

panel_table = ui.layout_sidebar(
    ui.sidebar(
        export_format(),
        download(),
        open='desktop',
    ),
    ui.layout_columns(
        tips_table(),
    )    
)
navbar_panel = ui.page_navbar(
    ui.nav_spacer(),
    ui.nav_panel("Tips", panel_tips),
    ui.nav_panel("Table", panel_table),
    title='Select...',
    navbar_options=ui.navbar_options(bg="blue", theme="dark", underline=True),
)

# Add page title and sidebar
app_ui = ui.page_fluid(
    # components
    ui.h1('bio-Analyzer', id='page_title'),
    navbar_panel,

    # css
    ui.include_css(app_dir / 'css' / "styles.css"),

    # set properties
    title="Restaurant tipping",
    fillable=True,
)

# load data server
def server(input, output, session):
    Update(input, output, session)
    ServerTips(input, output, session)
    # AppServer(input, output, session)

# create app object
app = App(app_ui, server)

