import allure
import pytest
# from pytest_bdd.parser import Step

from common.Browser import REMOTE

default_browser = "chrome"


def pytest_addoption(parser):
    parser.addoption("--browser", default='',
                     choices=sorted(REMOTE.BROWSERS),
                     help="run tests only for given browser")
    parser.addoption("--driver-path", default='',
                     type=str,
                     help="the driver binary path of browser")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser") or default_browser


@pytest.fixture(scope="session", autouse=True)
def driver_bin(request):
    return request.config.getoption("--driver-path")


@pytest.fixture(scope="session", autouse=True)
def WebDriver():
    import os
    home = os.environ.get("HOME") or os.environ.get("HOMEPATH")
    os.environ['PATH'] = ''.join([os.environ['PATH'], ":", home, "/webdrivers"])

    def web_driver(br):
        return REMOTE.WEBDRIVERS[br.lower()]()
    return web_driver


def pytest_exception_interact(node, call, report):
    try:
        # print("node: {}".format(node))
        # print("call: {}".format(call))
        # print("report: {}".format(report))
        # print(f"hasattr: {hasattr(node.instance, 'driver')}")
        if getattr(node.instance, 'driver'):
            driver = node.instance.driver
            allure.attach(driver.get_screenshot_as_png(), 'Fail screenshot', allure.attachment_type.PNG)
            driver.quit()
    except AttributeError:
        pass


def pytest_sessionfinish(session, exitstatus):
    pass


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    # pytest_bdd.hooks.pytest_bdd_step_error
    # print(step)
    # print(step_func)
    # print(step_func_args)
    if "driver" in step_func_args:
        step_driver = step_func_args['driver']
        allure.attach(step_driver.get_screenshot_as_png(), step.name, allure.attachment_type.PNG)
        print("attach")
        # # step error钩子driver不需要退出，在定义driver fixture出退出即可
        # step_driver.quit()


def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
    """Called when step lookup failed."""
    # print(scenario.steps)
    # print(scenario.steps[-1])
    # print(step.name)

    # lookup_step = Step()
    # scenario.add_step(lookup_step)
    pass


def pytest_bdd_before_scenario(request, feature, scenario):
    # pytest_bdd.parser.Scenario
    pass


def _inject_fixture(request, arg, value):
    """Inject fixture into pytest fixture request.

    :param request: pytest fixture request
    :param arg: argument name
    :param value: argument value
    """

    from _pytest.fixtures import FixtureDef
    fd = FixtureDef(
        fixturemanager=request._fixturemanager,
        baseid=None,
        argname=arg,
        func=lambda: value,
        scope="function",
        params=None,
    )
    fd.cached_result = (value, 0, None)

    old_fd = request._fixture_defs.get(arg)
    add_fixturename = arg not in request.fixturenames

    def fin():
        request._fixturemanager._arg2fixturedefs[arg].remove(fd)
        request._fixture_defs[arg] = old_fd

        if add_fixturename:
            request._pyfuncitem._fixtureinfo.names_closure.remove(arg)

    request.addfinalizer(fin)

    # inject fixture definition
    request._fixturemanager._arg2fixturedefs.setdefault(arg, []).insert(0, fd)
    # inject fixture value in request cache
    request._fixture_defs[arg] = fd
    if add_fixturename:
        request._pyfuncitem._fixtureinfo.names_closure.append(arg)