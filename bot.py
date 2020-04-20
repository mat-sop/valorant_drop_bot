import random
import sys
import time
from datetime import datetime, timedelta
from getpass import getpass
from signal import SIGINT, signal

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


def log_current_url(driver):
    print(f'{datetime.now().time()}\t{driver.current_url}')


def log_in(driver, username, password):
    login_button = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath(
            "//*[contains(text(), 'Log In')]")
    )
    login_button.click()

    username_input = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_id('login-username')
    )
    password_input = driver.find_element_by_id('password-input')
    username_input.send_keys(username)
    password_input.send_keys(password)

    passport_login_button = driver.find_element_by_xpath(
        "//*[@data-a-target='passport-login-button']")
    passport_login_button.click()

    confirmation_code_input = WebDriverWait(driver, 30).until(
        lambda x: x.find_element_by_xpath(
            "//*[@autocomplete='one-time-code']")
    )
    code = input('2FA Code: ')
    confirmation_code_input.send_keys(code)

    submit_button = driver.find_element_by_xpath(
        "//*[contains(text(), 'Submit')]")
    submit_button.click()


def get_random_valorant_channel(driver):
    channels = WebDriverWait(driver, 10).until(
        lambda x: x.find_elements_by_xpath(
            "//a[@data-a-target='preview-card-title-link']")
    )[:10]
    random.shuffle(channels)
    return channels[0]


def get_watching_time(min_sec=2*60*60, max_sec=2.5*60*60):
    return random.randint(min_sec, max_sec)


def get_valorant_category_link(driver):
    return driver.find_element_by_xpath(
        "//*[@data-a-target='stream-game-link']")


def sigint_handler(signum, frame):
    driver.quit()
    sys.exit(0)


signal(SIGINT, sigint_handler)


username = input('Username: ')
password = getpass('Password: ')

chrome_options = Options()
# chrome_options.add_argument('--headless') # problems with captcha during login
chrome_options.add_argument('--mute-audio')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.twitch.tv/directory/game/VALORANT')
log_in(driver, username, password)
time.sleep(5)  # reload of page after login

while True:
    channel = get_random_valorant_channel(driver)
    ActionChains(driver).move_to_element(channel).perform()
    channel.click()
    log_current_url(driver)

    watching_time = get_watching_time()
    approx_time = datetime.now() + timedelta(seconds=watching_time)
    print(
        f'Approximate time to end watching {driver.current_url} : \t {approx_time.time()}')
    time.sleep(watching_time)

    category_link = get_valorant_category_link(driver)
    category_link.click()
