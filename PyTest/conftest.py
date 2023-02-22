import pytest


@pytest.fixture(autouse=True)
def login():
    print("\n先执行登录操作")
    yield
    print("执行登出操作")


def pytest_configure(config):
    marker_list = ['search', 'login']
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
