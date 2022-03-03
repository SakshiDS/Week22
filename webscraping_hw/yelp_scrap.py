#!/usr/bin/env python

# Yelp search function
def yelp_search():

    # Load libraries
    from bs4 import BeautifulSoup as bs
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd
    
    # Empty lists to append
    names_list = []
    location_list = []
    review_list = []
    rating_list = []
    comments_list = []
    
    # Enter your zip code into the url
    my_zip = 63017
    # url with zip appended
    url=f'https://www.yelp.com/search?find_desc=Restaurants&find_loc={my_zip}'

    # executable path for a chrome driver
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True) # True to keep browser closed in function
    
    # iterate through the browser end points
    for next_ in range(10,60,10):
        # get url
        url_next = url + f'&start={next_}'

        # Visit the yelp url in our browser
        browser.visit(url_next)
        # Parse url
        soup = bs(browser.html, 'html.parser')
        
        try:
            # Retaurant names
            divs = soup.find_all("div", class_="businessName__09f24__EYSZE display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY")
            for a in divs:
                names = a.find('a', class_='css-1422juy').text
                names_list.append(names)

            # Location 
            ps = soup.find_all('p', class_='css-1gfe39a')
            for span in ps:
                neighborhood = span.find('span', class_='css-1e4fdj9').text
                location_list.append(neighborhood)

            # Reviews
            revs = soup.find_all("div", class_="attribute__09f24__hqUj7 display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY")
            for rev in revs:
                reviews = rev.find('span', class_="reviewCount__09f24__tnBk4 css-1e4fdj9").text
                review_list.append(reviews)

            # Restaurant rating
            star_block = soup.find_all("div", class_="attribute__09f24__hqUj7 display--inline-block__09f24__fEDiJ margin-r1__09f24__rN_ga border-color--default__09f24__NPAKY")
            for stars in star_block:
                for star in stars:
                    rating = star.div['aria-label']
                    rating_list.append(rating)

            # Comments
            div = soup.find_all("div", {"class": "display--inline-block__09f24__fEDiJ margin-t1__09f24__w96jn border-color--default__09f24__NPAKY"})
            for d in div:
                var = d.find('p', class_='css-1e4fdj9')
                if var is None:
                    var = 'Not available'
                    comments_list.append(var)
                else:
                    var = var = d.find('p', class_='css-1e4fdj9').text
                    comments_list.append(var) 

        except Exception as e:
            print(e)
    
    # Create Data frame; limit to 50 restaurants
    dictionary = {'Retaurant':names_list[0:50], 
    'Neighborhood':location_list[0:50], 
    'Total Reviews':review_list[0:50], 
    'Rating':rating_list[0:50], 
    'Comments':comments_list[0:50]}

    df = pd.DataFrame.from_dict(dictionary)
    return df   