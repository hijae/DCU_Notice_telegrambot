# DCU_Notice_telegrambot
 대구가톨릭대학교 공지사항 텔레그램 채널 알림 봇

## Prerequisite 종속성

* python-telegram-bot (`pip install python-telegram-bot`)
* requests (`pip install requests`)
* beautifulsoup4 (`pip install beautifulsoup4`)

## Installation 설치
 텔레그램에서 BotFather을 이용해 봇 생성을 한다. ( https://telegram.me/BotFather )
 발급된 Token Key를 run.py에 yourtoken에 넣는다.
 채널 생성을 하고 봇에게 관리자 권한을 준다.
 채널ID를 확인한다. ( https://api.telegram.org/bot[YourTokenKey]/getUpdates )
 확인한 채널ID를 run.py의 -100125727994대신에 넣는다.
 run.py을 실행한다.
