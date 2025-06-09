from shiny import reactive, ui

from components import bill_rng

def Update(input, output, session):

    @reactive.effect
    @reactive.event(input.reset_tips)
    def _():
        '''
        update inputs of sidebar
        '''
        # panel: tips
        ui.update_slider("total_bill", value=bill_rng)
        ui.update_checkbox_group("time", selected=["Lunch", "Dinner"])

        ui.update_checkbox_group(
            "selected_columns",
            choices=list(df.columns),
            selected=list(df.columns)
        )
        
        # panel: table
        ui.update_select('export_format', )

