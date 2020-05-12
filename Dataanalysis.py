print("This program tells you how many times a word has been repeated in a website.we have taken the website 'altoro mutual'.we can do this for any website.This functions by getting the input from the user.")
import bs4 as bs
import urllib.request
sauce=urllib.request.urlopen('http://demo.testfire.net/').read()
soup=bs.BeautifulSoup(sauce,'lxml')
chars =str(input("enter the string you want to search"))
check_string =soup.get_text()
count = check_string.count(chars)
if count>=1:
    print("The output is",chars, count)
else:
    print("the given string is not found in this website,try another word")



    
