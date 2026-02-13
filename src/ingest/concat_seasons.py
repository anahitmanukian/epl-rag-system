### src.ingest.concat_seasons.py

import pandas as pd
from pathlib import Path


DATA_DIR = Path("data/raw")
OUT_FILE = Path("data/processed/epl_all_seasons.csv")


def concat_seasons():

    all_files = list(DATA_DIR.glob("*.csv"))

    if not all_files:
        raise ValueError("No CSV files found!")

    dfs = []

    for file in all_files:
        print(f"Loading {file.name}")

        df = pd.read_csv(file)

        # Optional: add season from filename
        season = file.stem.replace("epl_", "")

        df["season"] = season

        dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)

    OUT_FILE.parent.mkdir(exist_ok=True)

    full_df.to_csv(OUT_FILE, index=False)

    print(f"Saved {len(full_df)} rows to {OUT_FILE}")


if __name__ == "__main__":
    concat_seasons()
