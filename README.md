# web-scraping-challenge
## GA Tech Data Science and Analytics Boot Camp Module 12
### Description
<p>This module utilizes new concepts, such as web scraping with BeautifulSoup and MongoDB, and former concepts like HTML, Bootstrap, and Flask to develop an application that will scrape data from four sites and display the data through a Flask application.</p>

<h1>Part 1: Scraping</h1>
<p>This module first starts with a Python Jupyter notebook in order to utilize BeautifulSoup, Pandas, and Requests/Splinter to scrape for data.</p>

<p>The four sites that data is scraped from include:</p>

* <a href="https://redplanetscience.com/">NASA Mars News</a>
    - Collect the latest News Title and Paragraph Text

<img src="MarsNews.png">

* <a href="https://spaceimages-mars.com/">JPL Marks Space Images-Featured Image</a>
    - Save complete URL string for the featured image

<img src="FeaturedImageURL.png">

* <a href="https://galaxyfacts-mars.com/">Mars Facts</a>
    - Collect table containing facts about Mars

<img src="MarsFacts.png">

* <a href="https://marshemispheres.com/">Mars Hemispheres</a>
    - Save image URLs for each hemisphere, including the title

<img src="HemisphereList.png">

<p>The code for the scraping script can be found <a href="MissionToMars.ipynb">here</a>.</p>

<h1>Part 2: MongoDB and Flask Application</h1>
<p>Once the script works in Jupyter, it is then copied into a Python file in order for the script to be used by the Flask application. This code can be found in <a href="scrape_mars.py">scrape_mars.py</a></p>

<p>The Flask application will then call to the scraping script in order to load and display the data in the browser. At the same time, the data is loaded into a MongoDB database named marsDataDB, collection marsData.</p>

<p>Additionally, an HTML template that utilizes Bootstrap is called into the Flask application in order to properly display the data.</p>

<p>The code for the Flask application can be found <a href="app.py">here</a>, and the HTML template can be found <a href="templates/index.html">here</a>.</p>

<p>Here is the final application:</p>
<img src="FinalApplication_1">
<img src="FinalApplication_2">

### Submission Requirements
* Jupyter notebook with scraping code
* Screenshots of final application
* Flask App with HTML template