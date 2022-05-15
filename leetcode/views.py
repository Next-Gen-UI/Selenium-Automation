# from tkinter.messagebox import YES
from webdriver_manager.chrome import ChromeDriverManager
from django.http import HttpResponse
from django.shortcuts import render
import time
from xml.etree.ElementTree import tostring
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
from requests.structures import CaseInsensitiveDict


# index = 1


def findNumberByIndex(index):
    if(index < 10):
        return "000"+str(index)
    elif(index < 100):
        return "00"+str(index)
    elif(index < 1000):
        return "0"+str(index)
    else:
        return str(index)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create your views here.
def index(response):
    

#     driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

    driver.get("https://github.com/login")

    driver.maximize_window()

    time.sleep(2)
    driver.get("https://github.com/Next-Gen-UI/Code-Dynamics/tree/main/Leetcode")

    codes = []

    # hERE lOOP sTART
    # i =  3

    for i in range(2, 101):

        myUrl = "(//div[@role='rowheader'])["+str(i)+"]"
        resulti = driver.find_element_by_xpath(myUrl)
        val = resulti.text

        driver.get("https://github.com/Next-Gen-UI/Code-Dynamics/tree/main/Leetcode/"+val+"/"+findNumberByIndex(i-1)+".py")

        time.sleep(1)

        driver.find_element_by_css_selector("#raw-url").click()
        time.sleep(1)
        pythonCode=driver.find_element_by_xpath("/html/body/pre").text


        # CPP Code get
        driver.get("https://github.com/Next-Gen-UI/Code-Dynamics/tree/main/Leetcode/"+val+"/"+findNumberByIndex(i-1)+".cpp")

        time.sleep(1)

        driver.find_element_by_css_selector("#raw-url").click()
        time.sleep(1)
        cppCode=driver.find_element_by_xpath("/html/body/pre").text


        # Java Code
        # CPP Code get
        driver.get(
            "https://github.com/Next-Gen-UI/Code-Dynamics/tree/main/Leetcode/"+val+"/"+findNumberByIndex(i-1)+".java")

        time.sleep(1)

        driver.find_element_by_css_selector("#raw-url").click()
        time.sleep(1)
        javaCode=driver.find_element_by_xpath("/html/body/pre").text

        # val = resulti.text
        json3={
            'title': val,
            'cpp': cppCode,
            "java": javaCode,
            "python": pythonCode,

        }

        y = json.dumps(json3)
        codes.append(y)
        # print("Result :- ", myRes)
        driver.get(
            "https://github.com/Next-Gen-UI/Code-Dynamics/tree/main/Leetcode")

    # https://codedynamics.herokuapp.com/api/leetcode

    # Post Request

    # Thr end of loop

    resJson={
        "data": {
            "questions": codes
        }
    }

    y1 = json.dumps(resJson)
    print(y1)
    # Put request
    # requests.put(
        # 'https://codedynamics.herokuapp.com/api/leetcode', data=resJson)

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    r = requests.put(
        "https://codedynamics.herokuapp.com/api/leetcode", headers = headers, data = y1)
    print(r, "Response is:- ")
    print(r.content, "Content is:- ")



    return HttpResponse(y1)


def leetcode(response):
    return HttpResponse("This is Subset of Services Page Bro Let's Move One Step Ahead")
