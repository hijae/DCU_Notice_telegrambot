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

    # 제일 최신 게시글의 번호 저장
    latest_num = 0
    while True:
        req = requests.get('http://www.cu.ac.kr/plaza/notice/notice')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("tbody")
        flag=0
        for link in posts.find_all('td'):
            post_num=link.text.strip()
            break
        for link in posts.find_all('a'):
            post_name=link.text.strip()
            postlink=link.get('href')
            break

        # 제일 최신 게시글 번호와 600초 마다 크롤링한 첫번째 게시글의 번호 비교
        # 비교 후 같지 않으면 최신 게시글 업데이트 된 것으로 텔레그램 봇으로 업데이트 메시지 전송
        if latest_num != post_num :
            latest_num = post_num
            links = 'http://www.cu.ac.kr/'+postlink

            text = '<대구가톨릭대학교 공지사항 업데이트>'+'\n'+post_num+'\n'+post_name+'\n'+links
            bot.sendMessage(-1001257279942, text)
            # 프롬프트 로그
            print(text)
        time.sleep(300) # 600초(10분) 간격으로 크롤링
        print('bot 동작 중 현재 게시글 번호' + latest_num)
