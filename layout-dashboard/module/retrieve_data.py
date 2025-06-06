# Load data and compute static values
from shared import app_dir, tips
from shiny import reactive

class RetrieveData:

    def tips(self):
        '''
        data from shared.tips
        '''
        return tips