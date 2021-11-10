# DCU_Notice_telegrambot
 대구가톨릭대학교 공지사항 텔레그램 채널 알림 봇  
 daegu catholic university notice telegram channel bot
 5분마다 공지사항을 확인하여 변경되면 알려줍니다.

## 종속성

* python-telegram-bot (`pip install python-telegram-bot`)
* requests (`pip install requests`)
* beautifulsoup4 (`pip install beautifulsoup4`)

## 설치
 텔레그램에서 BotFather을 이용해 봇 생성을 한다. ( https://telegram.me/BotFather )  
 발급된 Token Key를 run.py에 yourtoken에 넣는다.  
 채널 생성을 하고 봇에게 관리자 권한을 준다.  
 채널ID를 확인한다. ( https://api.telegram.org/bot[YourTokenKey]/getUpdates )  
 확인한 채널ID를 run.py의 -100125727994대신에 넣는다.  
 run.py을 실행한다.  
 
 ## To-do
 * ~~인터넷 끊긴 경우 대처~~
 * 버그 확인
 
 ## Test
 https://t.me/DCU_Notice
 테스트용 링크입니다. 테스트로 알림이 올수있습니다.
