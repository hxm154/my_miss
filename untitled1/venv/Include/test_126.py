# -*- coding:utf8 -*-
'''
Project:使用unittest框架编写测试用例。
'''
import unittest,time
from test_126_loginPage import LoginPage
from selenium import webdriver

class Caselogin126mail(unittest.TestCase):
    """
          登录126邮箱的case
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url ="http://www.126.com"
        self.username ="zhpmiss@126.com"
        self.password ="zhou0829miss@"

    #用例执行体
    def test_login_mail(self):
        #声明LoginPage类对象
        login_page = LoginPage(self.driver, self.url, "网易")
        #调用打开页面组件
        login_page.open()
        #切换到登录框Frame
        time.sleep(4)
        login_page.switch_to_frame()
        #调用用户名输入组件
        login_page.input_username(self.username)
        #调用密码输入组件
        login_page.input_password(self.password)
        #调用点击登录按钮组件
        login_page.click_submit()
        if login_page.show_error():
            print("测试帐号密码有误的情况下是否弹出提示框：")
            self.assertEqual(login_page.show_error(),"帐号或密码错误")
        else:
            print("测试帐号密码正确的情况下是否进入确定页面：")
            self.assertEqual(login_page.show_userid(),'zhpmiss@126.com')
    def tearDown(self):
        print("测试完毕")
        #self.driver.quit()

if __name__ == "__main__":
    unittest.main()