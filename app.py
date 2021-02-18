from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(3)
driver.get("https://hyomo777.github.io/Reaction/")

driver.find_element_by_class_name("waiting").click()

now = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, "now"))
)

now.click()
