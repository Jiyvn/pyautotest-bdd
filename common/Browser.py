import platform
from selenium import webdriver
import os

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class REMOTE:
    PLATFORM = platform.system().lower()
    PLATFORM_OS = "windows" if PLATFORM.startswith('windows') else "mac" if PLATFORM.startswith('darwin') else 'linux'
    PC_PLATFORM = ("windows", "mac", "linux")
    MOBILE_PLATFORM = ("ios", "android")
    BROWSERS = ("chrome", "firefox", "safari", "ie", "edge")
    BROWSER_OPTIONS = {
        'chrome': webdriver.ChromeOptions(),
        'firefox': webdriver.FirefoxOptions(),
        'ie': webdriver.IeOptions()
    }

    WEBDRIVERS = {
        'chrome': webdriver.Chrome,
        'firefox': webdriver.Firefox,
        'ie': webdriver.Ie,
        'edge': webdriver.Edge,
        'safari': webdriver.Safari
    }

    WEBDRIVER_BIN = {
        'chrome': str(PATH('WebDrivers/chromedriver.exe')),
        'firefox': str(PATH('WebDrivers/geckodriver.exe')),
        'ie': str(PATH('WebDrivers/IEDriverServer.exe')),
        'edge': str(PATH('WebDrivers/MicrosoftWebDriver.exe')),
        'safari': "",
    }
    DEFAULT_DRIVER = {
        'chrome': "chromedriver",
        'firefox': "geckodriver",
        'ie': 'IEDriverServer.exe',
        'edge': 'MicrosoftWebDriver.exe',
        'safari': "/usr/bin/safaridriver"
    }


