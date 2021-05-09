from bs4 import BeautifulSoup
import requests
import pandas as pd
import utils

# Get data from vnexpress.net:
for i in range(199,2000):
    page_links = 'https://vnexpress.net/phap-luat-p{page_number}'.format(page_number=i)
    utils.get_data_from_page(page_links)