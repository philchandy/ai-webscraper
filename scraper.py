from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def getHTMLElements(url):

    chrome_options = Options()
    chrome_options.add_argument('--headless')

    chrome_driver_path = './chromedriver.exe'

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    driver.get(url)

    elements = driver.find_elements(By.XPATH, '//*')

    all_elements = driver.page_source

    driver.quit()

    return all_elements

def getBodyContent(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content) 
    return ""

def cleanBodyContent(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def splitDOMContent(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]

if __name__ == "__main__":
    url = "https://google.com"
    elements = getHTMLElements(url)

    body = (getBodyContent(elements))
    print(cleanBodyContent(body))