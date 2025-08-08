import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_weather(location):
    # 브라우저 열기
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)

    # 네이버 날씨 검색 페이지 열기
    driver.get(f'https://search.naver.com/search.naver?query={location} 날씨')
    time.sleep(2)

    # 강수량 추출
    rain_el = driver.find_element(By.CSS_SELECTOR, '.graph_wrap.rainfall li:nth-child(1) div.data_inner')
    rain_text = rain_el.get_attribute('innerText')
    rain = float(rain_text.replace('.', '').replace('~', ''))
    
    # 날씨 추출
    weather_list = driver.find_elements(By.CLASS_NAME, 'weather_info')
    weather = weather_list[0].text.split('\n')

    # 기온 추출
    temp = float(weather[3].replace('°', ''))

    # 습도 추출
    humi = float((weather[7].split('습도 ')[1]).split('%')[0])

    # 풍속 추출
    wind = float((weather[7].split('풍 ')[1]).replace('m/s', ''))

    return rain, temp, humi, wind
