from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://translate.google.com/?hl=zh-TW&sl=en&tl=zh-TW&op=translate"
words = str(input("輸入單字:"))
driver = webdriver.Chrome()
driver.get(url)
trasnlate_element = driver.find_element(By.CSS_SELECTOR, 'textarea[class="er8xn"]')
trasnlate_element.send_keys(words)
trasnlate_element.send_keys(Keys.ENTER)
driver.implicitly_wait(5)
result = driver.find_element(By.CSS_SELECTOR, 'span[class="ryNqvb"]')
print(result.text)

'''
<textarea aria-label="原文內容" aria-autocomplete="list" aria-expanded="false" aria-controls="kvLWu" class="er8xn" jsaction="blur:TP1Wfd; click:R8nDBd; focus:HCeAxb; input:r9XDpf,Gyn8rd; keydown:O0Dsab,RHer4; select:BR6jm,RHer4; paste:puy29d;" jsname="BJE2fc" jslog="176025; track:click,input,paste;" autocapitalize="off" autocomplete="off" autocorrect="off" role="combobox" rows="1" placeholder="" spellcheck="false" style="height: 32px;"></textarea>
<span class="ryNqvb" jsname="W297wb" jsaction="click:PDNqTc,GFf3ac,qlVvte;contextmenu:Nqw7Te,QP7LD; mouseout:Nqw7Te; mouseover:PDNqTc,c2aHje"></span>
'''