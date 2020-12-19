from files import read, write
import selenium
from selenium import webdriver
from constants import codeforces_rating_xpath, codeforces_profile, codeforces_file_name


def cf_read():
    return read(codeforces_file_name)


def cf_write(contents, today, driver):
    driver.get(codeforces_profile)
    rating = [driver.find_element_by_xpath(codeforces_rating_xpath).text]
    write(codeforces_file_name, contents, today, rating)
