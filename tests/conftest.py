import pytest
from selene.support.shared import browser


@pytest.fixture
def browser_open():
    browser.config.window_height = 920
    browser.config.window_width = 1140
    browser.open('https://google.com')

    yield
    browser.element('[name="q"]').clear()