import pytest


class TestMark:

    @pytest.mark.xfail
    def test_case1(self):
        print("***start test***")
        a = 1
        assert a == 2

    xfail = pytest.mark.xfail

    def test_case2(self):
        print('***开始测试***')
        pytest.xfail(reason='改功能尚未完成')
        print('test way')
        assert 1 == 1


if __name__ == '__main__':
    pytest.main()
