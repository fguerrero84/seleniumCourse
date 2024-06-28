from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


file_path = 'C:\Users\fguerrero\Downloads\download.xlsx'
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://rahulshettyacademy.com/upload-download-test/')
driver.maximize_window()
driver.find_element(By.ID, 'downloadbutton').click()

#here goes the excel modification code

#file upload
file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
file_input.send_keys(file_path)

#verify upload success
successmsg = driver.find_element(By.CSS_SELECTOR, '.Toastify__close-button div:nth-child(2)')
WebDriverWait(driver,10).until(EC.presence_of_element_located(successmsg))



