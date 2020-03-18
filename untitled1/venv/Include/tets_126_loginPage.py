# coding=utf-8
'''
Project:页面基本操作方法：如open，input_username，input_password，click_submit
'''
from selenium.webdriver.common.by import By
from test_basePage import BasePage

#继承BasePage类
class LoginPage(BasePage):
    #定位器，通过元素属性定位元素对象
    username_loc =(By.NAME,'email')
    password_loc =(By.NAME,'password')
    submit_loc =(By.ID,'dologin')
    error_loc =(By.XPATH,"//div[@class='ferrorhead']")
    userid_loc=(By.ID,"spnUid")
    frame_loc="x-URS-iframe"

    #操作
    #通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。

    #输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    #输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    #点击登录：调用click对象，点击登录
    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    #切换到用户登录框的iframe中
    def switch_to_frame(self):
        self.switch_frame(self.frame_loc)

    #用户名或密码不合理是Tip框内容展示
    def show_error(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.error_loc))
            return self.find_element(*self.error_loc).text
        except:
            return False

    #切换登录模式为动态密码登录（IE下有效）
    def swich_DynPw(self):
        self.find_element(*self.dynpw_loc).click()
    #登录成功后获取当前窗口的title
    def check_current_title(self):
        return self.driver.title

    #登录成功页面中的用户ID查找
    def show_userid(self):
        return self.find_element(*self.userid_loc).text