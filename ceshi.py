# -*-coding:utf-8-*-
# @Time    :2023/10/3014:19
# @Author  :liuxiaomeng
# @Email   :lxm@outlook.com
# @File    :ceshi.py
# @Software:PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
import HTMLTestRunnerNew
import ddt
from parse_csy import parse_csv
from parameterized import parameterized, param


#元素定位
class login():
    username=(By.ID,"inputUsername")
    password=(By.XPATH,'//*[@id="inputPassword"]')
    button=(By.XPATH,'/html/body/div[1]/form/button')
    remind=(By.XPATH,'/ html / body / div[1] / form / p')

class fabuhui():
    addbutton=(By.XPATH,'/html/body/div[1]/div[1]/div[2]/button')
    addname=(By.NAME,"name")
    address=(By.NAME,"address")
    addnumber=(By.XPATH,'//*[@id="id_limit"]')
    adddate=(By.XPATH,'//*[@id="id_start_time"]')
    addsubmit=(By.XPATH,'/html/body/div[1]/div[2]/form/div[7]/div/button')

class jiabin():
    addjiabin = (By.XPATH, '//*[@id="navbar"]/ul[1]/li[2]/a')
    addjiabinbutton=(By.XPATH,'/html/body/div[1]/div[1]/div[2]/button')
    addfabuhui=(By.XPATH,'//*[@id="id_event"]/option[2]')
    addphone=(By.NAME,"phone")
    addemail=(By.NAME,"email")
    addmingzi=(By.NAME,"realname")
    addtijiao=(By.XPATH,'/html/body/div[1]/div[2]/form/div[7]/div/button')







class BasePage():#初始化
    def __init__(self,driver):
        self.driver = driver

#元素操作层
class login_01(BasePage):
    def set_username(self,username):
        ele = self.driver.find_element(*login.Username)  # 解包
        ele.clear()
        ele.send_keys(username)
    def set_password(self,password):
        ele = self.driver.find_element(*login.Password)
        ele.clear()
        ele.send_keys(password)
    def set_button(self):
        ele = self.driver.find_element(*login.button)
        ele.clear()
    def set_remind(self):
        ele = self.driver.find_element(*login.remind)
        print(ele.text)

class fabuhui_01(BasePage):
    def add_button(self,):
        ele = self.driver.find_element(*fabuhui.addbutton)
        ele.clear()
    def add_name(self,addname):
        ele = self.driver.find_element(*fabuhui.addname)
        ele.clear()
        ele.send_keys(addname)
    def add_ress(self,address):
        ele = self.driver.find_element(*fabuhui.address)
        ele.clear()
        ele.send_keys(address)
    def add_number(self,addnumber):
        ele = self.driver.find_element(*fabuhui.addnumber)
        ele.clear()
        ele.send_keys(addnumber)
    def add_date(self,adddate):
        ele = self.driver.find_element(*fabuhui.adddate)
        ele.clear()
        ele.send_keys(adddate)
    def add_submit(self):
        ele=self.driver.find_element(*fabuhui.submitbtu)
        ele.click()

class jiabin_01(BasePage):
    def jb(self):
        ele=self.driver.find_element(*jiabin.addjiabin)
        ele.clear()
    def jbb(self):
        ele=self.driver.find_element(*jiabin.addjiabinbutton)
        ele.clear()
    def fbh(self):
        ele=self.driver.find_element(*jiabin.addfabuhui)
        ele.select_by_index(2)
    def phone(self,phone):
        ele=self.driver.find_element(*jiabin.addphone)
        ele.clear()
        ele.send_keys(phone)
    def email(self,email):
        ele=self.driver.find_element(*jiabin.addemail)
        ele.clear()
        ele.send_keys(email)
    def mz(self,mz):
        ele=self.driver.find_element(*jiabin.addmingzi)
        ele.clear()
        ele.send_keys(mz)
    def tj(self,tj):
        ele=self.driver.find_element(*jiabin.addtijiao)
        ele.clear()

@ddt.ddt
class yongli(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Edge()
        self.driver.get("http://150.109.156.47:8000/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)






