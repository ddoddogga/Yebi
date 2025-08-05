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

    df.columns = ["day", "hour", "value"]
    df = df[["day", "value"]]

    rows_to_drop = []
    for row in df.itertuples():
        if("Start" in row.day):
            month += 1
            rows_to_drop.append(row.Index)  # 삭제할 인덱스 저장
        else:
            day = int(row.day)
        date_str = f"{year}{month:02d}{day:02d}"
        df.at[row.Index, 'day'] = date_str

    df = df.drop(index=rows_to_drop)

    df.loc[df['value'] < 0, 'value'] = None

    average_df = df.groupby('day', as_index=False)['value'].mean()

    keywords = {
    "강수": "강수_평균.csv",
    "기온": "기온_평균.csv",
    "습도": "습도_평균.csv",
    "풍속": "풍속_평균.csv",
    }

    fileName = "default_data.csv"
    for key, name in keywords.items():
        if key in filePath:
            fileName = name
            break
    folder = os.path.dirname(filePath)  # 폴더 경로만 추출
    newFilePath = os.path.join(folder, fileName)
    
    average_df.to_csv(newFilePath, index=False, encoding="utf-8-sig")

def main():
    makeToAverageCsv("데이터/온도습도강수풍속 데이터/용산구/남영동/남영동_강수_202301_202312.csv")

main()