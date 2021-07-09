
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import smtplib, ssl
import sys
import re


news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")

allnews = ''
file1 = open("myfile.txt","w") 

for news in news_list:
	title=(news.title.text)
	link=(news.link.text)
	file1.write(title)
	file1.write("\n")
	file1.write(link)
	file1.write("\n")
	file1.write("\n")
	allnews += title
	allnews += link
	
file1.close()

file = open("myfile.txt", "r")

allnews1 = file.read()
allnews = re.sub(u"(\u2018|\u2019|\xed|\u2013|\u2014|\xf6)", "'", allnews1)
#If there is any encoding problems simply add the text giving the problem like those already entered above


Body = """\
Subject : Daily News Report

Your top news stories of the day:

""" + allnews + """\

Sincerely,
Your Computer"""



sendto='johnnyapple@gmail.com'
sendfrom='johnnyCarrot@gmail.com'
password='Carrot123'
server=smtplib.SMTP_SSL('smtp.gmail.com:465')

#Just enter the email you want to send to and the gmail you want to login and send from. 
#Make sure that you enable IMAP in gmail settings.
#MUST BE A GMAIL ACC OR CHANGE THE SMTP SERVER AND PORT TO YOUR EMAIL PROVIDERS


server.login(sendfrom,password)

server.sendmail(sendfrom, sendto, Body)

server.quit()
file.close()
delete = open("myfile.txt", "r+")
delete.truncate(0)
delete.close()
print ("done")

#This code works great along side the windows task scheduler to recieve emails right when you wake up!