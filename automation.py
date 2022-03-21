from http.server import executable
from selenium import webdriver
chrome_browser = webdriver.Chrome(executable_path='./chromedriver.exe')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_msg_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_msg_button.get_attribute('innerHTML'))

user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)

assert 'Show Message' in chrome_browser.page_source
user_msg = chrome_browser.find_element_by_id('user-message')
user_msg.clear()
user_msg.send_keys('I AM SO COOL')

show_msg_button.click()
output_msg = chrome_browser.find_element_by_id('display')
assert 'I AM SO COOL' in output_msg.text

chrome_browser.quit()
chrome_browser.quit()