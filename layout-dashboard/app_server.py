import plotly.express as px
# Load data and compute static values
from shared import app_dir, tips
from shinywidgets import output_widget, render_plotly

from shiny import App, reactive, render, ui, Session

class AppServer:
    
    def __init__(self, input, output, session: Session):
        self.input = input
        self.output = output
        self.session = session

    @reactive.effect
    # @reactive.event(input.reset)
    def __call__(self):
        '''
        sidebar: slide
        '''
        ui.update_slider("total_bill", value=bill_rng)
        ui.update_checkbox_group("time", selected=["Lunch", "Dinner"])

    @reactive.calc
    def tips_data(self):
        '''
        input data
        '''
        bill = self.input.total_bill()
        print('###', bill)
        idx1 = tips.total_bill.between(bill[0], bill[1])
        idx2 = tips.time.isin(input.time())
        return tips[idx1 & idx2]

    @render.ui
    def total_tippers(self):
        '''
        value box: total tippers
        '''
        return self.tips_data().shape[0]

    @render.ui
    def average_tip(self):
        '''
        value box: average tip
        '''
        d = self.tips_data()
        if d.shape[0] > 0:
            perc = d.tip / d.total_bill
            return f"{perc.mean():.1%}"

    @render.ui
    def average_bill(self):
        '''
        value box: average bill
        '''
        d = self.tips_data()
        if d.shape[0] > 0:
            bill = d.total_bill.mean()
            return f"${bill:.2f}"