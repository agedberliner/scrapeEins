# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# //*[@id="textblock_233905"]/div/div/p/span[1]
from selenium.webdriver.common.by import By


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


def click(url, path):
    browser = webdriver.ChromiumEdge()
    browser.get(url)
    listOfLinks = browser.find_elements(by=By.XPATH, value="//a[@href]")


    for link in listOfLinks:
            print(link.get_attribute("href"))
            if link.get_attribute("href").__contains__("magazine/brand-eins-wirtschaftsmagazin"):
                if link.get_attribute("href").__contains__("magazine/brand-eins-wirtschaftsmagazin/2020/wie-wollen-wir-leben/der-richter-soll-die-kinder-nur-ganz-selten-schlagen"):
                    continue
                browser.get(link.get_attribute("href"))

                temp = 1
                for i in range(5):

                    print(browser.find_element(by=By.XPATH, value="/html/body/div[2]/main/section[" + str(temp) + "]/div/div").text)
                    temp += 1
                #print(browser.find_element(by=By.XPATH, value="/html/body/div[2]/main").text)

            #/html/body/div[2]/main/section[2]/div/div







    #print(browser.find_element(by=By.XPATH, value=listOfLinks).text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://www.brandeins.de/themen/rubriken/leichte-sprache'
    path = '/html/body/div[2]/main/section[2]/div/div/p'
    click(url, path)


