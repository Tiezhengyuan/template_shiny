from pathlib import Path
import pandas as pd


app_dir = Path(__file__).parent.parent

class ProcessData:
    def __init__(self, data_dir=None):
        self.data_dir = app_dir / 'data' if \
            data_dir is None else data_dir

    def load_penguins(self):
        infile = self.data_dir / "penguins.csv"
        df = pd.read_csv(infile)
        return df
