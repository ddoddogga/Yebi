import pandas as pd
import os

def averageByGu(root_dir):
    weather_list = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith("날씨_통합.csv"):
                full_path = os.path.join(dirpath, filename)
                df = pd.read_csv(full_path)
                weather_list.append(df)
    
    all_data = pd.concat(weather_list)
    average = all_data.groupby('date').mean().reset_index()

    new_file_path = os.path.join(root_dir, "날씨_통합_구.csv")
    average.to_csv(new_file_path, index=False, encoding="utf-8-sig")

def allAverageByGu():
    root_dir = "데이터/온도습도강수풍속 데이터"
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if dirname.endswith("구"):
                full_path = os.path.join(dirpath, dirname)
                averageByGu(full_path)

def main():
    allAverageByGu()

main()