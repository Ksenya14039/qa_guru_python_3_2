from selene.support.shared import browser
from selene import be, have

def test_google_positive_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_google_negative_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('kneqnjnineqtnijpxaoscko').press_enter()
    browser.element('[id="res"]').should(have.text('По запросу kneqnjnineqtnijpxaoscko ничего не найдено'))