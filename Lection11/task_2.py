# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()

"""Исходные данные для авторизации"""

base_url = 'https://fix-online.sbis.ru/'
login_standard_user = "Asafov"
password_all = "Asafov123"
dialog_url = 'https://fix-online.sbis.ru/page/dialogs'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)

try:

    user_name = driver.find_element(By.XPATH, "//input[@name='Login']").send_keys(login_standard_user)
    time.sleep(1)
    print("Логин введен")
    button_login = driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__checkSignInTypeButton"]')
    button_login.click()
    time.sleep(1)
    password = driver.find_element(By.XPATH, "//input[@name= 'Password']").send_keys(password_all)
    print("Input password")
    time.sleep(1)
    button_login2 = driver.find_element(By.CSS_SELECTOR, '[data-qa="auth-AdaptiveLoginForm__signInButton"]')
    button_login2.click()
    time.sleep(1)

    """Переходим в контакты"""

    contact_directory = driver.find_element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title')
    print(type(contact_directory))

    time.sleep(5)

    driver.get(dialog_url)
    print(driver.current_url)
    assert driver.current_url == dialog_url

    plus_dialog = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton')
    plus_dialog.click()
    time.sleep(2)

    search_string_dialog_form = driver.find_elements(By.CSS_SELECTOR, '[data-qa="controls-Render__field')
    print(type(search_string_dialog_form))
    print(search_string_dialog_form)
    print(len(search_string_dialog_form))
    print(search_string_dialog_form[0].text)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(search_string_dialog_form[0])
    action_chains.click(search_string_dialog_form[0])
    action_chains.send_keys('Асафов Саша')
    action_chains.perform()
    time.sleep(2)

    result_serching = driver.find_elements(By.CSS_SELECTOR, '.controls-padding_left-xs')
    print(len(result_serching))
    assert result_serching[0].text == 'Асафов Саша'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(result_serching[0])
    action_chains.click(result_serching[0])
    action_chains.perform()
    time.sleep(2)

    """Вводим текст в поле сообщения"""
    text_editor = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(text_editor)
    action_chains.click(text_editor)
    action_chains.send_keys('222')
    action_chains.perform()

    send_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(send_button)
    action_chains.click(send_button)

    action_chains.perform()

    time.sleep(2)

    """Проверяем, что сообщение ушло и отобразилось в реестре"""
    message_in_reestr = driver.find_elements(By.CSS_SELECTOR, '[data-qa="msg-dialogs-item__addressee')
    print(len(message_in_reestr))
    print(message_in_reestr[0].text)
    assert message_in_reestr[0].text == 'Асафов Саша'

    text_in_reestr = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__content-inner')
    len_message_in_reestr = len(text_in_reestr)
    print(type(text_in_reestr))
    print(len(text_in_reestr))
    print(text_in_reestr[0].text)
    assert text_in_reestr[0].text == '222'
    time.sleep(2)


    """Удаляем сообщение"""
    action_chains = ActionChains(driver)
    action_chains.move_to_element(text_in_reestr[0])
    action_chains.context_click(text_in_reestr[0])
    action_chains.perform()
    time.sleep(1)

    delete_button = driver.find_element(By.CSS_SELECTOR, '[data-target = "menu_item_deleteToArchive"]')
    print(delete_button.text)
    time.sleep(1)
    delete_button.click()
    time.sleep(1)

    len_message_in_reesr_after_deleting = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__content-inner')
    print(len(len_message_in_reesr_after_deleting))

    assert len(len_message_in_reesr_after_deleting) == len_message_in_reestr-1, 'сообщение не удалилось'  # Убеждаемся, что после удаления из реестра, длина списка сообщений равна длине списка сообщений -1 сообщений от момента, когда новое сообщение еще было в реестре

    print("ТЕСТ ПРОЙДЕН")

finally:
    driver.quit()

