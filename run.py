"""
github.com/hijae/DCU_Notice_telegrambot
Copyright (c) 2020, Hijae Song
hijae99@gmail.com

제일 최신 게시글 번호와 300초 마다 확인한 첫번째 게시글의 이름 비교
비교 후 같지 않으면 최신 게시글 업데이트 된 것으로 텔레그램 봇으로 업데이트 메시지 전송
        
"""


import requests
import time
from bs4 import BeautifulSoup # pip install beautifulsoup4
import telegram # pip install python-telegram-bot

bot = telegram.Bot(token='yourtoken') # 토큰 입력

if __name__ == '__main__':
    while True:
        try: # 인터넷이 안되는 등 에러가 발생했을 때 다음에 다시 시도하도록 예외처리
            req = requests.get('http://www.cu.ac.kr/plaza/notice/notice') # 공지사항 페이지 접속
            html = req.text # 페이지의 html 코드를 저장
            soup = BeautifulSoup(html, 'html.parser') # html 코드를 파싱
            posts = soup.find("tbody") # tbody 요소를 찾음
            post_name=[] # 게시글 제목을 저장할 리스트
            postlink=[] # 게시글 링크를 저장할 리스트
            latest_name=[] # 이전 게시글의 이름을 저장할 리스트
            with open('data.txt', 'r') as MyFile: # 이전 게시글 목록을 파일에서 읽어옴
                while True:
                    line = MyFile.readline()
                    if not line:
                        break
                    latest_name.append(line.rstrip())
            
            for link in posts.find_all('a'): # a 태그를 찾음
                if link.get('href')!="#pdsWinOpen" and link.get('title')!="첨부파일 다운로드": #첨부파일, 다중첨부파일 무시
                    post_name.append(link.text.strip()) # 게시글 제목,링크를 저장
                    postlink.append(link.get('href'))
            nametemp = list(set(post_name) - set(latest_name))
            if len(nametemp)>= 1 : # 새 게시글이 있을 경우
                latest_name = post_name # 현재 게시글 이름 목록을 저장
                with open('data.txt', 'w') as MyFile:
                    for i in latest_name:
                        MyFile.write(i+'\n') #파일로 저장
                for i in nametemp:
                    links = 'http://www.cu.ac.kr'+postlink[post_name.index(i)] # 게시글 링크를 완성
                    text = '<새 공지사항>'+'\n'+i+'\n'+str(links) # 메시지를 완성
                    bot.sendMessage(-1001257279942, text) # 메시지를 보냄
                    # 프롬프트 로그
                    print(text)
                    time.sleep(5) # 봇 스팸 감지 방지 5초 대기
            print('bot 동작 중 현재', post_name) # 프롬프트 로그
        except:
            print('bot error 현재', post_name) # 프롬프트 로그
        time.sleep(300-len(nametemp)*5) # 300초(5분) 간격으로 확인. 텔레그램 스팸 방지 무시를 위해 5초에 한번만 전송

