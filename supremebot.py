from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time


while(True):
    now = datetime.now()
    currenttime = now.strftime("%H:%M:%S")
    droptime = "08:00:00" #change to your timezome's droptime
    time.sleep(1)
    if(currenttime >= droptime):
        driver = webdriver.Chrome()
        driver.get("https://us.supreme.com/collections/new")
        
        break
    else:
        print(currenttime)
        
# driver = webdriver.Chrome()
# driver.get("https://us.supreme.com/collections/new")

try:
    #enter the item after the CSS SELECTOR
    select = driver.find_element(By.CSS_SELECTOR, "img[alt='Polartec® Shearling Reversible Pullover - TrueTimber® HTC Fall Camo']")
    select.click()
    driver.implicitly_wait(2)

    size = driver.find_element(By.CSS_SELECTOR, "select[name='size']")
    selectsize = Select(size)
    selectsize.select_by_visible_text("Large") #choose your size
    cartbutton = driver.find_element(By.CSS_SELECTOR, "button[data-testid='add-to-cart-button']")
    cartbutton.click()
    driver.implicitly_wait(0.8)

    keepshoppingbutton = driver.find_element(By.CSS_SELECTOR, "a[data-testid='keep-shopping-link']")
    keepshoppingbutton.click()  

     
except:
    print("Checkout Failed")

# try:
#     #enter the item after the CSS SELECTOR
#     select = driver.find_element(By.CSS_SELECTOR, "img[alt='Supreme®/Jordan® Warm Up Jersey - Light Blue']")
#     select.click()
#     driver.implicitly_wait(2)

#     size = driver.find_element(By.CSS_SELECTOR, "select[name='size']")
#     selectsize = Select(size)
#     selectsize.select_by_visible_text("Large") #choose your size
#     cartbutton = driver.find_element(By.CSS_SELECTOR, "button[data-testid='add-to-cart-button']")
#     cartbutton.click()
#     driver.implicitly_wait(0.8)

#     keepshoppingbutton = driver.find_element(By.CSS_SELECTOR, "a[data-testid='keep-shopping-link']")
#     keepshoppingbutton.click()  

     
# except:
#     print("Checkout Failed")

# #if you want multiple items in a drop, copy and paste this code right below each time per item
# try:
#     viewall = driver.find_element(By.CSS_SELECTOR, "a[href='/collections/all']")
#     viewall.click()

#     select = driver.find_element(By.CSS_SELECTOR, "img[alt='Supreme®/Jordan® Biggie S/S Top - Black']")
#     select.click()
#     driver.implicitly_wait(2)

#     size = driver.find_element(By.CSS_SELECTOR, "select[name='size']")
#     selectsize = Select(size)
#     selectsize.select_by_visible_text("Large") #choose your size
#     cartbutton = driver.find_element(By.CSS_SELECTOR, "button[data-testid='add-to-cart-button']")
#     cartbutton.click()
#     driver.implicitly_wait(0.8)
# except:
#     print("Checkout Failed")


#Takes you to the cart, IF ANY INSTANCE OF FAILED APPEARS, RESTART IMMEDIATELY
try:
    checkoutbutton = driver.find_element(By.CSS_SELECTOR, "a[data-testid='mini-cart-checkout-link']")
    checkoutbutton.click()    
    print("Checkout Confirmed") 
except:
    print("Failed to checkout")
    time.sleep(5)

try:
    waitscreen = driver.find_element(By.CLASS_NAME, "XKMDH")
    if EC.presence_of_element_located(waitscreen):
        print("Success")
        waitforcheckout = WebDriverWait(driver, 300).until(EC.staleness_of(waitscreen))
    else:
        print("Failed")
except:
    print("Wait Failed")
    time.sleep(20)


    
#USER ENTRY FIELDS
try:
    email = driver.find_element(By.ID, "email") 
    driver.implicitly_wait(0.9)
    email.send_keys("tolonial1@gmail.com") #Enter inside quotations
    print("Email Entry Successful")

except:
    print("Email Entry Failed")
    time.sleep(1)

try:
    fname = driver.find_element(By.ID, "TextField0")
    fname.send_keys("Christian") #Enter inside quotations
    print("First Name Entry Successful")

except:
    print("First Name Entry Failed")
    time.sleep(1)

try:
    lname = driver.find_element(By.ID, "TextField1")
    lname.send_keys("Scott") #Enter inside quotations
    print("Last Name Entry Successful")

except:
    print("Last Name Entry Failed")
    time.sleep(1)

try:
    address = driver.find_element(By.ID, "shipping-address1")
    address.send_keys('9051 Montoya Street') #Enter inside quotations
    print("Address Entry Successful")

except:
    print("Address Entry Failed")
    time.sleep(1)

try:
    aptnum = driver.find_element(By.ID, "TextField2")
    aptnum.send_keys('4') #Enter inside quotations or leave blank
    print("Apt# Entry Successful")

except:
    print("Apt# Entry Failed")
    time.sleep(1)

try:
    city = driver.find_element(By.ID, "TextField3")
    city.send_keys("Sacramento") #Enter inside quotations
    print("City Entry Successful")

except:
    print("City Entry Failed")
    time.sleep(1)

try:
    postal = driver.find_element(By.ID, "TextField4")
    postal.send_keys("95826") #Enter inside quotations
    print("Post Code Entry Successful")

except:
    print("Post Code Entry Failed")
    time.sleep(1)

try:
    phone = driver.find_element(By.ID, "TextField5")
    phone.send_keys("8312973087") #Enter inside quotations
    print("Phone # Entry Sucessful")

except:
    print("Phone # Entry Failed")
    time.sleep(1)



#PAYMENT ENTRY FIELDS
  
try:
    
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'number')]")
    driver.switch_to.frame(iframe)
    cn = driver.find_element(By.ID, "number")
    cn.send_keys("5213071019314148") #Enter inside quotations
    print("Card Number Entry Successful")
    driver.switch_to.default_content()
    
except:
    print("Card Number Entry Failed")
    time.sleep(1)

try:
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'expiry')]")
    driver.switch_to.frame(iframe)
    exp = driver.find_element(By.ID, "expiry")
    #input the exp date in each indiviual send keys
    exp.send_keys("1")
    time.sleep(0.2)
    exp.send_keys("0")
    time.sleep(0.2)
    exp.send_keys("2")
    time.sleep(0.2)
    exp.send_keys("8")
    driver.switch_to.default_content()

except:
    print("Expiration Date Entry Failed")
    time.sleep(1)

try:
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'verification')]")
    driver.switch_to.frame(iframe)
    sec = driver.find_element(By.ID, "verification_value")
    sec.send_keys("843") #Enter inside quotations
    print("Security Code Entry Successful")
    driver.switch_to.default_content()

except:
    print("Security Code Entry Failed")
    time.sleep(1)

try:
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'name')]")
    driver.switch_to.frame(iframe)
    noc = driver.find_element(By.ID, "name")
    noc.send_keys("Christian Scott") #Enter inside quotations
    print("Name on Card Entry Succesful")
    driver.switch_to.default_content()
    
except:
    print("Name on Card Entry Failed")
    time.sleep(1)

try:
    pay = driver.find_element(By.ID, "checkout-pay-button")
    pay.click()
except:
    print("Failed to pay")

time.sleep(300)