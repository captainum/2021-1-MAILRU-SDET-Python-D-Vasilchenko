import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.dashboard_page import DashboardPage

class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request:FixtureRequest):
        self.driver = driver

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.dashboard_page: DashboardPage = request.getfixturevalue('dashboard_page')