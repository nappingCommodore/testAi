from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
browser = webdriver.Chrome(executable_path=r'/opt/chromedriver', chrome_options=chrome_options)
browser.get('http://localhost:8000')

assert 'Django' in browser.title