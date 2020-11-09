from selenium import webdriver

driver = webdriver.Chrome('D:/chromedriver.exe')
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter name or group name:")
msg = input("Enter message:")
count = int(input("Enter count:"))

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
for index in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print("Success")
