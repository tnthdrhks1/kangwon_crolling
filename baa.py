import pandas as pd               
from selenium import webdriver
import requests
from bs4 import BeautifulSoup #크롤링을 위한 BeautifulSoup, selenium 모듈 가져옴
import re


class Football: 
    def __init__(self, address):
        self.address = address #주소 : url을 객체로 설정

    def search (self): #데이터를 가져올 함수
        with open('menu.csv', 'w', encoding='utf-8-sig') as file:

            driver = webdriver.Chrome('C:\chrome\driver\chromedriver')

            url = self.address # 객체로 만든 주소를 입력][]
            driver.get(url)
            driver.implicitly_wait(3)

            page = driver.page_source
            team_rank_list = BeautifulSoup(page,"html.parser")
            bab_day = team_rank_list.select('#contents > table > thead > tr > th') #날짜 크롤링 할 좌표
            bab_menu = team_rank_list.select('#contents > table > tbody > tr') #메뉴 크롤링 할 좌표
            
            #####################################################
            #                날짜 크롤링 시작                    #
            #####################################################
            day = []
            dayday = []
            for i in bab_day: 
                day.append(i.text)
            
            for num in range(1,6):
                dayday.append(day[num]) # 날짜 크롤링 완료

            #####################################################
            #                메뉴 크롤링 시작                    #
            #####################################################

            menu_menu = []
            tds_list = []
            for j in bab_menu:
                menu = j.select('td')
                tds_list.append(menu)
            
            backban = []
            for j in tds_list[3]:
                mm = str(j)
                num2 = mm.split('<br/>')
                
                for hh in num2:
                    real_menu = hh.replace("<td>", "")
                    my_menu = real_menu.replace("</td>", "")
                    
                    menu_menu.append(my_menu)
                
                backban.append(menu_menu)
                menu_menu = []

            #print(backban) # 메뉴 크롤링 완료

            for bab in range(5):
                file.write('{0},'.format(dayday[bab]))

            file.write("\n")

            for p in range(7):
                for q in range (5):
                    try:
                        file.write("{0},".format(backban[q][p]))
                    except:
                        pass
                    
                file.write("\n")
                
name = Football('https://www.kangwon.ac.kr/www/selecttnCafMenuListWU.do?key=223&sc1=SC20&sc2=SC')
name.search()
