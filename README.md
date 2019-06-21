# Song-Lyrics-Scrapper

The Given Project is a song lyrics scrapper tool created using BeautifulSoup ,Tkinter and Selenium webdriver.
This Project scrapes the song lyrics from the site genius.com

### Working 
* Install Python and pip in open windows powershell using python website

* Install Virtualenv by:
 ```
 pip install virtualenv
 
 ```
* open windows powershell and create a virtual environment using virtualenv :
```
   virtualenv venv 
```
* Keep all these files in the venv folder and move to scripts folder and activate virtual environment:

```
   1) cd Scripts
   2) .\activate
```
* Then Install Necessary packages like :

```
   BeautifulSoup - pip install BeautifulSoup (Used for Scraping)
   Selenium - pip install Selenium (Used for Navigation between Webpages)
   Tkinter - pip install Tkinter (Used for GUI)
   requests - pip install requests (Used for user requests on Webpages
```
* To run the project - Open powershell and command:
```
  python interface.py
```
* A GUI interface will be shown like this - 

![Screenshot (132)](https://user-images.githubusercontent.com/37475805/59906106-7d654380-9425-11e9-8a16-85f790088907.png)

* After that we will be logged in - 


![Screenshot (133)](https://user-images.githubusercontent.com/37475805/59906270-f1075080-9425-11e9-869d-5b611bf659b5.png)

* Then with the help of selenium we will be navigated to genius.com site and lyrics will be scraped using BeautifulSoup

![Screenshot (134)](https://user-images.githubusercontent.com/37475805/59906364-33309200-9426-11e9-9f98-58e9a3332026.png)

* The Scraped Lyrics will be stored in lyrics.txt file.
