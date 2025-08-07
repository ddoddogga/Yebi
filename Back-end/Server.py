from fastapi import FastAPI, Request # 웹 API 서버를 생성하기 위한 파이썬 프레임워크
import uvicorn # FastAPI 서버를 실행하기 위한 ASGI 서버
from datetime import datetime as dt
import pandas as pd
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

app = FastAPI() # FastAPI 서버 객체 생성

@app.post('/webhook') # POST 요청 시 실행
async def webhook(request: Request): # 비동기 실행
    # 위치 추출
    req = await request.json()
    location = req['action']['detailParams']['sys_location']['origin']

    # 월, 요일, 계절 불러오기
    now = dt.now()
    month = now.month
    weekday = now.weekday()
    season = get_season(month)

    # 강수량, 기온, 습도, 풍속 불러오기 (나중에 웹 크롤링으로 날씨 불러오기)
    rain = 1.1
    temp = 8.18
    humi = 10.16
    wind = 3.5

    # 입력값 생성하기
    input_value = pd.DataFrame([{
        'month': month,
        'weekday': weekday,
        'season': season,
        'rain': rain,
        'temp': temp,
        'humi': humi,
        'wind': wind
    }])

    # 모델 불러오기 & 예측하기
    try:
        model = joblib.load(f'{location}.yebi')
        print(f'INFO:\t  Get model: {location}.yebi')

        prediction = model.predict(input_value)[0]
        risk_level = int(round(prediction))

    except:
        risk_level = 0
        print('INFO:\t  Get model failed')

    response = { # 응답
        'version': "2.0",
        'template': {
            'outputs': [
                {
                    'simpleText': {
                        'text': f'{location}의 화재 위험도는 {risk_level}레벨이야! 조심해!'
                    }
                }
            ]
        }
    }

    return response

if __name__ == '__main__':
    uvicorn.run('Server:app', host = '127.0.0.1', port = 8000, reload = True)
