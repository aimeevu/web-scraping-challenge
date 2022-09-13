# Imports
from splinter import Browser
from bs4 import BeautifulSoup as soup
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    #print("Scrape all was reached")
    path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome',**path, headless=False)

    # Get info from news page
    newsTitle, newsParagraph = scrapeNews(browser)

    # Dictionary of scraped information
    marsData = {
        "newsTitle": newsTitle,
        "newsParagraph": newsParagraph,
        "featuredImage": scrapeFeatureImg(browser),
        "facts": scrapeFactsPage(browser),
        "hemispheres": scrapeHemispheres(browser),
        "lastUpdated": dt.datetime.now()
    }

    # Stops webdriver
    browser.quit()

    return marsData

# Scrapes news pages
def scrapeNews(browser):
    # Visit news site
    # With the wait_time
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert browser html to soup object
    html = browser.html
    newsSoup = soup(html, 'html.parser')

    # Display current title content
    slideElem = newsSoup.select_one('div.list_text')
    newsTitle = slideElem.find('div', class_='content_title').get_text()

    # Uses parent element to find paragraph text
    newsP = slideElem.find('div', class_='article_teaser_body').get_text()

    # Returns title and paragraph
    return newsTitle, newsP

# Scrapes for Feature Image
def scrapeFeatureImg(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    fullImageLink = browser.find_by_tag('button')[1]
    fullImageLink.click()

    # Parse html with soup
    html = browser.html
    imgSoup = soup(html, 'html.parser')

    # Find relative image url
    imgUrlRel = imgSoup.find('img', class_='fancybox-image').get('src')

    # Store image url as absolute url to use later
    imgUrl = f'https://spaceimages-mars.com/{imgUrlRel}'

    # Return image URL
    return imgUrl

# Scrape Facts Page
def scrapeFactsPage(browser):
    # Visit URL
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    # Parse through HTML with soup
    html = browser.html
    factsSoup = soup(html, 'html.parser')

    # Find facts location
    factsLocation = factsSoup.find('div', class_="diagram mt-4")
    factsTable = factsLocation.find('table') # Grabs table html code

    # Empty string
    facts = ""

    # Adds text to empty string
    facts += str(factsTable)

    return facts

# Scrap Hemispheres Page
def scrapeHemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # List to hold images and titles
    hemisphereImgUrl = []

    for i in range(4):
        hemisphereInfo = {}
    
        # Find element on each loop
        browser.find_by_css('a.product-item img')[i].click()
        
        # Find sample image anchor tag and extract href
        sample = browser.links.find_by_text('Sample').first
        hemisphereInfo['img_url'] = sample['href']
        
        # Get title
        hemisphereInfo['title'] = browser.find_by_css('h2.title').text
        
        # Append object to list
        hemisphereImgUrl.append(hemisphereInfo)
        
        # Navigate back
        browser.back()
    
    return hemisphereImgUrl

# Sets up flask app
if __name__ == "__main__":
    print(scrape_all())