import calendar
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

year = 2023
days_in_year = 366 if calendar.isleap(year) else 365
print(days_in_year)

# weather = pd.read_csv('./데이터/온도습도강수풍속 데이터/남영동/남영동_강수_202301_202312.csv')
fireDf = pd.read_csv('./데이터/화재 데이터/전국 다중이용업소 데이터셋_통합본.csv')
yongSanFireDf = fireDf[fireDf['상호주소'].str.contains('서울특별시 용산구', na=False)]
print(yongSanFireDf)

# 일단 남영동만
for day in range(days_in_year):
    


# x = [[1, 2, 4, 2],
#      [1, 2, 3, 4]]
# y = [1, 0]
# # random_state에 값을 할당하면(난수 시드값 고정) 결과가 고정됨.
# clf = RandomForestClassifier(random_state=0)
# # 용산구 동자동은 남영동에 속함

# clf.fit(x, y)

# print(clf.predict([[3, 4, 50, 4]]))