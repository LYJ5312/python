import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def hollys_store(result):
    for page in range(1, 52):
        hollys_url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
        print(hollys_url)
        response = requests.get(hollys_url)

        # HTTP 요청이 성공한 경우에만 계속

        soupHollys = BeautifulSoup(response.text, 'html.parser')
        tag_tbody = soupHollys.find('tbody')

        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:
                break
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            result.append([store_name, store_sido, store_address, store_phone])

def main():
    result = []
    print('Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    # 사용자에게 선택지 제공
    choice = input('저장할 파일 경로를 지정하시겠습니까? (Y/N): ').upper()

    if choice == 'Y':
        # 사용자가 Y를 선택하면 파일 경로 및 파일명 입력받음
        file_path = input('저장할 파일 경로를 입력하세요: ')
        file_name = input('저장할 파일명을 입력하세요 (예: hollys_data.csv): ')
        file_path = os.path.join(file_path, file_name)
    else:
        # 기존 경로를 사용하더라도 파일명은 입력받음
        file_name = input('저장할 파일명을 입력하세요 (예: hollys_data.csv): ')
        file_path = os.path.join('D:/workspaces/python', file_name)

    hollys_store(result)
    hollys_tbl = pd.DataFrame(result, columns=('store', 'sido-gu', 'address', 'phone'))
    hollys_tbl.to_csv(file_path, encoding='cp949', mode='w', index=True)
    del result[:]

if __name__ == '__main__':
    main()