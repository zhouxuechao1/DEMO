from typing import List

import pytest


@pytest.fixture(autouse=False)
def login():
    print("\n先执行登录操作")
    yield
    print("执行登出操作")

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")



def pytest_configure(config):
    marker_list = ['search', 'login']
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
