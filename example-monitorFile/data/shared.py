
from pathlib import Path
import subprocess

import pandas as pd
from shiny import reactive
from shiny.session import session_context

# Launch process to generate logs
app_dir = Path(__file__).parent
cmd = ["python", app_dir / "populate-logs.py"]
process = subprocess.Popen(cmd)


# File reader polls the file (every second by default) for changes
#
# NOTE: the session_context(None) here is only necessary at the moment
# for Express -- this should improve/change in a future release
# https://github.com/posit-dev/py-shiny/issues/1079
log_file = app_dir / "logs.csv"
with session_context(None):
    
    @reactive.file_reader(log_file)
    def get_logs():
        return pd.read_csv(log_file)