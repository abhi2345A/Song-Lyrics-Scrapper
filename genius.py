from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from bs4 import BeautifulSoup
import requests

Artist = 'Alan Walker'
Song_name = 'Darkside'

try:

    driver = webdriver.Chrome('C://Users/dell/chromedriver.exe')
    driver.get('https://www.genius.com')

    login_prompt = driver.find_element_by_xpath('//a[@href="/login"]')
    login_prompt.click()

    username = driver.find_element_by_id('user_session_login')
    username.send_keys('abhijeet2345')

    password = driver.find_element_by_id('user_session_password')
    password.send_keys('abhijeet2345')



    sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
    sign_in_button.click()
    sleep(1.3)
    actual_error = driver.find_element_by_xpath('.//*[@class="form_message form_message--error"]')
    expected_error = 'INVALID USERNAME OR PASSWORD'
    assert actual_error.text != expected_error
    sleep(1.3)
    

except IndexError:
    print('No Results were found')

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
	print('----------SORRY SENORITA----------------')
	driver.quit()


driver.quit()