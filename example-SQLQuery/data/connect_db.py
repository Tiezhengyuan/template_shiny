import urllib.request
from pathlib import Path

import duckdb

app_dir = Path(__file__).parent
db_file = app_dir / "weather.db"


def load_csv(con, csv_name, table_name):
    csv_url = f"https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-12-20/{csv_name}.csv"
    local_file_path = app_dir / f"{csv_name}.csv"
    urllib.request.urlretrieve(csv_url, local_file_path)
    con.sql(
        f"CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{local_file_path}')"
    )


if not Path.exists(db_file):
    con = duckdb.connect(str(db_file), read_only=False)
    load_csv(con, "weather_forecasts", "weather")
    load_csv(con, "cities", "cities")
    con.close()

con = duckdb.connect(str(db_file), read_only=True)