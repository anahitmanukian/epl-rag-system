### src.ingest.build_docs.py

import pandas as pd
from pathlib import Path


INPUT_FILE = Path("data/processed/epl_all_seasons.csv")
OUT_FILE = Path("data/processed/epl_documents.txt")


def format_match(row):

    text = f"""
Match played on {row['Date']} in {row['season']} season.

Home team: {row['HomeTeam']}
Away team: {row['AwayTeam']}

Final score: {row['HomeTeam']} {row['FTHG']} - {row['FTAG']} {row['AwayTeam']}
Full-time result: {row['FTR']}

Half-time score: {row['HTHG']} - {row['HTAG']}
Half-time result: {row['HTR']}

Referee: {row['Referee']}

Match statistics:
- Home shots: {row['HS']} (on target: {row['HST']})
- Away shots: {row['AS']} (on target: {row['AST']})
- Fouls: Home {row['HF']}, Away {row['AF']}
- Corners: Home {row['HC']}, Away {row['AC']}
- Yellow cards: Home {row['HY']}, Away {row['AY']}
- Red cards: Home {row['HR']}, Away {row['AR']}
"""

    return text.strip()


def build_documents():

    df = pd.read_csv(INPUT_FILE)

    documents = []

    for _, row in df.iterrows():
        doc = format_match(row)
        documents.append(doc)

    OUT_FILE.parent.mkdir(exist_ok=True)

    with open(OUT_FILE, "w", encoding="utf-8") as f:

        for i, doc in enumerate(documents):

            f.write(f"### MATCH {i+1}\n")
            f.write(doc)
            f.write("\n\n")

    print(f"Created {len(documents)} documents")
    print(f"Saved to {OUT_FILE}")


if __name__ == "__main__":
    build_documents()
