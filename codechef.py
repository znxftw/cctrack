from files import read, write
import selenium
from selenium import webdriver
from constants import codechef_rating_class, codechef_profile, codechef_file_name


def cc_read():
    return read(codechef_file_name)


def cc_write(contents, today, driver):
    driver.get(codechef_profile)
    rating = [i.text for i in driver.find_elements_by_class_name(
        codechef_rating_class)]
    write(codechef_file_name, contents, today, rating)
