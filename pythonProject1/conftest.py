import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def browser():
    """
    Фикстура для запуска и управления экземпляром браузера Chromium.
    Returns:
        Browser: Экземпляр браузера Playwright для использования в тестах
    Raises:
        pytest.fail: В случае ошибки инициализации браузера
    """
    try:
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        yield browser
    except Exception as er:
        pytest.fail(f'Произошла ошибка: {er}')
    finally:
        browser.close()
        playwright.stop()
