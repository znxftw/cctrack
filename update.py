from datetime import date
from codeforces import cf_read, cf_write
from codechef import cc_read, cc_write
from leetcode import lc_read, lc_write
import selenium
from selenium import webdriver
from constants import chromedriver_path

today = str(date.today())
driver = webdriver.Chrome(chromedriver_path)

cf_write(cf_read(), today, driver)
cc_write(cc_read(), today, driver)
lc_write(lc_read(), today, driver)

driver.quit()
