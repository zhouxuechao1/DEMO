import pytest


"""yield关键字的用法，将测试方法执行前的准备和执行后的销毁"""
# @pytest.fixture(scope="class")
# def login():
#     print("先执行登录操作")
#     token = "andhh6787878bbcd"
#     yield token
#     print("再完成登出操作")


class TestShop:
    def test_search(self):
        a = 10
        print(f"搜索到物品需要{a}元")
