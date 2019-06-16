
import unittest

import config
from pages.Home import *

import time


class HomePageTemplate(unittest.TestCase):

    def setUp(self):

        self.session = webdriver.Chrome(config.chromedriver_path)
        self.page = HomePage(self.session)
        self.page.click_cookie_banner_button()
        self.page.click_email_modal_close_button()

    def tearDown(self):

        self.session.quit()



class LocationFieldPopover(HomePageTemplate):
    """
    Confirm the location field popover is invoked when submit is pressed with no input or incorrect
    input in the location field

    acceptance criteria
    --------------------
    - If the location field is empty and the submit button is clicked, the location field popover
        appears and the user is not navigated away from the home page
    - If the location field has invalid contents and the submit button is clicked, as above
    """


    def testNoInput(self):

        self.page.click_submit_button()

        try:    popover = self.page.location_popover()
        except: popover = None

        self.assertTrue(popover)
        self.assertTrue(self.session.current_url == 'https://www.rocketmiles.com/')

    def testIncorrectInput(self): pass

    def testPopoverDismiss(self): pass



class RewardFieldError(HomePageTemplate):

    def testNoInput(self): pass

    def testIncorrectInput(self): pass

    def testPopoverDismiss(self): pass



class Search(HomePageTemplate):

    def testTypeInput(self): pass

    def testDropdownInput(self): pass





if __name__ == '__main__': unittest.main()
