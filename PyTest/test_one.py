import pytest


# def setup_module():
#     print("模块级setup")
#
#
# def teardown_module():
#     print("模块级teardown"


class TestDay:

    # def setup_class(self):
    #     print("执行类级别setup")
    #
    # def teardown_class(self):
    #     print("执行类级别teardown")

    # def setup_method(self):
    #     print("setup_method")
    #
    # def teardown_method(self):
    #     print("teardown_method")

    # def setup(self):
    #     print("每次用例开始执行setup")
    #
    # def teardown(self):
    #     print("每次用例结束执行teardown")
    @pytest.fixture(name=login)
    def test_name(self):
        print("指定test_one方法调用")

    def test_one(self):
        print("开始执行 test_one 方法 ")
        a = 2
        b = 3
        assert a * b == 6

    def test_two(self):
        print("开始执行 test_two 方法")
        a = 6
        b = 3
        assert a / b == 2

    def test_three(self):
        print("开始执行 test_three 方法")
        a = 4
        b = 2
        assert a + b == 6


if __name__ == '__main__':
    pytest.main()
