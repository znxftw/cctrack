from files import read, write
import selenium
from selenium import webdriver
from constants import codechef_rating_class, codechef_profile


def cc_read():
    return read('codechef.csv')


def cc_write(contents, today, driver):
    driver.get(codechef_profile)
    rating = [i.text for i in driver.find_elements_by_class_name(codechef_rating_class)]
    write('codechef.csv', contents, today, rating)
