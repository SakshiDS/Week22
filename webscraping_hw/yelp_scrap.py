#!/usr/bin/env python

# Yelp search function
def yelp_scrap_50(zip_code):


    from bs4 import BeautifulSoup as bs
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd
    import numpy as np
    
    # Data I want to scrape for the restaurants
    restaurant_name = []
    hours = []
    pricing = []
    rating = []
    no_of_reviews = []
    
    # url updated with the zip code passed
    url=f'https://www.yelp.com/search?find_desc=Restaurants&find_loc={zip_code}'

    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True) # True to keep browser closed in function
    for page in range(0,50,10):
        
        pg_url = url + f'&start={page}'
    
        browser.visit(pg_url)
        
        soup = bs(browser.html, 'html.parser')
        #rint(pg_url)
        
        try:
            # Restaurant Name
            name_divs = soup.find_all("div", class_="businessName__09f24__EYSZE display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY")
            for n in name_divs:
                name = n.find('a', class_='css-1422juy').text
                restaurant_name.append(name)
            
           #print(len(restaurant_name))
            
            # Hours of Operation
            hour_divs = soup.find_all("div", class_="container__09f24__mpR8_ hoverable__09f24__wQ_on margin-t3__09f24__riq4X margin-b3__09f24__l9v5d padding-t3__09f24__TMrIW padding-r3__09f24__eaF7p padding-b3__09f24__S8R2d padding-l3__09f24__IOjKY border--top__09f24__exYYb border--right__09f24__X7Tln border--bottom__09f24___mg5X border--left__09f24__DMOkM border-color--default__09f24__NPAKY")
            for h in hour_divs:
                text = h.find('p', class_='css-1sufhje')
                if text is None:
                    text="Not Available"
                    hours.append(text) 
                else:
                    text = h.find('p', class_='css-1sufhje').text
                    hours.append(text)
            
           #print(len(hours))
            
            # Pricing Points    
            para = soup.find_all('p', class_='css-1gfe39a')
            for span in para:
                price = span.find('span', class_='css-1e4fdj9').text
                pricing.append(price)
            
           #print(len(pricing))
            
            # Restaurant rating
            rating_divs = soup.find_all("div", class_="attribute__09f24__hqUj7 display--inline-block__09f24__fEDiJ margin-r1__09f24__rN_ga border-color--default__09f24__NPAKY")
            for d in rating_divs:
                for x in d:
                    stars = x.div['aria-label']
                    rating.append(stars)
            
           #print(len(rating))
            
            # Reviews
            review_divs = soup.find_all("div", class_="attribute__09f24__hqUj7 display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY")
            for r in review_divs:
                reviews = r.find('span', class_="reviewCount__09f24__tnBk4 css-1e4fdj9").text
                no_of_reviews.append(reviews)
            
           #print(len(no_of_reviews))            
            


        except Exception as e:
            print(e)
   
    # Parsing data into dictionary
    yelp_50_dic = {'Rank#':np.arange(1,51,1),
    'Retaurant Name':restaurant_name, 
    'Hours(Open/Close)':hours, 
    'Pricing Point':pricing, 
    'Rating':rating, 
    'No. of Reviews':no_of_reviews}

    yelp_50_df = pd.DataFrame.from_dict(yelp_50_dic)
    yelp_50_df.set_index("Rank#",inplace=True)
    return yelp_50_df