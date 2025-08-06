import pandas as pd

# 원하는 구 입력
def loadFireDf(location):
    # 접수일시, 시군구명
    DATE = "RCPT_DT"
    LOCATION = "SGG_NM"
    fire = pd.read_csv("데이터/화재 데이터/화재 현황_2023_전국.csv")
    fire = fire[[LOCATION, DATE]]
    fire.columns = ['location', 'date']
    fire['date'] = fire['date'].astype(str).str[:8].astype(int)
    return fire[fire['location'] == location].reset_index(drop=True)

def main():
    print(loadFireDf())

if __name__ == "__main__":
    main()