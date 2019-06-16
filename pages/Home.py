
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import config



class HomePage():

    def __init__(self, session):

        session.get('http://www.rocketmiles.com')
        session.set_window_position(2000,0)
        session.maximize_window()
        self.page = session

    # Buttons

    def cookie_banner_button(self):       return self.page.find_element_by_class_name('cookie-banner-button')
    def click_cookie_banner_button(self): self.cookie_banner_button().click()

    def email_modal_close_button(self): return self.page.find_element_by_class_name('close')
    def click_email_modal_close_button(self):
        self.email_modal_close_button().click()
        wait(self.page,10).until(EC.invisibility_of_element_located(self.email_modal_loc()))

    def submit_button_loc(self): return (by.CLASS_NAME, 'search-submit-btn')
    def submit_button(self):     return self.page.find_element_by_class_name('search-submit-btn')
    def click_submit_button(self):
        wait(self.page,10).until(EC.element_to_be_clickable(self.submit_button_loc()))
        self.submit_button().click()

    # Fields

    def location_field(self):             self.page.find_element_by_xpath("//input[@placeholder='Where do you need a hotel?']")
    def input_location_field(self, keys): self.location_field().send_keys(keys)

    # Widgets

    def contact_widget_loc(self):   return (by.CLASS_NAME, 'contact-widget')
    def contact_widget(self):       return self.page.find_element_by_class_name('contact-widget')
    def click_contact_widget(self): 
        wait(self.page,10).until(EC.element_to_be_clickable(self.contact_widget_loc()))
        self.contact_widget().click()

    # Modals

    def email_modal_loc(self): return (by.CLASS_NAME, 'user-email-modal')

    # Pop-overs

    def location_popover(self): return self.page.find_element_by_class_name('popover-content')
