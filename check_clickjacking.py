# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import re

# def check_clickjacking(url):
#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(options=options)

#     try:
#         driver.get(url)
#         html_content = driver.page_source

#         html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)

#         x_frame_options = "X-Frame-Options" in html_content
#         csp = "Content-Security-Policy" in html_content
#         vulnerabilities = []

#         if not x_frame_options:
#             vulnerabilities.append("Missing X-Frame-Options header")
#         if not csp:
#             vulnerabilities.append("Missing Content-Security-Policy header")

#         return "No vulnerabilities found" if not vulnerabilities else ", ".join(vulnerabilities)
#     finally:
#         driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup

# def remove_iframes(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     for iframe in soup.find_all('iframe'):
#         iframe.extract()
#     return str(soup)

# def check_clickjacking(url):
#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(options=options)

#     try:
#         driver.get(url)
#         html_content = driver.page_source

#         html_content_without_iframes = remove_iframes(html_content)

#         x_frame_options = "X-Frame-Options" in html_content_without_iframes
#         csp = "Content-Security-Policy" in html_content_without_iframes
#         vulnerabilities = []

#         if not x_frame_options:
#             vulnerabilities.append("Missing X-Frame-Options header")
#         if not csp:
#             vulnerabilities.append("Missing Content-Security-Policy header")

#         return html_content_without_iframes, "No vulnerabilities found" if not vulnerabilities else ", ".join(vulnerabilities)
#     finally:
#         driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

def remove_iframes(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for iframe in soup.find_all('iframe'):
        iframe.extract()
    return str(soup)

def check_clickjacking(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        html_content = driver.page_source

        html_content = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)

        html_content_without_iframes = remove_iframes(html_content)

        x_frame_options = "X-Frame-Options" in html_content_without_iframes
        csp = "Content-Security-Policy" in html_content_without_iframes
        vulnerabilities = []

        if not x_frame_options:
            vulnerabilities.append("Missing X-Frame-Options header")
        if not csp:
            vulnerabilities.append("Missing Content-Security-Policy header")

        return html_content_without_iframes, "No vulnerabilities found" if not vulnerabilities else ", ".join(vulnerabilities)
    finally:
        driver.quit()
