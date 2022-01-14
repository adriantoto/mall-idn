import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_all_malls_name():
    """To scrape all mall's name in jabodetabek

    Returns:
        List: all mall's name
    """
    url = "https://en.wikipedia.org/wiki/List_of_shopping_malls_in_Jakarta"
    driver = webdriver.Firefox()
    driver.get(url)
    all_malls = []
    for i in range(2, 12):
        for items in driver.find_elements(
            By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[{}]/ul'.format(i)
        ):
            for item in items.find_elements(By.TAG_NAME, "li"):
                all_malls.append(item.text)

    for i in range(1, 4):
        for items in driver.find_elements(
            By.XPATH, '//*[@id="mw-content-text"]/div[1]/ul[{}]'.format(i)
        ):
            for item in items.find_elements(By.TAG_NAME, "li"):
                all_malls.append(item.text)
    driver.quit()
    all_malls = list(dict.fromkeys(all_malls))  # to remove duplicate in list
    return all_malls
