import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def get_season(month):
    if month in [3, 4, 5]:
        return 0
    elif month in [6, 7, 8]:
        return 1
    elif month in [9, 10, 11]:
        return 2
    else:
        return 3

def preprocessing(df):
    df['date'] = pd.to_datetime(df['date'], format = '%Y%m%d') # 날짜를 날짜 형식으로 변환
    df['month'] = df['date'].dt.month # 월 추출
    df['weekday'] = df['date'].dt.weekday # 요일 추출 (월요일 = 0, 화요일 = 1, 수요일 = 2, ... , 일요일 = 6)
    df['season'] = df['month'].apply(get_season) # 계절 추출 (봄 = 0, 여름 = 1, 가을 = 2, 겨울 = 3)
    return df

def create_model(location):
    # csv 파일 불러오기
    df = pd.read_csv(f'{location}.csv')

    # 데이터 전처리
    df = preprocessing(df)

    # 특성과 타겟 설정
    feature = df[['month', 'weekday', 'season', 'rain', 'temp', 'humi', 'wind']]
    target = df['fire_count']

    # 학습 & 테스트 데이터 분할
    train_input, test_input, train_output, test_output = train_test_split(feature, target, test_size = 0.3, random_state = 42)

    # 모델 생성
    model = RandomForestRegressor(n_estimators = 100, random_state = 42)

    # 모델 학습
    model.fit(train_input, train_output)

    # 예측 & 정수로 변환
    prediction = model.predict(test_input)
    prediction_round = prediction.round().astype(int)

    # 모델 저장
    joblib.dump(model, f'{location}.yebi')

    # 평가
    mse = mean_squared_error(test_output, prediction_round)
    rs = r2_score(test_output, prediction_round)
    print(f'―――――――――― {location} ――――――――――')
    print(f'ㆍMean squared error: {mse}')
    print(f'ㆍR2 score: {rs}\n')

def main():
    print('―――――――――― Infomation ――――――――――')
    print('ㆍMean squared error: 오차의 제곱의 평균, 0에 가까울수록 좋음')
    print('ㆍR2 score: 정확도, 1에 가까울수록 좋음\n')
    create_model('강남구')
    create_model('강동구')
    create_model('강북구')
    create_model('강서구')
    create_model('관악구')
    create_model('광진구')
    create_model('구로구')
    create_model('금천구')
    create_model('노원구')
    create_model('도봉구')
    create_model('동대문구')
    create_model('동작구')
    create_model('마포구')
    create_model('서대문구')
    create_model('서초구')
    create_model('성동구')
    create_model('성북구')
    create_model('송파구')
    create_model('양천구')
    create_model('영등포구')
    create_model('용산구')
    create_model('은평구')
    create_model('종로구')
    create_model('중구')
    create_model('중랑구')
    
if __name__ == '__main__':
    main()
