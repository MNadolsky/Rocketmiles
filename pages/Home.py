
from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

import config



class HomePage():

    def __init__(self, session):

        session.get(config.homepage_url)
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

    def location_field(self): return self.page.find_element_by_xpath("//input[@placeholder='Where do you need a hotel?']")
    def location_field_contents(self):    return self.location_field().get_attribute('value')
    def input_location_field(self, keys): self.location_field().send_keys(keys)
    def click_location_field(self):       self.location_field().click()

    def rewards_field(self): return self.page.find_element_by_xpath("//input[@placeholder='Select reward program']")
    def rewards_field_contents(self):    return self.rewards_field().get_attribute('value')
    def input_rewards_field(self, keys): self.rewards_field().send_keys(keys)
    def click_rewards_field(self):       self.rewards_field().click()


    # Widgets

    def contact_widget_loc(self):   return (by.CLASS_NAME, 'contact-widget')
    def contact_widget(self):       return self.page.find_element_by_class_name('contact-widget')
    def click_contact_widget(self): 
        wait(self.page,10).until(EC.element_to_be_clickable(self.contact_widget_loc()))
        self.contact_widget().click()

    # Modals

    def email_modal_loc(self): return (by.CLASS_NAME, 'user-email-modal')

    # Pop-overs

    def location_popover_loc(self): return (by.XPATH, "//div[@class='popover-content'][contains(text(),'Unknown location')]")
    def location_popover(self):
        wait(self.page,10).until(EC.presence_of_element_located(self.location_popover_loc()))
        return self.page.find_element_by_xpath("//div[@class='popover-content'][contains(text(),'Unknown location')]")

    def rewards_popover_loc(self): return (by.XPATH, "//div[@class='popover-content'][contains(text(),'Reward program')]")
    def rewards_popover(self):
        wait(self.page,10).until(EC.presence_of_element_located(self.rewards_popover_loc()))
        return self.page.find_element_by_xpath("//div[@class='popover-content'][contains(text(),'Reward program')]")

    # Dropdowns

    def location_dropdown(self): return self.page.find_element_by_class_name('tt-dropdown-menu')
    def location_dropdown_suggested_items(self):
        return self.location_dropdown().find_element_by_class_name('tt-dataset-suggestedPlaces')
    def location_dropdown_item(self, item_text):
        return self.location_dropdown_suggested_items().find_element_by_xpath(".//*[contains(text(),'" + item_text + "')]")
    def click_location_dropdown_item(self, item_text): self.location_dropdown_item(item_text).click()

    def rewards_dropdown(self): return self.page.find_element_by_xpath("//ul[@class='dropdown-menu'][@role='listbox']")
    def rewards_dropdown_item(self, item_text):
        return self.rewards_dropdown().find_element_by_xpath(".//a[contains(text(),'" + item_text + "')]")
    def click_rewards_dropdown_item(self, item_text): self.rewards_dropdown_item(item_text).click()
















