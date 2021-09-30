import pytest
import sys
from source.page import *
from source.input_component import *
from source.logger import *
from resources.element_locators import RadioLocators, PopUpLocators


driver = None
elem_grp_radio = None
elem_grp_btn = None
elem_grp_lbl = None
elem_grp_msg = None
tlog = None


@pytest.fixture(scope='module')
def setup():
    global tlog
    global driver

    tlog = Logger(__name__)
    tlog.logger.info('-'*80)
    tlog.logger.info('Creating test setup')
    tlog.logger.info('-'*80)
    mypage = Page('chrome', 'basic-radiobutton-demo.html')
    driver = mypage.driver
    tlog.logger.info('Opened browser with URL: {}'.format(driver.current_url))
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, PopUpLocators.pop_up_div)))
    except Exception as e:
        tlog.logger.info('Pop up dialog did not appear')
        pass
    else:
        driver.find_element_by_xpath(PopUpLocators.pop_up_close).click()
        tlog.logger.info('Closed unwanted pop up dialog')
    tlog.logger.info('-'*80+'\n')
    yield
    mypage.close_driver()
    tlog.logger.info('Closed browser after test execution')


def test_radio_single_group_no_opt_selected(setup):
    global elem_grp_msg
    global elem_grp_lbl
    global elem_grp_btn
    global elem_grp_radio
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 1: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    elem_grp_radio = RadioComponent(driver, RadioLocators.single_group_radio)
    is_selected = elem_grp_radio.is_selected()
    elem_grp_btn = ButtonComponent(driver, RadioLocators.single_group_btn)
    elem_grp_btn.click()
    elem_grp_lbl = LabelComponent(driver, RadioLocators.single_group_lbl)
    obtained_msg = elem_grp_lbl.get_value()
    tlog.logger.info('Obtained message: {}'.format(obtained_msg))
    tlog.logger.info('Expected message: {}'.format(RadioLocators.single_group_msg1))
    tlog.logger.info('-' * 80)
    if is_selected is None and obtained_msg == RadioLocators.single_group_msg1:
        tlog.logger.info('Result: PASS')
    else:
        tlog.logger.fatal('Result: FAIL')
    tlog.logger.info('-'*80+'\n')
    assert obtained_msg == RadioLocators.single_group_msg1


def test_radio_single_group_option_male_selection(setup):
    global elem_grp_msg
    global elem_grp_lbl
    global elem_grp_btn
    global elem_grp_radio
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 2: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    elem_grp_radio = RadioComponent(driver, RadioLocators.single_group_radio)
    elem_grp_btn = ButtonComponent(driver, RadioLocators.single_group_btn)
    is_selected = elem_grp_radio.is_selected()
    if is_selected is None:
        tlog.logger.info('No radio option selected')
    else:
        tlog.logger.fatal('Option {} is already selected'.format(is_selected))
        assert is_selected is None
    tlog.logger.info('Selecting radio option Male')
    elem_grp_radio.select_opt('Male')
    tlog.logger.info('Clicking button')
    elem_grp_btn.click()
    is_selected = elem_grp_radio.is_selected()
    elem_grp_lbl = LabelComponent(driver, RadioLocators.single_group_lbl)
    elem_grp_msg = RadioLocators.single_group_msg2.format('Male')
    obtained_msg = elem_grp_lbl.get_value()
    tlog.logger.info('Value of selected option: {}'.format(is_selected))
    tlog.logger.info('Obtained message: {}'.format(obtained_msg))
    tlog.logger.info('Expected message: {}'.format(elem_grp_msg))
    tlog.logger.info('-' * 80)
    if is_selected == 'Male' and elem_grp_msg == obtained_msg:
        tlog.logger.info('Result: PASS')
    else:
        tlog.logger.fatal('Result: FAIL')
    tlog.logger.info('-'*80+'\n')
    assert obtained_msg == elem_grp_msg


def test_radio_single_group_option_female_selection(setup):
    global elem_grp_msg
    global elem_grp_lbl
    global elem_grp_btn
    global elem_grp_radio
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 3: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    elem_grp_radio = RadioComponent(driver, RadioLocators.single_group_radio)
    elem_grp_btn = ButtonComponent(driver, RadioLocators.single_group_btn)
    tlog.logger.info('Selecting radio option Female')
    elem_grp_radio.select_opt('Female')
    tlog.logger.info('Clicking button')
    elem_grp_btn.click()
    is_selected = elem_grp_radio.is_selected()
    elem_grp_lbl = LabelComponent(driver, RadioLocators.single_group_lbl)
    elem_grp_msg = RadioLocators.single_group_msg2.format('Female')
    obtained_msg = elem_grp_lbl.get_value()
    tlog.logger.info('Value of selected option: {}'.format(is_selected))
    tlog.logger.info('Obtained message: {}'.format(obtained_msg))
    tlog.logger.info('Expected message: {}'.format(elem_grp_msg))
    tlog.logger.info('-' * 80)
    if is_selected == 'Female' and elem_grp_msg == obtained_msg:
        tlog.logger.info('Result: PASS')
    else:
        tlog.logger.fatal('Result: FAIL')
    tlog.logger.info('-'*80+'\n')
    assert obtained_msg == elem_grp_msg


def test_radio_single_group_options(setup):
    global elem_grp_radio
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 4: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    elem_grp_radio = RadioComponent(driver, RadioLocators.single_group_radio)
    obtained_opt_vals = elem_grp_radio.get_values()
    obtained_opt_vals.sort()
    expected_opt_vals = RadioLocators.single_group_vals
    expected_opt_vals.sort()
    tlog.logger.info('Obtained values for single radio button group: {}'.format(str(obtained_opt_vals)))
    tlog.logger.info('Expected values for single radio button group: {}'.format(str(expected_opt_vals)))
    tlog.logger.info('-' * 80)
    if obtained_opt_vals == expected_opt_vals:
        tlog.logger.info('Result: PASS')
    else:
        tlog.logger.fatal('Result: FAIL')
    tlog.logger.info('-'*80+'\n')
    assert obtained_opt_vals == expected_opt_vals
