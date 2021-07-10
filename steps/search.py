from pytest_bdd import given, when, then, parsers
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from common.Browser import REMOTE


@given(parsers.parse("搜索词:{searchWord}"), target_fixture="word")
def word(searchWord):
    return dict(searchWord=searchWord)


# # https://pytest-bdd.readthedocs.io/en/stable/#override-fixtures-via-given-steps
@given(parsers.parse("浏览器:{br}"), target_fixture='driver')
# @given(parsers.parse("浏览器:{br}"))
def set_browser(br, WebDriver):
    return WebDriver(br.lower())


@when("打开百度，输入搜索词搜索")
def search_keyword(driver, word):
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(word['searchWord'])
    driver.find_element_by_id("su").click()
    import time
    time.sleep(2)

