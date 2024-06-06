from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pynput.keyboard import Controller, Key
import time
import pyperclip

def post_to_group(driver, group_id):
    try:
        # 等待一段时间，确保页面加载完全
        time.sleep(15)
        driver.get("https://www.facebook.com/groups/" + str(group_id))
        print("https://www.facebook.com/groups/" + str(group_id))
        time.sleep(3)

        # 发帖按钮
        write_button = driver.find_element("xpath", "//div[@class='x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")
        ActionChains(driver).click(write_button).perform()
        print(write_button.text)
        
        #Tag
        time.sleep(3)
        tag_button = driver.find_element("xpath", "//div[@aria-label='Tag people']")
        tag_button.click()
        time.sleep(3)
        tag_button = driver.find_element("xpath", "//input[@aria-label='Search for people']")
        tag_button.send_keys("Elmie Canales")
        time.sleep(3)
        tag_button = driver.find_element("id", "100002572328514")
        tag_button.click()
        tag_button = driver.find_element("xpath", "//div[@aria-label='Back']")
        tag_button.click()
        
        
        # 上传图片视频
        time.sleep(3)
        pyperclip.copy('"1.jpg" "2.jpg" "3.jpg" "4.jpg" ')
        pv_button = driver.find_element("xpath", "//div[@aria-label='Photo/video']")
        pv_button.click()
        time.sleep(3)
        #upload = driver.find_element("xpath", "//div[@class='x9f619 x1n2onr6 x1ja2u2z xlhe6ec x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xiba41w xkjf3g4 xbwy6ji']")
        #ActionChains(driver).click(upload).perform()
        #time.sleep(3)
        keyboard = Controller()
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.release('v') 
        keyboard.release(Key.ctrl)
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        # 评论区域
        time.sleep(3)
        max_attempts = 10
        wait_time = 3  # 等待时间（秒）

        # 开始循环直到找到元素或达到最大尝试次数
        for attempt in range(max_attempts):
            try:
                # 尝试查找元素
                element = driver.find_element("xpath", "//div[@data-contents]")
                # 如果找到了元素，跳出循环
                break
            except NoSuchElementException:
                # 如果找不到元素，则打印提示信息并等待一段时间后继续循环
                print("Element not found. Retrying...")
                time.sleep(wait_time)
        else:
            # 如果达到最大尝试次数仍未找到元素，打印错误信息
            print("Element not found after {} attempts.".format(max_attempts))
            element = None
        element.send_keys("Now accepting advance bookings! Secure your trip now!")
        keyboard.press(Key.enter)
        element.send_keys("https://www.facebook.com/profile.php?id=61557435454422")
        keyboard.press(Key.enter)
        existing_html = element.get_attribute("innerHTML")
        additional_html = '<span start="3" end="16" class="xv78j7m" data-offset-key="ft1nn-1-0" spellcheck="false"><span data-offset-key="ft1nn-1-0"><span data-text="true">Elmie Canales</span></span></span>'
        new_html = existing_html + additional_html
        driver.execute_script("arguments[0].innerHTML = arguments[1];", element, new_html)


        # 发布按钮
        time.sleep(10)
        post_button = driver.find_element("xpath", "//div[@aria-label='Post']")
        ActionChains(driver).click(post_button).perform()
        print("https://www.facebook.com/groups/" + str(group_id) + "，发布完毕")
    except Exception as e:
        print("An exception occurred:", str(e))

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

username_input.send_keys("账号")
password_input.send_keys("密码")
password_input.send_keys(Keys.RETURN)

numbers = [
    使用read.py读取脸书全部群组的html,获取小组ID数组
]

time.sleep(15)
# 跳转小组页面
for number in numbers:
    post_to_group(driver, number)

# 关闭浏览器
driver.quit()
