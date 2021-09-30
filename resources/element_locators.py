class InputForm:
    single_field_message = './/span[@id="display"]'
    single_field_input = './/input[@id="user-message"]'
    single_field_button = './/button[text()="Show Message"]'
    two_field_input_1 = './/input[@id="sum1"]'
    two_field_input_2 = './/input[@id="sum2"]'
    two_field_button = './/button[text()="Get Total"]'
    two_field_message = './/span[@id="displayvalue"]'


class PopUpLocators:
    pop_up_close = './/a[@title="Close"]'
    pop_up_div = './/div[@id="at-cv-lightbox-header"]'


class CheckBoxLocators:
    single_check_box = './/input[@id="isAgeSelected"]'
    single_check_success_lbl = './/div[@id="txtAge"]'
    single_check_success_msg = 'Success - Check box is checked'

    multi_check_box = './/input[@class="cb1-element"]'
    multi_check_button = './/input[@id="check1"]'


class RadioLocators:
    single_group_radio = './/input[@name="optradio"]'
    single_group_btn = './/button[text()="Get Checked value"]'
    single_group_lbl = './/p[@class="radiobutton"]'
    single_group_msg1 = 'Radio button is Not checked'
    single_group_msg2 = 'Radio button \'{}\' is checked'
    single_group_vals = ['Male', 'Female']


class PrintElements:
    blank_line = '\n'
    separator_line = '-'*80
    ts_create = 'Creating test setup'
    ts_end = 'Closed browser after test execution\n'
    bw_open = 'Opening browser'
    bw_cur_url = 'Current URL: {}'
    popup_absent = 'Pop up dialog did not appear'
    popup_closed = 'Closed unwanted pop up dialog'
