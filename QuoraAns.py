from selenium import webdriver
import pdfcrowd
from selenium.webdriver.common.keys import Keys
import os

chromedriver = "" # Chrome Driver Path
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get("http://www.quora.com/How-many-times-can-you-interview-with-Google-1") #Quora Link to questions

body = browser.find_element_by_tag_name("body")

#Get total answers for the question"
total_answers = str(browser.find_element_by_class_name("answer_count").text.split(" ")[0])
print "Total answers : ", total_answers

#Load all the answers first.
body.send_keys(Keys.END)

html = browser.page_source

urls =  ["http://www.quora.com/How-many-times-can-you-interview-with-Google-1","https://www.quora.com/What-are-the-best-Python-scripts-youve-ever-written"]
url = urls[0]

#PDF Crowd API Credentials: With Free account You get only 100 Tokens free
client = pdfcrowd.Client("", "")
file_name = url.split('/')[-1]+'.pdf'
output_file = open(file_name,'wb')
print "Converting to pdf..."
client.enableJavaScript(False)
pdf = client.convertHtml(html,output_file)
output_file.close()
#PDF file is created
print "File ", file_name, "created"
browser.close()
