import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

test_data = [["https://pajis.archeo.ru/v022020r.html#rge022020", "2020", "2"],
             ["https://pajis.archeo.ru/v012022r.html#rshum012022", "2022", "1"]]


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize("old_url, year, number", test_data)
def test_old_url_opens_correct_magazine_page(browser, old_url, year, number):
    browser.get(old_url)
    actual_magazine_name = browser.find_element(By.CSS_SELECTOR, "h2.page__title").text.lower()
    # проверяем, что страница загрузилась
    assert actual_magazine_name is not None, "Страница не загрузилась"
    expected_magazine_name = f"первобытная археология. журнал междисциплинарных исследований, {year}, №{number}"
    # проверяем, что ссылка ведёт на нужную страницу
    assert expected_magazine_name == actual_magazine_name, "Ссылка ведёт на другой журнал"
