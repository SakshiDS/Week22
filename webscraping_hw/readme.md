#### 1.	Create a python function to scrape Yelp data for 50 restaurants close to you OR Craigslist for the top 50 items of any topic interesting to you. Think about what data you want to scrape aside from the name and location. You must pick at least three other fields. You can use beautiful soup, selenium, scrapy, and/or splinter as possible.
The python function for scraping is uploaded as : https://github.com/SakshiDS/Week22/blob/main/webscraping_hw/yelp_scrap.py

#### 2.	Create a local API that calls your scrape function and stores the data when you call /scrape endpoint. The data you scrape should be viewable when you go to /all .
App for this functionality is coded in the file: https://github.com/SakshiDS/Week22/blob/main/webscraping_hw/yelp_flask.py

Screenshots of all endpoints - 
##### homepage
![image](https://user-images.githubusercontent.com/90784468/156541326-14fa0cac-3d6e-42cd-9b37-2b1fa2b374cd.png)

##### /scrape
At this end point the python function to scrape data in yelp_scrap.py is called and the data is saved as json file.

![image](https://user-images.githubusercontent.com/90784468/156541276-ac184fe2-b7b8-4dc3-83c6-167c2df0c967.png)

##### /all
On calling this end point the save json file with scraped data is loaded and passed to html file.

![image](https://user-images.githubusercontent.com/90784468/156541201-11fc8a47-9554-4971-93b7-93394fcc3288.png)

#### 3.	What is web scraping? Why is it helpful? What does it mean for your online presence? Refence the readings and DataCamp. 
* Web scraping is the process of collecting structured web data in an automated fashion. It’s also called web data extraction. Web data extraction is used by people and businesses who want to make use of the vast amount of publicly available web data to make smarter decisions.

* A data scraping tool can help automate the process of extracting information from websites, quickly and accurately. It can also make sure the data extracted is neatly organized, making it easier to analyze and use for other projects. 
* 
* In theory, we could manually cut and paste information from individual web pages into a spreadsheet or another document. But we’ll find this to be laborious, time-consuming, and error-prone if we’re trying to extract information from hundreds or thousands of pages. A web scraping tool automates the process, efficiently extracting the web data we need and formatting it in some kind of neatly-organized structure for storage and further processing.
