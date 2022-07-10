# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# //*[@id="textblock_233905"]/div/div/p/span[1]
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

import csv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


def getarticles(url):
    browser = webdriver.Firefox()
    browser.get(url)
    listOfLinks = browser.find_elements(by=By.XPATH, value="//a[@href]")
    articles = []

    for link in listOfLinks:

            if link.get_attribute("href").__contains__("magazine/brand-eins-wirtschaftsmagazin"):
                if link.get_attribute("href").__contains__("magazine/brand-eins-wirtschaftsmagazin/2020/wie-wollen-wir-leben/der-richter-soll-die-kinder-nur-ganz-selten-schlagen"):
                    continue  #first article is skipped because of a paywall
                articles.append(link.get_attribute("href"))
    print(articles)
    return articles


            #/html/body/div[2]/main/section[2]/div/div


def gettext(articles):
    browser = webdriver.Firefox()
    text = [""] * len(articles)
    textindex = 0
    for article in articles:
        browser.get(article)
        temp = 1
        for i in range(20):
            #print(temp)
            try:
                if browser.find_element(by=By.XPATH, value="/html/body/div[2]/main/section[" + str(temp) + "]/div/div").text.__contains__("📫"):
                    break
            except:
               break
            #print(browser.find_element(by=By.XPATH, value="/html/body/div[2]/main/section[" + str(temp) + "]/div/div").text)
            text[textindex] = text[textindex] + (browser.find_element(by=By.XPATH, value="/html/body/div[2]/main/section[" + str(temp) + "]/div/div").text)
            print((browser.find_element(by=By.XPATH, value="/html/body/div[2]/main/section[" + str(temp) + "]/div/div").value_of_css_property('color')))
            temp += 1


        textindex += 1

        #print(browser.find_element(by=By.XPATH, value="/html/body/div[2]/main").text)
    return text

def file(text):
    filetest = open("testFile.txt", "w+", encoding="utf-8")

    temp = 1
    for t in text:
        #print(temp)
        filetest.write(t)
        filetest.write("\n\n\n\n\n ")
        temp += 1

    filetest.close()

def ptest(url):
    browser = webdriver.Firefox()
    browser.get(url)
    listofp = browser.find_elements(by=By.TAG_NAME, value='p')
    counter = 0
    line = ["", "", url]
    for p in listofp:
        if p.text.__contains__('Text:'):
            continue
        if p.text.__contains__('Lust auf mehr') or p.text.__contains__('Mehr zum Thema'):
            break
        print(counter)
        line[counter] = p.text
        #print(tags[counter])
        #print(p.text)
        print("line: " + "counter: " + str(counter) + " " + line[counter])
        print('\n\n')
        if counter == 1:
            writer.writerow(line)
        counter = (counter + 1) % 2





    #print(browser.find_element(by=By.XPATH, value=listOfLinks).text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://www.brandeins.de/themen/rubriken/leichte-sprache'
    ##path = '/html/body/div[2]/main/section[2]/div/div/p'
    arts = getarticles(url)
    #txt = gettext(arts)
    #file(txt)
    csvcat = ['complex', 'simple', 'source']
    f =  open('brandeins.csv', 'w', encoding='UTF8')
    writer = csv.writer(f)
    writer.writerow(csvcat)

    for a in arts:
        ptest(a)

    #ptest('https://www.brandeins.de/magazine/brand-eins-wirtschaftsmagazin/2020/leistung/man-darf-auch-nicht-so-tun-als-waere-es-ein-milch-erzeugnis')


