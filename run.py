"""
github.com/hijae/DCU_Notice_telegrambot
Copyright (c) 2020, Hijae Song
hijae99@gmail.com
"""

import requests

import time

from bs4 import BeautifulSoup

import telegram



bot = telegram.Bot(token='yourtoken')



if __name__ == '__main__':

    # 제일 최신 게시글의 이름 저장
    latest_name = []
    while True:
        req = requests.get('http://www.cu.ac.kr/plaza/notice/notice')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("tbody")
        post_name=[]
        postlink=[]
        latest_name=[]
        with open('data.txt', 'r') as MyFile:
            while True:
                line = MyFile.readline()
                if not line:
                    break
                latest_name.append(line.rstrip())
        for link in posts.find_all('a'):
            if link.get('href')!="#pdsWinOpen" and link.get('title')!="첨부파일 다운로드": #첨부파일, 다중첨부파일 무시
                post_name.append(link.text.strip())
                postlink.append(link.get('href'))
        nametemp = list(set(post_name) - set(latest_name))
        if len(nametemp)>= 1 :
            latest_name = post_name
            with open('data.txt', 'w') as MyFile:
                for i in latest_name:
                    MyFile.write(i+'\n')
            for i in nametemp:
                links = 'http://www.cu.ac.kr'+postlink[post_name.index(i)]
                text = '<새 공지사항>'+'\n'+i+'\n'+str(links)
                bot.sendMessage(-1001257279942, text)
                # 프롬프트 로그
                print(text)
                time.sleep(5)
        
        # 제일 최신 게시글 번호와 300초 마다 크롤링한 첫번째 게시글의 이름 비교
        # 비교 후 같지 않으면 최신 게시글 업데이트 된 것으로 텔레그램 봇으로 업데이트 메시지 전송
        
        print('bot 동작 중 현재', post_name)
        time.sleep(300-len(nametemp)*5) # 300초(5분) 간격으로 크롤링

