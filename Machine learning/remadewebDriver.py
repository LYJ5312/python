from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

def hollys_store_dynamic(result):
    driver = webdriver.Chrome('./chromedriver.exe')

    page = 1
    while True:
        hollys_url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
        print(hollys_url)
        driver.get(hollys_url)
        html = driver.page_source
        soupHollys = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHollys.find('tbody')
        
        # 페이지에 데이터가 더 이상 없으면 종료
        if tag_tbody is None:
            break

        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:
                break
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            result.append([store_name] + [store_sido] + [store_address] + [store_phone])

        page += 1

    driver.quit()
    return

def main():
    result = []
    print('Hollys store crawling (Dynamic) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    hollys_store_dynamic(result)
    hollys_tbl = pd.DataFrame(result, columns=('store', 'sido-gu', 'address', 'phone'))
    hollys_tbl.to_csv('D:/workspaces/python/hollys_dynamic.csv', encoding='cp949', mode='w', index=True)
    del result[:]

if __name__ == '__main__':
    main()
