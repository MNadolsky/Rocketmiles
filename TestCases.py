
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

import unittest

import config
from pages.Home import *
from pages.Search import *

import time


class HomePageTemplate(unittest.TestCase):

    def setUp(self):

        self.session = webdriver.Chrome(config.chromedriver_path)
        self.page = HomePage(self.session)
        self.page.click_cookie_banner_button()
        self.page.click_email_modal_close_button()

#        self.search_page = SearchPage(self.session)

    def tearDown(self):

        self.session.quit()



class LocationFieldPopover(HomePageTemplate):
    """
    Confirm the location field popover is invoked when submit is pressed with no input or incorrect
    input in the location field. Confirm that the popover is dismissed when the user clicks on the
    location field.

    acceptance criteria
    --------------------
    - When the location field is empty and the submit button is clicked, the location field popover
        appears and the user is not navigated away from the home page
    - When the location field has invalid contents and the submit button is clicked, as above
    - If the location field popover is visible, it is dismissed when the user clicks the location field
    """


    def testNoInput(self):

        self.page.click_submit_button()

        try: popover = self.page.location_popover()
        except (TimeoutException, NoSuchElementException): popover = None

        self.assertTrue(popover)
        self.assertTrue(self.session.current_url == config.homepage_url, '\nCurrent URL: ' + self.session.current_url)

    def testIncorrectInput(self):

        self.page.input_location_field('cats are better than dogs')
        time.sleep(1) # Sometimes the 'no offers' popover isn't dismissed if the submit button is clicked too quickly
        self.page.click_submit_button()

        try: popover = self.page.location_popover()
        except (TimeoutException, NoSuchElementException): popover = None

        self.assertTrue(popover)
        self.assertTrue(self.session.current_url == config.homepage_url, '\nCurrent URL: ' + self.session.current_url)

    def testPopoverDismiss(self): 

        # Invoke pupover
        self.page.click_submit_button()

        try: popover = self.page.location_popover()
        except (TimeoutException, NoSuchElementException): popover = None

        self.assertTrue(popover)

        # Dismiss popover
        self.page.click_location_field()

        try: popover = self.page.location_popover()
        except (TimeoutException, NoSuchElementException): popover = None

        self.assertFalse(popover)



class RewardsFieldPopover(HomePageTemplate):
    """
    Confirm the rewards field popover is invoked when submit is pressed with no input or incorrect
    input in the rewards field. Confirm that the popover is dismissed when the user clicks on the
    rewards field.

    acceptance criteria
    --------------------
    - When the rewards field is empty and the submit button is clicked, the rewards field popover
        appears and the user is not navigated away from the home page
    - When the rewards field has invalid contents and the submit button is clicked, as above
    - If the rewards field popover is visible, it is dismissed when the user clicks the rewards field
    """



    def setUp(self):

        super().setUp()

        self.page.click_location_field()
        self.page.click_location_dropdown_item('Chicago')

    def testNoInput(self):

        self.page.click_submit_button()

        try: popover = self.page.rewards_popover()
        except (TimeoutException, NoSuchElementException): popover = None

        self.assertTrue(popover)
        self.assertTrue(self.session.current_url == config.homepage_url, '\nCurrent URL: ' + self.session.current_url)

    def testIncorrectInput(self): 

        self.page.input_rewards_field('The Beatles are overrated.')
        time.sleep(1) # Sometimes the 'choose a valid program' popover isn't dismissed if the submit button is clicked too quickly
        self.page.click_submit_button()

        try: popover = self.page.rewards_popover()
        except (TimeoutException, NoSuchElementException): popover = None

        self.assertTrue(popover)
        self.assertTrue(self.session.current_url == config.homepage_url, '\nCurrent URL: ' + self.session.current_url)

    def testPopoverDismiss(self):

        # Invoke pupover
        self.page.click_submit_button()

        try: popover = self.page.rewards_popover()
        except (TimeoutException, NoSuchElementException): popover = None

        self.assertTrue(popover)

        # Dismiss popover
        self.page.click_rewards_field()

        try: popover = self.page.rewards_popover()
        except (TimeoutException, NoSuchElementException): popover = None



class Search(HomePageTemplate):
    """
    Confirm that the submit button navigates the user to the search page when the location and input fields are correctly filled 
    via typing and clicking.

    acceptance criteria
    --------------------
    - When the location and input fields are filled out via dropdown and the submit button is clicked, the user is navigated to
    the search page
    - When the location and input fields are filled out via typing and the submit button is clicked, the user is navigated to
    the search page
    """
 


    def testTypeInput(self):

        page = self.page

        page.input_location_field('Chicago, IL, USA')
        page.input_rewards_field('United MileagePlus')
        page.click_submit_button()

        self.assertIn('https://www.rocketmiles.com/search', self.session.current_url,
            '\nLocation: ' + page.location_field_contents() + '\nRewards: ' + page.rewards_field_contents())

    def testDropdownInput(self):

        page = self.page

        page.click_location_field()
        page.click_location_dropdown_item('Chicago')
        page.click_rewards_field()
        page.click_rewards_dropdown_item('United')
        page.click_submit_button()

        self.assertIn(config.search_url, self.session.current_url,
            '\nLocation: ' + page.location_field_contents() + '\nRewards: ' + page.rewards_field_contents())



class SearchFunctionality(HomePageTemplate):
    """Confirm that the search results conform to the search request. Only location and rewards fields are tested.

    acceptance criteria
    --------------------
    - The search summary claims > 0 listings
    - The serach summary lists the city that was searched (matched to the string in the location dropdown)
    - The search summary lists the rewards program that was searched (summary rewards term is contained in the string in the
    rewards dropdown)
    """

    def parse_search_summary(self):

        summary = self.search_page.search_summary()

        num_results = int(summary.split('of')[1].split('hotels')[0].strip())
        city = summary.split('near')[1].split('earning')[0].strip()
        rewards = summary.split('earning')[1].split(" ")[0].strip()

        return num_results, city, rewards


    def testLocationAndRewards(self):

        page = self.page

        page.click_location_field()
        page.click_location_dropdown_item('Chicago')
        input_city = page.location_field_contents()

        page.click_rewards_field()
        page.click_rewards_dropdown_item('United')
        input_rewards = page.rewards_field_contents()

        page.click_submit_button()
        self.search_page = SearchPage(self.session)

        num_results, searched_city, searched_rewards = self.parse_search_summary()
        
        self.assertGreater(num_results, 0)
        self.assertEqual(input_city, searched_city)
        self.assertIn(searched_rewards, input_rewards)






if __name__ == '__main__': unittest.main()





























