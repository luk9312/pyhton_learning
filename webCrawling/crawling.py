from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json

url = 'https://kazemai.github.io/fgo-vz/servant.html'

def writeToJSONFile(path,fileName, data):
    filePathNameWExt = './'+ path + fileName + '.json'
    with open(filePathNameWExt, 'w', encoding="utf-8") as fp:
      json.dump(data, fp,ensure_ascii=False, indent=2)

# firefox headless
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()

driver = webdriver.Firefox(firefox_options=fireFoxOptions)

driver.get(url)
pageSource = driver.page_source

soup = BeautifulSoup(pageSource, 'lxml')  # 解析器
result = soup.find_all("tr", class_="svtList")

# trun data into JSON format
data = []
for count, item in enumerate(result, start=1):
  dataObj = {}
  nameList = item.contents[3].get_text("|").split("|")
  dataObj["cName"] = nameList[1].strip()
  dataObj["jName"] = nameList[0].strip()
  dataObj["url"] = "https://kazemai.github.io/fgo-vz/"+item.contents[3].a.get("href")
  dataObj["ui"] = item.contents[1].get_text()
  dataObj["rare"] = len(item.contents[2].get_text())
  dataObj["class"] = item.contents[4].img.get("title")
  dataObj["baseHp"] = item.contents[5].get_text()
  dataObj["maxHp"] = item.contents[6].get_text()
  dataObj["baseAtt"] = item.contents[7].get_text()
  dataObj["maxAtt"] = item.contents[8].get_text()
  dataObj["cost"] = item.contents[11].get_text()
  data.append(dataObj)

writeToJSONFile('webCrawling/','servent',data)


driver.quit()