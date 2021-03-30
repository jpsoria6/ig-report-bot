from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = ''
password = ''
victim = ''

browser = webdriver.Firefox(executable_path='D:\GitHub\ig-report-bot\geckodriver.exe')
browser.get('https://www.instagram.com/')

time.sleep(5)

## Login into instagram account
txtUser = browser.find_element_by_name('username')
txtUser.send_keys(username)
txtPass = browser.find_element_by_name('password')
txtPass.send_keys(password)
btnLogin = browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
btnLogin.click()

## Shearch and report victim
time.sleep(3)
browser.get('https://www.instagram.com/'+victim)
btnOptions = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/button')
btnOptions.click()
btnReport = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div/button[3]')
btnReport.click()

time.sleep(3)
btnInapropiado = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]')
btnInapropiado.click()

time.sleep(3)
btnReportAccount = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]')
btnReportAccount.click()


time.sleep(3)
btnOtherPeople = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[3]/button[2]')
btnOtherPeople.click()


time.sleep(3)
btnAlguienConocido = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/fieldset/div[2]/label/div')
btnAlguienConocido.click()

btnSendReport = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div/div/div[6]/button').click()


time.sleep(3)
browser.quit()