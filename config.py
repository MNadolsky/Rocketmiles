
import os


# Windows is default. To run the tests on another OS, replace the end of the chromedriver_path variable with one of the three driver
# filenames below
windows_chromedriver = 'chromedriver.exe'
mac_chromedriver = 'mac/chromedriver'
linux_chromedriver = 'linux/chromedriver'

chromedriver_path = os.path.dirname(os.path.realpath(__file__)) + '/resources/' + windows_chromedriver

homepage_url = 'https://www.rocketmiles.com/'
search_url = 'https://www.rocketmiles.com/search'
