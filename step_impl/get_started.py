import os
from getgauge.python import before_suite, after_suite, step
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
from uuid import uuid1
from getgauge.python import custom_screenshot_writer

class Driver:
    instance = None

@before_suite
def init():
    global driver
    options = Options()
    #  By default the chrom instance is launched in
    #  headless mode. Do not pass this option if
    #  you want to see the browser window
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-dedv-shm-usage')
    options.add_argument("--no-sandbox")

    Driver.instance = webdriver.Chrome(chrome_options=options)

@after_suite
def close():
    Driver.instance.close()

@step("Search for <query>")
def go_to_get_started_page(query):
  textbox = Driver.instance.find_element_by_xpath("//input[@name='q']")
  textbox.send_keys(query)
  textbox.send_keys(Keys.RETURN)

@step("Read overview of onboarding process")
def read_overview_of_onboarding_process():
    Driver.instance.get('https://example.com/read-overview-of-onboarding-process')

@step("Select product package")
def select_product_package():
    Driver.instance.get('https://example.com/select-product-package')

@step("Accept GDPR agreement")
def accept_gdpr_agreement():
    Driver.instance.get('https://example.com/accept-gdpr-agreement')

@step("Confirm phone number")
def confirm_phone_number():
    Driver.instance.get('https://example.com/confirm-phone-number')

@step("Allow access to camera for OCR & Liveness check")
def allow_access_to_camera_for_ocr_and_liveness_check():
    Driver.instance.get('https://example.com/allow-access-to-camera-for-ocr-and-liveness-check')

@step("Confirm email address")
def confirm_email_address():
    Driver.instance.get('https://example.com/confirm-email-address')

@step("Provide personal ID")
def provide_personal_id():
    Driver.instance.get('https://example.com/provide-carte-de-identitate')

@step("Perform liveness checks")
def perform_liveness_checks():
    Driver.instance.get('https://example.com/perform-liveness-checks')

@step("Go to Google homepage at <url>")
def go_to_gauge_homepage_at(url):
    Driver.instance.get(url)

# Return a screenshot file name
@custom_screenshot_writer
def take_screenshot():
    image = Driver.instance.get_screenshot_as_png()
    file_name = os.path.join(os.getenv("gauge_screenshots_dir"), "screenshot-{0}.png".format(uuid1().int))
    file = open(file_name, "wb")
    file.write(image)
    return os.path.basename(file_name)
