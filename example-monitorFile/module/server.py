from shiny import render, reactive
import pandas as pd

# Import the reactive file reader (logs) and the process the external
# process that generates the logs
from data.shared import get_logs, process

def Server(input, output, session):

    @reactive.calc
    def current():
        df = get_logs()
        return df.iloc[-1]

    @render.text
    def cur_message():
        return current()["message"]

    @render.text
    def cur_status():
        return current()["status"]

    @render.text
    def last_update():
        dates = pd.to_datetime(current()["date"])
        return dates.strftime("%H:%M:%S")

    @render.text
    def n_messages():
        df = get_logs()
        return len(df)


    @render.data_frame
    def df():
        df = get_logs()
        df = df.sort_values("date", ascending=False)
        return df

    @render.data_frame
    def message_counts():
        df = get_logs()
        counts = df["message"].value_counts().reset_index()
        counts.columns = ["message", "count"]
        counts = counts.sort_values("count", ascending=False)
        return render.DataGrid(
            counts,
            filters=True
        )

    # kill the process
    session.on_ended(process.kill)

