from helium import *
import time
from bs4 import BeautifulSoup
from langchain.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

link="https://play.google.com/store/apps/details?id=com.nflystudio.InfiniteStaircase&pcampaignid=merch_published_cluster_promotion_battlestar_browse_all_games&hl=en"

browser=start_chrome(link,headless=True)


click("See all reviews")
click("Star rating")
click('1-star')

data=browser.page_source
soup = BeautifulSoup(data, 'html.parser')
reviews = soup.find_all('div', class_='h3YV2d')
reviews=[review.get_text(strip=True) for review in reviews]

time.sleep(5)

kill_browser()

genai.configure(api_key=os.environ["GOOGLE_API"])
gemini_model = genai.GenerativeModel(model_name="gemini-1.5-flash")

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
    output = response.text.strip().split('\n')
    return output

res=analyze_reviews_with_gemini(str(reviews),gemini_model)
print(res)

