from functools import partial
from pytest_bdd import scenario
# from pytest_bdd.parser import Scenario

Scenario = partial(
    scenario,
    features_base_dir="./features"
)