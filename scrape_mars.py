# Imports
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    #print("Scrape all was reached")
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path, headless=False)

    # Get info from news page
    news_title, news_paragraph = scrape_news(browser)

    # Build dictionary from scraped information
    marsData = {
        "newsTitle": news_title,
        "newsParagraph": news_paragraph
    }

    # Stops webdriver
    browser.quit()

    return marsData

def scrape_news(browser):
    # Visit news site
    # With the wait_time
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert browser html to soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Display current title content
    slide_elem = news_soup.select_one('div.list_text')
    news_title = slide_elem.find('div', class_='content_title').get_text()

    # Uses parent element to find paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    # Returns title and paragraph
    return news_title, news_p

if __name__ == "__main__":
    print(scrape_all())