from files import read, write
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import leetcode_profile, leetcode_rating_class, leetcode_file_name


def lc_read():
    return read(leetcode_file_name)


def lc_write(contents, today, driver):
    driver.get(leetcode_profile)
    wait = WebDriverWait(driver, 10)

    # Dynamic webpage, had problem retrieving rating unless page was fully loaded.
    rating = [i.text for i in wait.until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, leetcode_rating_class)))]
    write(leetcode_file_name, contents, today, rating)
