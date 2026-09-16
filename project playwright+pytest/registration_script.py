from playwright.sync_api import expect, sync_playwright

# Запускается Playwright и создаётся объект p, через который происходит работа с браузерами
with sync_playwright() as p:
    # Запуск браузера Chromium (в видимом режиме)
    browser = p.chromium.launch(headless=False)
    # После запуска браузера создаётся новая вкладка
    page = browser.new_page()

    # Открытие страницы по указанному адресу (page - это текущая вкладка браузера)
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    # page.locator(...) находит элемент на странице по локатору (находим поле email)
    # .fill(...) вводит текст в найденное поле (он не просто дописывает текст в конец поля, а очищает поле и записывает в него новое значение)
    page.locator("[data-testid='registration-form-email-input'] input").fill('user@example.com')
    # Находимо поле user и заполняем его testUser
    page.locator("[data-testid='registration-form-username-input'] input").fill('testUser')
    # Находимо поле password и заполняем его password123
    page.locator("[data-testid='registration-form-password-input'] input").fill('password123')
    # Клик по кнопке Registration для регистрации пользователя и перехода на другую страницу
    page.locator("[data-testid='registration-page-registration-button']").click()

    # Проверка, что выполнен переход на другую страницу (проверяем URL)
    expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    # Проверяем заголовок на новой странице
    dashboard_title = page.locator("[data-testid='dashboard-toolbar-title-text']")
    # Проверка на то, что заголовок отображается на странице
    expect(dashboard_title).to_be_visible()
    # Проверка текста заголовка
    expect(dashboard_title).to_have_text("Dashboard")

    # Для того чтобы задержать итоговую страницу для прочтения
    input("Нажмите Enter для завершения...")

   # После завершения работы браузер закрывается
    browser.close()