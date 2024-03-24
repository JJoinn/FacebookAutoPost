from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pynput.keyboard import Controller, Key
import time
import pyperclip

def post_to_group(driver, group_id):
    # 等待一段时间，确保页面加载完全
    time.sleep(15)
    driver.get("https://www.facebook.com/groups/" + group_id)
    print("https://www.facebook.com/groups/" + group_id)
    time.sleep(3)

    write_button = driver.find_element("xpath", "//div[@class='x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
    ActionChains(driver).click(write_button).perform()
    print(write_button.text)
    time.sleep(3)

    element = driver.find_element("xpath", "//div[@data-contents]")
    element.send_keys("Now accepting advance booking BOOK YOUR TRIP NOW")

    time.sleep(3)
    post_button = driver.find_element("xpath", "//div[@aria-label='Photo/video']")
    ActionChains(driver).click(post_button).perform()

    time.sleep(3)
    pyperclip.copy('"1.jpg" "2.jpg" "3.jpg" "4.jpg" ')
    upload = driver.find_element("xpath", "//div[@class='x9f619 x1n2onr6 x1ja2u2z xlhe6ec x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xiba41w xkjf3g4 xbwy6ji']")
    ActionChains(driver).click(upload).perform()
    time.sleep(3)
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(10)
    post_button = driver.find_element("xpath", "//div[@aria-label='Post']")
    ActionChains(driver).click(post_button).perform()
    print("https://www.facebook.com/groups/" + group_id + "，发布完毕")
    

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
driver= webdriver.Chrome(options)

# 打开网页
driver.get("https://www.facebook.com/?stype=lo&deoia=1&jlou=Afc4F3_2iiBdsSAva165h8CcvzMo7kj3_ZotiLEdBrBL123xCzby8fPHn4lfKRHOugSBsGVOvNGZJrnj88RK5JvjDw4LLGsbwpBm2OlJ42wTPA&smuh=33353&lh=Ac-ViRUd9IRWeWvVT2c")

# 填写用户名和密码 登录
login_button = driver.find_element(By.NAME, "login")
username_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "pass")

username_input.send_keys("username")
password_input.send_keys("password")
password_input.send_keys(Keys.RETURN)

numbers = [
    "970877753563461", "3120657818004722", "2784391981672627", "647341186396105", 
    "819958535140042", "2335390943397180", "662196807148039", "1423187475142922", 
    "203719533560875", "225347694604553", "483035240115412", "1402246150202786", 
    "364677711287952", "901538320223067", "1959791800789766", "2328834007380378", 
    "2243676262334122", "298941651225083", "229502214381615", "1293072794831885", 
    "357364656259027", "3137102572998910", "979641949281586", "938892053392152", 
    "2150208801960620", "RentACarRentAVanCarServiceAndVanServiceWithDriver", 
    "4766883030072172", "497331794224719", "213431029991180", "837895933738441", 
    "2378365439147258", "3347453155291577", "437195209966854", "470291574040074", 
    "826340601578884", "2205903666156796", "692193321467690", "324597439618621", 
    "2340388709546151", "362406514275869", "373084149991305", "308669567235683", 
    "676360701159558", "801473400002696", "373900100459829", "285169913035885", 
    "409528346154515", "595011088394909", "523109594988636", "2112671922141256", 
    "219260422805092", "676480876654109", "1667295116903863", "condo.foreigner", 
    "2451149121808033", "277368616911113", "472107707839115", "2330484337163538", 
    "511601943465466"
]

time.sleep(15)
# 跳转小组页面
for number in numbers:
    post_to_group(driver, number)

# 关闭浏览器
driver.quit()
