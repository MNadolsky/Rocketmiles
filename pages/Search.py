
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import config



class SearchPage():

    def __init__(self, session):

        self.page = session
        try: wait(self.page,30).until(EC.invisibility_of_element_located(self.search_transition_loc()))
        except NoSuchElementException: pass

    # Text

    def search_summary(self): return self.page.find_element_by_class_name('search-summary-container-transparent').text

    # Transitions

    def search_transition_loc(self): return self.page.find_element_by_class_name('search-transition')
 
