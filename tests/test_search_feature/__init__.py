from functools import partial

import pytest

from .. import Scenario

scenario = partial(
    Scenario,
    feature_name="search.feature",
)


@pytest.fixture(autouse=True, scope='module')
def driver(browser, WebDriver):
    """
    will create a new driver for every scenario - test_xxx.py
    scope='module': driver will quit after executing every scenario - test_xxx.py
    scope='session': drivers will quit simultaneously after executing all scenarios - all test_xxs.py
    :return:
    """
    driver = WebDriver(browser)
    yield driver
    # # 使用yield：step error会先执行，然后再执行下面语句
    # # step error钩子不能退出driver，否则同一个模块其他scenario无法使用
    driver.quit()
