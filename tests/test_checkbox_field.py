import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from source.page import *
from source.input_component import *
from source.logger import *
from resources.element_locators import CheckBoxLocators, PopUpLocators

driver = None
elem_single_checkbox = None
elem_single_checkbox_lbl = None
elem_single_checkbox_msg = None
elem_multi_checkbox = None
elem_multi_checkbox_btn = None
tlog = None


@pytest.fixture(scope='module')
def setup():
    global driver
    global tlog
    global elem_single_checkbox
    global elem_single_checkbox_msg
    global elem_multi_checkbox
    global elem_multi_checkbox_btn
    # global elem_single_checkbox_lbl
    tlog = Logger(__name__)
    tlog.logger.info('-'*80)
    tlog.logger.info('Creating test setup')
    tlog.logger.info('-'*80)
    mypage = Page('chrome', 'basic-checkbox-demo.html')
    driver = mypage.driver
    tlog.logger.info('Opened browser with URL: {}'.format(driver.current_url))
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, PopUpLocators.pop_up_div)))
    except Exception:
        tlog.logger.info('Pop up dialog did not appear')
        pass
    else:
        driver.find_element_by_xpath(PopUpLocators.pop_up_close).click()
        tlog.logger.info('Closed unwanted pop up dialog')
    tlog.logger.info('-'*80+'\n')
    elem_single_checkbox = CheckBoxComponent(driver, CheckBoxLocators.single_check_box)
    elem_single_checkbox_msg = CheckBoxLocators.single_check_success_msg
    # elem_single_checkbox_lbl = LabelComponent(driver, CheckBoxLocators.single_check_success_lbl)
    yield
    mypage.close_driver()


def test_single_checkbox_click(setup):
    global elem_single_checkbox_lbl
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 1: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    elem_single_checkbox.check_the_box()
    elem_single_checkbox_lbl = LabelComponent(driver, CheckBoxLocators.single_check_success_lbl)
    msg = elem_single_checkbox_lbl.get_value()
    tlog.logger.info('Obtained message: {}'.format(msg))
    tlog.logger.info('Expected message: {}'.format(elem_single_checkbox_msg))
    tlog.logger.info('-' * 80)
    if msg == elem_single_checkbox_msg:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info('-' * 80+'\n')
    assert msg == elem_single_checkbox_msg


def test_single_checkbox_message(setup):
    global elem_single_checkbox_lbl
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 2: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    chk_status = elem_single_checkbox.checkbox_selected()
    msg_displayed = elem_single_checkbox.message_displayed(CheckBoxLocators.single_check_success_lbl)
    tlog.logger.info('Checkbox checked? {}'.format(str(chk_status)))
    tlog.logger.info('Success Message displayed? {}'.format(str(msg_displayed)))
    if msg_displayed:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info('-' * 80 + '\n')
    assert chk_status == msg_displayed


def test_single_checkbox_message_negative(setup):
    global elem_single_checkbox_lbl
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 3: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    if elem_single_checkbox.checkbox_selected():
        elem_single_checkbox.uncheck_the_box()
    chk_status = elem_single_checkbox.checkbox_selected()
    msg_displayed = elem_single_checkbox.message_displayed(CheckBoxLocators.single_check_success_lbl)
    tlog.logger.info('Checkbox checked? {}'.format(str(chk_status)))
    tlog.logger.info('Success Message displayed? {}'.format(str(msg_displayed)))
    if not msg_displayed:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info('-' * 80 + '\n')
    assert chk_status == msg_displayed


def test_multi_checkbox_button_text_1():
    global elem_multi_checkbox
    global elem_multi_checkbox_btn
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 4: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    elem_multi_checkbox = CheckBoxComponent(driver, CheckBoxLocators.multi_check_box, grp=True)
    chk_grp_status = elem_multi_checkbox.multi_checkbox_status()
    elem_multi_checkbox_btn = ButtonComponent(driver, CheckBoxLocators.multi_check_button)
    btn_state = elem_multi_checkbox_btn.get_value()
    tlog.logger.info('Checkbox group status: {}'.format(str(chk_grp_status)))
    tlog.logger.info('Is button caption proper: {}'.format(str(btn_state)))
    if not chk_grp_status and btn_state == 'Check All':
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info('-' * 80 + '\n')


def test_multi_checkbox_button_text_2():
    global elem_multi_checkbox
    global elem_multi_checkbox_btn
    elem_multi_checkbox = CheckBoxComponent(driver, CheckBoxLocators.multi_check_box, grp=True)
    elem_multi_checkbox_btn = ButtonComponent(driver, CheckBoxLocators.multi_check_button)
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 5: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    elem_multi_checkbox_btn.click()
    chk_grp_status = elem_multi_checkbox.multi_checkbox_status()
    btn_state = elem_multi_checkbox_btn.get_value()
    tlog.logger.info('Checkbox group status: {}'.format(str(chk_grp_status)))
    tlog.logger.info('Is button caption proper: {}'.format(str(btn_state)))
    if chk_grp_status and btn_state == 'Uncheck All':
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info('-' * 80 + '\n')


def test_multi_checkbox_partial_selected():
    global elem_multi_checkbox
    global elem_multi_checkbox_btn
    elem_multi_checkbox = CheckBoxComponent(driver, CheckBoxLocators.multi_check_box, grp=True)
    elem_multi_checkbox_btn = ButtonComponent(driver, CheckBoxLocators.multi_check_button)
    tlog.logger.info('-'*80)
    tlog.logger.info('Test 6: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info('-'*80)
    btn_state = elem_multi_checkbox_btn.get_value()
    if btn_state != 'Uncheck All':
        elem_multi_checkbox_btn.click()
    elem_multi_checkbox.element[0].click()
    elem_multi_checkbox.element[-1].click()
    btn_state = elem_multi_checkbox_btn.get_value()
    if btn_state == 'Check All':
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
