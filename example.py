import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. 예시 데이터 생성
# '지역', '평균_기온', '건물_밀집도'를 독립 변수로, '화재_발생수'를 종속 변수로 설정
data = {
    '지역': ['서울', '부산', '대구', '서울', '부산', '대구', '서울', '부산'],
    '평균_기온': [15, 18, 12, 16, 17, 13, 14, 19],
    '건물_밀집도': [80, 65, 50, 85, 60, 55, 75, 70],
    '화재_발생수': [10, 5, 8, 12, 6, 9, 11, 7]
}
df = pd.DataFrame(data)

print("--- 원본 데이터프레임 ---")
print(df)
print("\n" + "="*50 + "\n")

# 2. '지역' 열을 원-핫 인코딩으로 변환 (drop_first=True 적용)
# 이제 '지역' 열이 모델이 이해할 수 있는 숫자 형태로 바뀔 거야.
df_encoded = pd.get_dummies(df, columns=['지역'], drop_first=True)

print("--- 원-핫 인코딩 후 데이터프레임 ---")
print(df_encoded)
print("\n" + "="*50 + "\n")

# 3. 독립 변수 (X)와 종속 변수 (y) 나누기
# 독립 변수(X): 화재 발생수를 예측하는 데 사용하는 입력 데이터
# 종속 변수(y): 우리가 예측하고자 하는 값
X = df_encoded.drop('화재_발생수', axis=1) # '화재_발생수' 열을 제외한 나머지
y = df_encoded['화재_발생수'] # '화재_발생수' 열만 추출

print("--- 독립 변수(X) ---")
print(X)
print("\n--- 종속 변수(y) ---")
print(y)