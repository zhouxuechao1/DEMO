import allure

import pytest


@allure.epic("登录需求一")
@allure.feature("功能模块一")
class TestAllure:
    @allure.story("子功能一")
    @allure.title("测试参数{param1}+{param2}={expected}")
    @pytest.mark.parametrize("param1, param2, expected", [(1, 2, 3), (3, 3, 6)])
    def test_parametr_and_title(self, param1, param2, expected):
        """
        测试参数相加
        :param param1:
        :param param2:
        :param expected:
        :return:
        """
        assert param1 + param2 == expected

    @allure.story("子功能二")
    @allure.link('https://ceshiren.com/t/topic/15860', name='这是测试用例链接')
    def test_link(self):
        """
        测试链接
        :return:
        """
        assert 3 + 3 == 6

    testlink = 'https://ceshiren.com/t/topic/15860'

    @allure.story("子功能三")
    @allure.link(testlink, name='这是另一个可连接')
    def test_link2(self):
        pass

    @allure.story("子功能一")
    @allure.testcase(testlink, '用例管理系统')
    def test_casesysteam(self):
        pass

    @allure.story("子功能二")
    @allure.issue('15860', 'bug管理系统')
    def test_issue(self):
        pass


@allure.epic("登录需求一")
@allure.feature("功能模块二")
class TestAllure2:

    @allure.story("子功能四")
    def test_case1(self):
        print('功能点1')

    @allure.story("子功能五")
    @allure.title("测试子功能：{a},{b} 之和")
    @pytest.mark.parametrize('a, b, c', [(1, 2, 3), (4, 5, 6)])
    def test_case2(self, a, b, c):
        assert a + b == c
