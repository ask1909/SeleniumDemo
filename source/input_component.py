from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class InputComponent:
    """
    A class to handle html component Text Field Input
    """

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = self.driver.find_element_by_xpath(self.locator)

    def is_empty(self):
        result = False
        if self.element.text == '':
            result = True
        return result

    def get_value(self):
        result = self.element.text
        return result

    def set_value(self, val):
        self.element.send_keys(val)
        # time.sleep(3)

    def clear_text(self):
        self.element.clear()

    def click_input(self):
        self.element.click()


class LabelComponent:
    """
    A class to handle html component Label (Static Text)
    """

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = self.driver.find_element_by_xpath(self.locator)

    def get_value(self):
        return self.element.text


class ButtonComponent:
    """
    A class to to handle html component Button
    """

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = self.driver.find_element_by_xpath(self.locator)

    def click(self):
        self.element.click()

    def get_value(self):
        return self.element.get_attribute('value')


class CheckBoxComponent:
    """
    A class to handle html component Checkbox
    """

    def __init__(self, driver, locator, grp=False):
        self.driver = driver
        self.locator = locator
        self.grouped = grp
        if grp:
            self.element = self.driver.find_elements_by_xpath(self.locator)
        else:
            self.element = self.driver.find_element_by_xpath(self.locator)

    def check_the_box(self):
        if self.grouped:
            raise TypeError('Not callable on group')
        if not self.element.is_selected():
            self.element.click()

    def uncheck_the_box(self):
        if self.element.is_selected():
            self.element.click()

    def checkbox_selected(self):
        if self.element.is_selected():
            return True
        return False

    def message_displayed(self, locator):
        if not self.element.is_selected():
            try:
                elem_msg = LabelComponent(self.driver, locator)
            except Exception:
                return True
            else:
                return False
        else:
            try:
                elem_msg = LabelComponent(self.driver, locator)
            except Exception:
                return False
            else:
                return True

    def multi_checkbox_status(self):
        if not self.grouped:
            raise TypeError('Not callable on single checkbox')
        result = True
        for elem in self.element:
            if elem.is_selected():
                result = result and True
            else:
                result = result and False
        return result


class RadioComponent:
    """
    A class to handle html component Radio Button
    """

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.elements = self.driver.find_elements_by_xpath(self.locator)

    def is_selected(self):
        result = None
        for elem in self.elements:
            if elem.is_selected():
                result = elem.get_attribute('value')
                break
        return result

    def get_values(self):
        elem_val = []
        for elem in self.elements:
            elem_val.append(elem.get_attribute('value'))
        return elem_val

    def select_opt(self, val):
        result = False
        for elem in self.elements:
            cur_val = elem.get_attribute('value')
            if cur_val == val:
                elem.click()
                result = True
                break
        return result
