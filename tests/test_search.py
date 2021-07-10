from functools import partial

import pytest
from pytest_bdd import scenario, feature, cucumber_json, hooks

from common.Browser import REMOTE
from conftest import default_browser
from steps.search import *
# from pytest_bdd.parser import Scenario

scenario = partial(scenario,
                   feature_name="search.feature",
                   features_base_dir="./features")


@pytest.fixture(autouse=True, scope='module')
def driver(browser, WebDriver):
    driver = WebDriver(browser)
    yield driver
    driver.quit()


@scenario(
        scenario_name="搜索pytest"
    )
def test_search():
    pass


@scenario(
        scenario_name="搜索2pytest"
    )
def test_search2():
    pass

