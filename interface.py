from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from subprocess import call
from time import sleep
from bs4 import BeautifulSoup
import requests
from os import system, name

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  
def start(user1,pass1,Artist,Song_name):
	try:

	    #global user1,pass1,Artist,Song_name
	    driver = webdriver.Chrome('C://Users/dell/chromedriver.exe')
	    driver.get('https://www.genius.com')

	    login_prompt = driver.find_element_by_xpath('//a[@href="/login"]')
	    login_prompt.click()

	    username = driver.find_element_by_name('login')
	    username.send_keys(user1)

	    password = driver.find_element_by_name('password')
	    password.send_keys(pass1)

	    sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
	    y = sign_in_button.click()
	    sleep(1.3)

	    actual_error = driver.find_element_by_xpath('.//*[@class="form_message form_message--error"]')
	    expected_error = 'INVALID USERNAME OR PASSWORD'
	    assert actual_error.text != expected_error
	    sleep(1.3)


	    
	except IndexError:
	    messagebox.showinfo("Error!", "No Results were found")

	except NoSuchElementException:
	    driver.get('https://www.google.com')

	    search_query = driver.find_element_by_name('q')
	    link = 'site:genius.com/ AND '+ Artist +' AND ' +Song_name

	    search_query.send_keys(link)
	    search_query.send_keys(Keys.RETURN)

	    lyrics_urls = driver.find_elements_by_tag_name('h3')
	    lyrics_urls[0].click()
	    Edit_button = driver.find_element_by_xpath('//*[@class="square_button"]')
	    Edit_button.click()

	    Song = driver.find_element_by_xpath('.//*[@class="header_with_cover_art-primary_info-title"]').text
	    Artist_name = driver.find_element_by_xpath('.//*[@class="header_with_cover_art-primary_info-primary_artist"]').text

	    Song = '\n\t\t\t\t\t_______________SongName- ' + Song +'______________________\n\n'
	    Artist_name = '\t\t\t\t\t_______________Artist_name- ' + Artist_name+'_______________________\n\n'

	    page = requests.get(driver.current_url)
	    clear()
	    html = BeautifulSoup(page.text, "html.parser")
	    lyrics = html.find("div", class_="lyrics").get_text()
	    f = open('C://Users/dell/Desktop/Lyrics.txt','w',encoding='utf-8')
	    f.write(Song)
	    f.write(Artist_name)
	    f.write('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
	    f.write(lyrics)
	    f.write('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
	    f.close()

	except AssertionError:
		messagebox.showinfo("Error!", "Invalid Username or Password")
		clear()
		driver.quit()

   
	driver.quit()
	clear()
	root.destroy()

root = Tk()
root.title('Songs Lyrics Scrapper')
pic = PhotoImage(file="background.png")
background_label = Label(image=pic)
background_label.pack()
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = pic

default = root.cget('bg')
label=Label(root,text="Lyrics Scrapper",font=("Times",30,"bold"),fg='cyan3',bg='grey20')
label.place(x=500,y=30)
label1=Label(root,text="User Name (on Genius.com)",font=("Times",14),fg="cyan3",bg="grey20",)
label1.place(x=200,y=150)
entry_1= Entry(root,bg="grey25",bd=4)
entry_1.place(x=460,y=150)
label2=Label(root,text="Password (on Genius.com)",font=("Times",14),fg="cyan3",bg="grey20")
label2.place(x=650,y=150)
entry_2= Entry(root,bg="grey25",bd=4,show="*")
entry_2.place(x=900,y=150)
label3=Label(root,text="Artist Name",font=("Times",14),fg="cyan3",bg="grey20",)
label3.place(x=320,y=230)
entry_3= Entry(root,bg="grey25",bd=4)
entry_3.place(x=460,y=230)
label4=Label(root,text="Song Name",font=("Times",14),fg="cyan3",bg="grey20",)
label4.place(x=770,y=230)
entry_4= Entry(root,bg="grey25",bd=4)
entry_4.place(x=900,y=230)
w = Button(root,text="Submit",width=10,height=2,bd=4,font=("Times",10,"bold"),bg="cyan3"
	,command=lambda: start(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get()))
w.place(x=645,y=450)



root.mainloop()