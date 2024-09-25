import pandas as pd

def load_and_preview_data(file_path):
    data = pd.read_csv(file_path)
    return data.head()
