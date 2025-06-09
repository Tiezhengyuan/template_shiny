import random
import time
from datetime import datetime
from pathlib import Path

import pandas as pd

log_path = Path(__file__).parent / "logs.csv"

while True:
    status = "status" + str(random.randint(0, 20))
    # Create a new DataFrame with the current time and the random status
    messages = [
        "Running smoothly",
        "On fire",
        "Taking a nap",
        "Feeling happy",
        "Feeling sad",
        "Server is plotting world domination",
        "Server is questioning its existence",
        "Server is craving for digital pizza",
        "Server is dreaming of electric sheep",
        "Server is running on pure caffeine",
    ]
    message = random.choice(messages)
    df = pd.DataFrame(
        {"date": [datetime.now()], "status": [status], "message": [message]}
    )

    if not log_path.exists():
        df.to_csv(log_path, mode="w", header=True, index=False)
    else:
        df_current = pd.read_csv(log_path)
        # If we get over 10000 rows, just start over
        if len(df_current) > 10000:
            df.to_csv(log_path, mode="w", header=True, index=False)
        else:
            df.to_csv(log_path, mode="a", header=False, index=False)
    # Wait for a second before the next append operation
    time.sleep(random.randint(1, 5))