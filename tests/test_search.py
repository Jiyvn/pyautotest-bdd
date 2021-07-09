from functools import partial

from pytest_bdd import scenario, feature, cucumber_json, hooks
from steps.search import *
# from pytest_bdd.parser import Scenario

scenario = partial(scenario,  features_base_dir="./features")


@scenario(
        feature_name="search.feature",
        scenario_name="搜索pytest"
    )
def test_search():
    pass

@scenario(
        feature_name="search.feature",
        scenario_name="搜索2pytest"
    )
def test_search2():
    pass

