from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
  
# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'platform': "macOS 10.13",
    'browserName': "chrome",
    'version': "63.0",
}
start_time = time.time()
driver = webdriver.Remote(
   command_executor='http://mahendar.baddam@scriptbees.com:efa0b361-f776-48e1-9c0c-09c778130d9b@ondemand.saucelabs.com:80/wd/hub',
   desired_capabilities=desired_cap)
end_time = time.time()
print(start_time - end_time)
# This is your test logic. You can add multiple tests here.
driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("Sauce Labs")
elem.submit()
print(driver.title)
  
# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
driver.quit()