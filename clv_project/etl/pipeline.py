import pandas as pd

def transform():
    df = pd.read_csv("data/clv_data_5000.csv")

    df['year'] = pd.to_datetime(df['date']).dt.year

    df.to_csv("data/processed.csv", index=False)

if __name__ == "__main__":
    transform()
