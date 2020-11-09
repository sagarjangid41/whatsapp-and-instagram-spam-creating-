import time
driver = webdriver.Chrome('D:/chromedriver.exe')
driver.get("https://www.instagram.com/")
driver.maximize_window()
# login
urname = input("enter Username")
username=driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
username.send_keys(urname)
pas=input("Enter Password")
driver.implicitly_wait(10)
passw=driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
passw.send_keys(pas)
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
# notification 
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
# search user
send=input("Enter name/id of receiver")
driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div").click()
search = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
search.send_keys(send)
# click on user

driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div").click()

# click on message
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button").click()
count=int(input("enter count"))
text =input("enter message") 
for i in range(count):
    mess = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    mess.send_keys(text)
    driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
