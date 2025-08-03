import pandas as pd

name_map = {
    "서울특별시": "서울",
    "부산광역시": "부산",
    "대구광역시": "대구",
    "인천광역시": "인천",
    "광주광역시": "광주",
    "대전광역시": "대전",
    "울산광역시": "울산",
    "세종특별자치시": "세종",
    "경기도": "경기",
    "강원특별자치도": "강원",
    "충청북도": "충북",
    "충청남도": "충남",
    "전라북도": "전북",
    "전라남도": "전남",
    "경상북도": "경북",
    "경상남도": "경남",
    "제주특별자치도": "제주"
}

building_df = pd.read_csv("데이터/건축물_현황.csv")
area_df = pd.read_csv("데이터/지역별_면적.csv")

building_df = building_df.iloc[3:, :-1].copy()
building_df.columns = ["시도", "2019", "2020", "2021", "2022", "2023"]
building_df.iloc[:, 1:] = building_df.iloc[:, 1:].astype(int)
print(building_df)

area_df = area_df.iloc[1:].copy()
area_df.columns = ["시도", "2019", "2020", "2021", "2022", "2023"]
area_df["시도"] = area_df["시도"].map(name_map)
area_df.iloc[:, 1:] = area_df.iloc[:, 1:].astype(int)
print(area_df)

building_df.set_index("시도", inplace=True)
area_df.set_index("시도", inplace=True)

density_df = building_df / area_df
density_df.reset_index(inplace=True)
print(density_df)
density_df.to_csv("데이터/건물밀도_시도별.csv", index=False, encoding="utf-8-sig")