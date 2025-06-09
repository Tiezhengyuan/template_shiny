# Load data and compute static values
from shared import app_dir, tips
from shiny import reactive

def ServerData(input, output, session):

    @reactive.calc
    def data_tips():
        '''
        data table from shared.tips
        '''
        # get bill amount from input
        bill = input.total_bill()
        idx1 = tips.total_bill.between(bill[0], bill[1])
        idx2 = tips.time.isin(input.time())
        return tips[idx1 & idx2]