import pandas as pd
import os

# pd.set_option('display.max_rows', None)   # 모든 행 출력
# # pd.reset_option('display.max_rows') # 취소

def makeToAverageCsv(filePath):
    df = pd.read_csv(filePath)
    rawStartDay = df.columns[2]
    startDay = rawStartDay.split(" Start : ")[1].strip()
    year = startDay[:4]
    month = 1
    day = 0

    df.columns = ["date", "hour", "value"]
    df = df[["date", "value"]]

    rows_to_drop = []
    for row in df.itertuples():
        if "Start" in row.date:
            month += 1
            rows_to_drop.append(row.Index)  # 삭제할 인덱스 저장
        else:
            day = int(row.date)
        date_str = f"{year}{month:02d}{day:02d}"
        df.at[row.Index, 'date'] = date_str

    df = df.drop(index=rows_to_drop)

    if "기온" not in os.path.basename(filePath):
        df.loc[df['value'] < 0, 'value'] = None

    average_df = df.groupby('date', as_index=False)['value'].mean()

    keywords = {
    "강수": "강수_평균.csv",
    "기온": "기온_평균.csv",
    "습도": "습도_평균.csv",
    "풍속": "풍속_평균.csv",
    }

    newFileName = ""
    for key, name in keywords.items():
        if key in os.path.basename(filePath):
            newFileName = name
            break
    folder = os.path.dirname(filePath)  # 폴더 경로만 추출
    newFilePath = os.path.join(folder, newFileName)
    
    average_df.to_csv(newFilePath, index=False, encoding="utf-8-sig")

def delete_csvs(delFileName, root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == delFileName:
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)
                print(f"삭제됨: {file_path}")

def makeAllAverageCsv():
    root_dir = "데이터/온도습도강수풍속 데이터"  # 탐색할 최상위 폴더

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith("202312.csv"):  # csv 파일만 처리
                full_path = os.path.join(dirpath, filename)
                makeToAverageCsv(full_path)

def main():
    makeAllAverageCsv()    
    

main()