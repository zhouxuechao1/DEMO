import pytest

# 测试用例名字
# 测试用例路径

@pytest.mark.parametrize("name", ["哈利", "赫敏", "琼文"])
def test_mm(name):
    print(f"name:{name}")

