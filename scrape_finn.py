from selenium import webdriver
import time
import csv
import datetime

url = "https://www.finn.no/effekt/221719465/sammendrag?token=tcX08wsK1CwM6c84Qqa0KTY1q3JcljplLRsa4pxIyqs&expiry=1655113455&finnMail=effect-documentation_realestate"
csv_file = 'scrape_results.csv'

driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
time.sleep(5)

print(datetime.datetime.now())
epost = driver.find_elements_by_xpath(
    '//*[@id="sammendrag-panel"]/div[1]/section/div/div[1]/span/strong')[0].text
favoritt = driver.find_elements_by_xpath(
    '//*[@id="sammendrag-panel"]/div[1]/section/div/div[2]/span/strong')[0].text
oppgave = driver.find_elements_by_xpath(
    '//*[@id="sammendrag-panel"]/div[1]/section/div/div[3]/span/strong')[0].text
visning = driver.find_elements_by_xpath(
    '//*[@id="sammendrag-panel"]/div[1]/section/div/div[4]/span/strong')[0].text
print(epost, favoritt, oppgave, visning)
klikk = driver.find_elements_by_xpath(
    '//*[@id="sammendrag-panel"]/div[1]/div[1]/div/p/strong')[0].text
print(klikk)
besokende = driver.find_elements_by_xpath(
    '//*[@id="sammendrag-panel"]/div[2]/section/div/div[1]/strong')[0].text
print(besokende)
engang = driver.find_elements_by_xpath(
    '//*[@id="sammendrag-panel"]/div[2]/section/div/div[2]/div[1]/div/strong')[0].text
totilfem = driver.find_elements_by_xpath(
    '//*[@id="sammendrag-panel"]/div[2]/section/div/div[2]/div[2]/div/strong')[0].text
merennfem = driver.find_elements_by_xpath(
    '//*[@id="sammendrag-panel"]/div[2]/section/div/div[2]/div[3]/div/strong')[0].text
print(engang, totilfem, merennfem)

time.sleep(5)
driver.close()

row = [datetime.datetime.now(), epost, favoritt, oppgave, visning, klikk,
       besokende, engang, totilfem, merennfem]

with open(csv_file, 'a', newline='') as fd:
    writer = csv.writer(fd)
    writer.writerow(row)
