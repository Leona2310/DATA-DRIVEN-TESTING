from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Read CSV file
data = pd.read_csv("testdata.csv")

# Launch Chrome (make sure chromedriver is in this folder)
driver = webdriver.Chrome()

# Create result log file
log = open("results.txt", "w")

# Run test for each row
for index, row in data.iterrows():
    username = row["username"]
    password = row["password"]

    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Check result
    if "inventory" in driver.current_url:
        result = "PASS"
    else:
        result = "FAIL"

    print(username, result)
    log.write(f"{username} : {result}\n")

    driver.delete_all_cookies()

log.close()
driver.quit()
