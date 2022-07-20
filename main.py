# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import webbrowser

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# //*[@id="textblock_233905"]/div/div/p/span[1]
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

import csv

# if set to true, console output is printed
test = True


# logging function for testing
def log(text):
    if test:
        print(text)


def getarticles(url):
    browser.get(url)  # opens a firefox window and scrapes all links into >listoflinks<
    listoflinks = browser.find_elements(by=By.XPATH, value="//a[@href]")
    articles = []

    # we only want links of articles and not of the shop for example
    for link in listoflinks:
        if link.get_attribute("href").__contains__(
                "magazine/brand-eins-wirtschaftsmagazin"):  # all articles contain this part of the url
            if link.get_attribute("href").__contains__(
                    "magazine/brand-eins-wirtschaftsmagazin/2020/wie-wollen-wir-leben/der-richter-soll-die-kinder-nur-ganz-selten-schlagen"):
                continue  # first article is skipped because of a paywall
            else:
                articles.append(link.get_attribute("href"))  # we only want the href part of the web element
    log(articles)
    return articles

    # /html/body/div[2]/main/section[2]/div/div


# is used to get the complete plain text from each article, is not used for the scraping algorithm
def gettext(articles):
    text = [""] * len(articles)
    textindex = 0
    for article in articles:
        browser.get(article)
        temp = 1
        for i in range(20):
            # log(temp)
            try:
                if browser.find_element(by=By.XPATH, value="/html/body/div[2]/main/section[" + str(
                        temp) + "]/div/div").text.__contains__("📫"):
                    break
            except:
                break
            # log(browser.find_element(by=By.XPATH, value="/html/body/div[2]/main/section[" + str(temp) + "]/div/div").text)
            text[textindex] = text[textindex] + (browser.find_element(by=By.XPATH,
                                                                      value="/html/body/div[2]/main/section[" + str(
                                                                          temp) + "]/div/div").text)
            log((browser.find_element(by=By.XPATH, value="/html/body/div[2]/main/section[" + str(
                temp) + "]/div/div").value_of_css_property('color')))
            temp += 1

        textindex += 1

        # log(browser.find_element(by=By.XPATH, value="/html/body/div[2]/main").text)
    return text


# also not currently in use. used to create the file for storing the plain text
def file(text):
    filetest = open("testFile.txt", "w+", encoding="utf-8")
    temp = 1
    for t in text:
        # log(temp)
        filetest.write(t)
        filetest.write("\n\n\n\n\n ")
        temp += 1
    filetest.close()


# takes the url of an article as input and scrapes all paragraphs
def getparagraphs(url):
    browser.get(url)
    listofp = browser.find_elements(by=By.TAG_NAME, value='p')

    # each line of the csv is created in one iteration of the for loop, the url is appended after a pair of a complex
    # and a simple paragraph
    black = False
    red = False
    line = ["", "", url]
    for p in listofp:
        if p.text.__contains__('Text: ') or p.text.__contains__('Holger Fröhlich') or p.text.__contains__('Lust auf mehr') or p.text.__contains__('Mehr zum Thema') or p.text.__contains__('📫')  or p.text.__contains__("Abonnieren Sie unseren Newsletter") or p.text.__contains__("Ich habe die Informationen zum Datenschutz gelesen") or p.text.__contains__("Die Leichte Sprache nimmt den Inhalt"):
            continue
        #append black paragrahs to the first part of the csv line and write line if black and red are already written
        if checkcolor(p) == "rgb(0, 0, 0)":
            if black and red:
                writer.writerow(line)
                red = 0
                line = ["", "", url]

            black = True
            line[0] = line[0] + p.text
            #line[0].append(p.text)
        #append red paragraphs to the second part of the paragraph
        if checkcolor(p) == "rgb(255, 0, 0)":
            red = True
            line[1] = line[1] + p.text
            #line[1].append(p.text)
    if line[0] != "" and line[1] != "":
        writer.writerow(line)


#checks for child span elements and returns the color of the paragraph or the child
def checkcolor(p):
    try:
        return p.find_element(by=By.TAG_NAME, value="span").value_of_css_property("color")
    except NoSuchElementException:
        return p.value_of_css_property("color")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    brandeinsurl = 'https://www.brandeins.de/themen/rubriken/leichte-sprache'  # brand eins website
    browser = webdriver.Firefox()  # starts the browser
    # path = '/html/body/div[2]/main/section[2]/div/div/p'
    arts = getarticles(brandeinsurl)
    # txt = gettext(arts)
    # file(txt)
    csvcat = ['complex', 'simple', 'source']  # first line of the csv
    f = open('brandeins.csv', 'w', encoding='UTF8')  # creates or opens a new csv file and writes the first line
    writer = csv.writer(f)
    writer.writerow(csvcat)

    # loop over all articles and scrape paragraphs
    for a in arts:
        getparagraphs(a)
