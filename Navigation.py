import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "checkBoxOption2").click()
driver.find_element(By.CLASS_NAME, "radioButton").click()
driver.find_element(By.NAME, "radioButton").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "InterviewQues/ResumeAssistance").click()
# driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
print(driver.title)

driver.back()

driver.find_element(By.CSS_SELECTOR, "input[value='radio2']").click()

driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("Ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] div")
print(len(countries))
for country in countries:
    if country.text == "Indonesia":
        country.click()
        break

driver.implicitly_wait(10)

#print(driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value"))
select = Select(driver.find_element(By.ID, 'dropdown-class-example'))
select.select_by_index(2)

driver.implicitly_wait(10)

print(driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value"))