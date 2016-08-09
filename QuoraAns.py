from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pdfcrowd
from selenium.webdriver.common.keys import Keys
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

chromedriver = "C:\\Users\\sivard2\\Documents\\chromedriver_win32\\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get("http://www.quora.com/How-many-times-can-you-interview-with-Google-1")

body = browser.find_element_by_tag_name("body")

#Get total answers for the question"
#for example: 116 Answers would return 116
total_answers = str(browser.find_element_by_class_name("answer_count").text.split(" ")[0])
print "Total answers : ", total_answers

#Load all the answers first.
body.send_keys(Keys.END)

html = browser.page_source

#q = str(raw_input("http://www.quora.com/How-many-times-can-you-interview-with-Google-1"))+"?ref=1"
urls =  ["http://www.quora.com/How-many-times-can-you-interview-with-Google-1","https://www.quora.com/What-are-the-best-Python-scripts-youve-ever-written"]
url = urls[0]

client = pdfcrowd.Client("Diwahar", "da26172b7e048667fb981af752173393")
file_name = url.split('/')[-1]+'.pdf'
output_file = open(file_name,'wb')
print "Converting to pdf..."
client.enableJavaScript(False)
pdf = client.convertHtml(html,output_file)
output_file.close()
print "File ", file_name, "created"
browser.close()
#justchecking