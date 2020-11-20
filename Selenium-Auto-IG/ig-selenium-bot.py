from selenium import webdriver
from time import sleep
import id_pass


# *******************************************************************************
# Complete the function unfollow_non_followers
# *******************************************************************************


# Starting the Chrome Web Driver
driver = webdriver.Chrome(executable_path="C:/Users/samso/Documents/chromedriver_win32/chromedriver")
driver.get("https://www.instagram.com/")
sleep(4)


# initial IG Login
def login_ready():
  driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys((id_pass.username))
  driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys((id_pass.password))
  driver.find_element_by_xpath("//button[@type=\"submit\"]")\
    .click()
  sleep(5)
  driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
    .click()
  sleep(4)
  driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
    .click()
  sleep(4)


# Starts Auto-Follow from Home Page
def auto_follow():
  i=0
  while i<2:
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button/div')\
      .click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button/div')\
      .click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button/div')\
      .click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[4]/div[3]/button/div')\
      .click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[5]/div[3]/button/div')\
      .click()
    sleep(2)

    i+=1
    driver.refresh()
    sleep(3)

def analyze_non_followers():
  # fetch the list from instabot.
  pass

def unfollow_non_followers():
  driver.get("https://www.instagram.com/kindsam47/")
  sleep(3)
  driver.find_element_by_partial_link_text("following")\
    .click()

  no_of_people_unfollowed=0
  last_height = driver.execute_script("return document.body.scrollHeight")
  while no_of_people_unfollowed<=5:
    driver.find_element_by_xpath("//button[text()='Following']")\
      .click()
    driver.find_element_by_xpath("//button[text()='Unfollow']")\
      .click()

    # driver.find_element_by_xpath("//div[normalize-space()='Following']")

    no_of_people_unfollowed+=1
    if no_of_people_unfollowed%3==0:
      sleep(2)
    else:
      sleep(1)
    
    # to perform Scroll down on application using Selenium
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
      break
    last_height = new_height



# Close and Quit the Driver
def close_driver():
  driver.close()
  sleep(2)
  driver.quit()


# Function Calls
login_ready()
# auto_follow()
unfollow_non_followers()



# close_driver()