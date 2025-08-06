import pandas as pd
import os
from loadFireDf import loadFireDf

# 구 입력
def makeInputData(location):
    fire_df = loadFireDf(location)
    fire_counts = fire_df['date'].value_counts().reset_index()
    fire_counts.columns = ['date', 'fire_count']

    file_path = os.path.join("데이터/온도습도강수풍속 데이터", location, "날씨_통합_구.csv")
    weather_df = pd.read_csv(file_path)

    merged_df = pd.merge(weather_df, fire_counts, on="date", how="left")
    merged_df['fire_count'] = merged_df['fire_count'].fillna(0).astype(int)
    
    new_file_path = os.path.join("데이터/입력 데이터/", location+".csv")
    merged_df.to_csv(new_file_path, index=False, encoding='utf-8-sig')

def makeAllInputData():
    root_dir = "데이터/온도습도강수풍속 데이터"
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if dirname.endswith("구"):
                makeInputData(dirname)

def main():
    makeAllInputData()

if __name__ == "__main__":
    main()