from helium import *
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import os
#from dotenv import load_dotenv

#load_dotenv()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
        

def analyze_reviews_with_gemini(text,model):
    prompt = f"""
    You are analyzing a list of reviews for an app on playstore. The list contains both negetive and positive reviews.
    After analyzing give the pros and cons of the app pointwise.
    Sample Output -
    Pros:
    1.
    2.
    Cons:
    1.
    2.
    """
    
    response = model.generate_content([prompt, text])
    output = response.text.strip()
    return output



def scrape_reviews(link):
    browser=start_chrome(link,headless=True,options=chrome_options)
    click("See all reviews")
    click("Star rating")
    click('1-star')

    data=browser.page_source
    soup = BeautifulSoup(data, 'html.parser')
    reviews = soup.find_all('div', class_='h3YV2d')
    reviews=[review.get_text(strip=True) for review in reviews]

    kill_browser()

    return str(reviews)


def process_link(link,model):
    reviews=scrape_reviews(link)
    analysis=analyze_reviews_with_gemini(reviews,model)
    return analysis



    





