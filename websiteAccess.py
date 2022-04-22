import requests
from lxml import etree
from bs4 import BeautifulSoup


def getMontleyFool():

    articleHeaders = []
    while len(articleHeaders) == 0:
        url = "https://www.fool.com/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        ul = soup.findAll('ul')

        for ulTag in ul:
            for liTag in ulTag.find_all('li', {"class": "font-medium mb-16px text-md"}):
                articleHeaders.append(liTag.text)

    return articleHeaders


def fromListToOpenAIReadable(list):
    output = ""
    for i in range(len(list)):
        input = list[i]
        output += "\n" + str(i+1) + ". \"" + input + "\""
    return output
