import pandas as pd
import os

def mergeWeatherCsv(root_dir):
    rainFilePath = os.path.join(root_dir, '강수_평균.csv')
    tempFilePath = os.path.join(root_dir, '기온_평균.csv')
    humiFilePath = os.path.join(root_dir, '습도_평균.csv')
    windFilePath = os.path.join(root_dir, '풍속_평균.csv')
    # 각각 파일 불러오기
    rain = pd.read_csv(rainFilePath)
    temp = pd.read_csv(tempFilePath)
    humi = pd.read_csv(humiFilePath)
    wind = pd.read_csv(windFilePath)

    # 열 이름 바꾸기
    rain.rename(columns={'value': 'rain'}, inplace=True)
    temp.rename(columns={'value': 'temp'}, inplace=True)
    humi.rename(columns={'value': 'humi'}, inplace=True)
    wind.rename(columns={'value': 'wind'}, inplace=True)

    # date 기준으로 차례대로 merge
    df = rain.merge(temp, on='date').merge(humi, on='date').merge(wind, on='date')

    # # 결과 확인
    # print(df)

    # CSV로 저장하고 싶으면
    newFilePath = os.path.join(root_dir, '날씨_통합.csv')
    df.to_csv(newFilePath, index=False, encoding="utf-8-sig")

def Allmerge():
    root_dir = "데이터/온도습도강수풍속 데이터"  # 탐색할 최상위 폴더

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if dirname.endswith("동"):  # 동 폴더만 처리
                full_path = os.path.join(dirpath, dirname)
                mergeWeatherCsv(full_path)
    print("완료")
                
def main():
    Allmerge()

main()
