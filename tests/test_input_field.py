import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from source.page import *
from source.input_component import *
from source.logger import *
from resources.element_locators import InputForm, PopUpLocators, PrintElements

elem_txt = None
elem_lbl = None
elem_btn = None
elem_sum_txt1 = None
elem_sum_txt2 = None
elem_sum_lbl = None
elem_sum_btn = None
tlog = None


@pytest.fixture(scope='module')
def setup():
    global tlog
    global elem_txt
    global elem_lbl
    global elem_btn
    global elem_sum_txt1
    global elem_sum_txt2
    global elem_sum_lbl
    global elem_sum_btn
    tlog = Logger(__name__)
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info(PrintElements.ts_create)
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info(PrintElements.bw_open)
    mypage = Page('chrome', 'basic-first-form-demo.html')
    driver = mypage.driver
    tlog.logger.info(PrintElements.bw_cur_url.format(driver.current_url))
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, PopUpLocators.pop_up_div)))
    except Exception as e:
        tlog.logger.info(PrintElements.popup_absent)
        pass
    else:
        driver.find_element_by_xpath(PopUpLocators.pop_up_close).click()
        tlog.logger.info(PrintElements.popup_closed)
    tlog.logger.info(PrintElements.separator_line+'\n')
    elem_txt = InputComponent(driver, InputForm.single_field_input)
    elem_lbl = LabelComponent(driver, InputForm.single_field_message)
    elem_btn = ButtonComponent(driver, InputForm.single_field_button)

    elem_sum_txt1 = InputComponent(driver, InputForm.two_field_input_1)
    elem_sum_txt2 = InputComponent(driver, InputForm.two_field_input_2)
    elem_sum_lbl = LabelComponent(driver, InputForm.two_field_message)
    elem_sum_btn = ButtonComponent(driver, InputForm.two_field_button)
    yield
    mypage.close_driver()
    tlog.logger.info(PrintElements.ts_end)


def test_single_textfield(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 1: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val = 'Try Me'
    tlog.logger.info('Message to enter: {}'.format(set_val))
    elem_txt.clear_text()
    elem_txt.set_value(set_val)
    elem_btn.click()
    get_val = elem_lbl.get_value()
    tlog.logger.info('Message displayed: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if set_val == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert set_val == get_val


def test_single_textfield_big_string(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 2: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val = 'Ask me '*1000
    tlog.logger.info('Message to enter: {}'.format(set_val))
    elem_txt.clear_text()
    elem_txt.set_value(set_val)
    elem_btn.click()
    get_val = elem_lbl.get_value()
    get_val = get_val + ' '
    tlog.logger.info('Message displayed: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if set_val == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert set_val == get_val


def test_single_textfield_empty(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 3: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val = ''
    tlog.logger.info('Message to enter: {}'.format(set_val))
    elem_txt.clear_text()
    elem_txt.set_value(set_val)
    elem_btn.click()
    get_val = elem_lbl.get_value()
    tlog.logger.info('Message displayed: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if set_val == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert set_val == get_val


def test_single_textfield_special_chars(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 4: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val = '!@#$%&*()_+'
    tlog.logger.info('Message to enter: {}'.format(set_val))
    elem_txt.clear_text()
    elem_txt.set_value(set_val)
    elem_btn.click()
    get_val = elem_lbl.get_value()
    tlog.logger.info('Message displayed: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if set_val == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert set_val == get_val


def test_multiple_input_fields_sum_positive_numbers(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 5: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val1 = 25
    set_val2 = 37
    ans_val = 62
    elem_sum_txt1.clear_text()
    elem_sum_txt2.clear_text()
    elem_sum_txt1.set_value(str(set_val1))
    tlog.logger.info('Value in first field: {}'.format(str(set_val1)))
    elem_sum_txt2.set_value(str(set_val2))
    tlog.logger.info('Value in second field: {}'.format(str(set_val2)))
    elem_sum_btn.click()
    get_val = elem_sum_lbl.get_value()
    tlog.logger.info('Expected sum: {}'.format(str(ans_val)))
    tlog.logger.info('Obtained sum: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if str(ans_val) == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert str(ans_val) == get_val


def test_multiple_input_fields_sum_positive_negative_numbers_1(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 6: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val1 = -25
    set_val2 = 37
    ans_val = 12
    elem_sum_txt1.clear_text()
    elem_sum_txt2.clear_text()
    elem_sum_txt1.set_value(str(set_val1))
    tlog.logger.info('Value in first field: {}'.format(str(set_val1)))
    elem_sum_txt2.set_value(str(set_val2))
    tlog.logger.info('Value in second field: {}'.format(str(set_val2)))
    elem_sum_btn.click()
    get_val = elem_sum_lbl.get_value()
    tlog.logger.info('Expected sum: {}'.format(str(ans_val)))
    tlog.logger.info('Obtained sum: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if str(ans_val) == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert str(ans_val) == get_val


def test_multiple_input_fields_sum_positive_negative_numbers_2(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 7: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val1 = 25
    set_val2 = -37
    ans_val = -12
    elem_sum_txt1.clear_text()
    elem_sum_txt2.clear_text()
    elem_sum_txt1.set_value(str(set_val1))
    tlog.logger.info('Value in first field: {}'.format(str(set_val1)))
    elem_sum_txt2.set_value(str(set_val2))
    tlog.logger.info('Value in second field: {}'.format(str(set_val2)))
    elem_sum_btn.click()
    get_val = elem_sum_lbl.get_value()
    tlog.logger.info('Expected sum: {}'.format(str(ans_val)))
    tlog.logger.info('Obtained sum: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if str(ans_val) == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert str(ans_val) == get_val


def test_multiple_input_fields_sum_negative_numbers(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 8: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val1 = -25
    set_val2 = -37
    ans_val = -62
    elem_sum_txt1.clear_text()
    elem_sum_txt2.clear_text()
    elem_sum_txt1.set_value(str(set_val1))
    tlog.logger.info('Value in first field: {}'.format(str(set_val1)))
    elem_sum_txt2.set_value(str(set_val2))
    tlog.logger.info('Value in second field: {}'.format(str(set_val2)))
    elem_sum_btn.click()
    get_val = elem_sum_lbl.get_value()
    tlog.logger.info('Expected sum: {}'.format(str(ans_val)))
    tlog.logger.info('Obtained sum: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if str(ans_val) == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert str(ans_val) == get_val


def test_multiple_input_fields_sum_positive_big_numbers(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 9: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val1 = 257
    set_val2 = 32767
    ans_val = 33024
    elem_sum_txt1.clear_text()
    elem_sum_txt2.clear_text()
    elem_sum_txt1.set_value(str(set_val1))
    tlog.logger.info('Value in first field: {}'.format(str(set_val1)))
    elem_sum_txt2.set_value(str(set_val2))
    tlog.logger.info('Value in second field: {}'.format(str(set_val2)))
    elem_sum_btn.click()
    get_val = elem_sum_lbl.get_value()
    tlog.logger.info('Expected sum: {}'.format(str(ans_val)))
    tlog.logger.info('Obtained sum: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if str(ans_val) == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert str(ans_val) == get_val


def test_multiple_input_fields_sum_positive_bigger_numbers(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 10: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val1 = 2147483647
    set_val2 = 9223372036854775807
    ans_val = 9223372039002259454
    elem_sum_txt1.clear_text()
    elem_sum_txt2.clear_text()
    elem_sum_txt1.set_value(str(set_val1))
    tlog.logger.info('Value in first field: {}'.format(str(set_val1)))
    elem_sum_txt2.set_value(str(set_val2))
    tlog.logger.info('Value in second field: {}'.format(str(set_val2)))
    elem_sum_btn.click()
    get_val = elem_sum_lbl.get_value()
    tlog.logger.info('Expected sum: {}'.format(str(ans_val)))
    tlog.logger.info('Obtained sum: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if str(ans_val) == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert str(ans_val) == get_val


def test_multiple_input_fields_sum_fractions(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 11: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val1 = 24.15
    set_val2 = 37.25
    ans_val = 61.4
    elem_sum_txt1.clear_text()
    elem_sum_txt2.clear_text()
    elem_sum_txt1.set_value(str(set_val1))
    tlog.logger.info('Value in first field: {}'.format(str(set_val1)))
    elem_sum_txt2.set_value(str(set_val2))
    tlog.logger.info('Value in second field: {}'.format(str(set_val2)))
    elem_sum_btn.click()
    get_val = elem_sum_lbl.get_value()
    tlog.logger.info('Expected sum: {}'.format(str(ans_val)))
    tlog.logger.info('Obtained sum: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if str(ans_val) == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert str(ans_val) == get_val


def test_multiple_input_fields_sum_strings(setup):
    tlog.logger.info(PrintElements.separator_line)
    tlog.logger.info('Test 12: {}'.format(sys._getframe().f_code.co_name))
    tlog.logger.info(PrintElements.separator_line)
    set_val1 = 'Time'
    set_val2 = ' Stamp'
    ans_val = 'Time Stamp'
    elem_sum_txt1.clear_text()
    elem_sum_txt2.clear_text()
    elem_sum_txt1.set_value(str(set_val1))
    tlog.logger.info('Value in first field: {}'.format(str(set_val1)))
    elem_sum_txt2.set_value(str(set_val2))
    tlog.logger.info('Value in second field: {}'.format(str(set_val2)))
    elem_sum_btn.click()
    get_val = elem_sum_lbl.get_value()
    tlog.logger.info('Expected sum: {}'.format(str(ans_val)))
    tlog.logger.info('Obtained sum: {}'.format(get_val))
    tlog.logger.info(PrintElements.separator_line)
    if ans_val == get_val:
        tlog.logger.info('Result: {}'.format('PASS'))
    else:
        tlog.logger.fatal('Result: {}'.format('FAIL'))
    tlog.logger.info(PrintElements.separator_line+PrintElements.blank_line)
    assert ans_val == get_val
