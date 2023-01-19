from selene.support.conditions import be
from selene.support.jquery_style_selectors import s
from selene.support.shared import browser
from selene.support import by


def test_github():
    browser.open('https://github.com/')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('eroshenkoam/allure-example')
    s('.header-search-input').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()
    s(by.partial_text('#76')).should(be.visible)