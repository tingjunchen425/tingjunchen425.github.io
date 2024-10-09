from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://onlinealarmkur.com/world/zh-tw/"
driver = webdriver.Chrome()
driver.get(url)

date_element = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div/div[1]')
time_element = driver.find_element(By.CSS_SELECTOR, 'div[class="text-7xl xs:text-[5rem] sm:text-8xl md:text-9xl mt-6"]')
print(date_element.text, end=' ')
print(time_element.text)
driver.quit()

''' 
<div data-format="YYYY年M月D日dddd" class="text-2xl" id="date">2024年10月9日星期三</div> 
<div data-format="HH:mm:ss" data-format-original="HH:mm:ss" class="text-7xl xs:text-[5rem] sm:text-8xl md:text-9xl mt-6" id="clock">14:53:04</div>
'''