import pytest


@pytest.fixture(name='')
def login():
    print("\n这是个登陆方法")


def pytest_configure(config):
    marker_list = ['search', 'login']
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
