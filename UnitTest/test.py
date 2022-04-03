"""
  @title: it's testcases
  @author: sonwc
  @create_time: 2021/8/8
  @update_time: ----
"""

from selenium import webdriver
import time
import unittest



class TestCase(unittest.TestCase):



    @classmethod
    def setUpClass(cls) -> None:   # Classmethod fixture
        print("类级别前置条件")
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.baidu.com")
        time.sleep(2)
        cls.title = None
        print(cls.title)


    @classmethod
    def tearDownClass(cls) -> None:
        print("类级别后置条件")
        # 输出用例002的值
        print(cls.title)
        cls.driver.quit()


    def test_001(self):
        self.driver.find_element_by_id("kw").send_keys("ui自动化")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        # 输出None
        print(self.title)
        TestCase.title = self.driver.title
        # 输出UI自动化
        print(self.title)
        self.assertEqual(self.title, "ui自动化_百度搜索", msg='断言失败')
        self.driver.find_element_by_id("kw").clear()


    def test_002(self):
        self.driver.find_element_by_id("kw").send_keys("接口自动化")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        print(self.title)  # 这里还是输出UI自动化, 用例与用例间关联参数
        TestCase.title = self.driver.title
        # 输出 接口自动化
        print(self.title)
        self.assertEqual(self.title, "接口自动化_百度搜索", msg='断言失败')



if __name__ == '__main__':
    unittest.main()
