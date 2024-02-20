import os
import sys
import urllib.request
import datetime
import time
import json
import urllib.parse         # 필요한 urllib.parse 모듈 추가

client_id = 'QKTxTFeCFT_Py018IGfu'
client_secret = 'iPRsOklkKn'

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)  # 변수명 수정
    req.add_header("X-Naver-Client-Secret", client_secret)  # 변수명 수정

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s]Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)  # urllib.parse 모듈 사용

    url = base + node + parameters
    responseDecod = getRequestUrl(url)

    if responseDecod == None:
        return None
    else:
        return json.loads(responseDecod)

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')  # 날짜 형식 변환
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt': cnt, 'title': title, 'description': description, 'org_link': org_link, 'link': link, 'pDate': pDate})
    return

def main():
    node = 'news'
    srcText = input('검색어를 입력하세요:')
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    total = jsonResponse['total']

    while (jsonResponse != None) and (jsonResponse['display'] != 0):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)  # 변수명 수정

    print('전체 검색 : %d 건' % total)

    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        json.dump(jsonResult, outfile, indent=4, sort_keys=True, ensure_ascii=False)  # 변수명 수정

    print("가져온 데이터: %d 건" % (cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))

if __name__ == '__main__':
    main()
