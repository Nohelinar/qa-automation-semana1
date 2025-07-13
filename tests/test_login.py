from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import time

def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("student", "Password123")

    assert "logged-in-successfully" in driver.current_url

    message = driver.find_element(By.TAG_NAME, "h1").text
    assert "Logged In Successfully" in message

    logout_button = driver.find_element(By.LINK_TEXT, "Log out")
    assert logout_button.is_displayed()

    time.sleep(2)

def test_login_username_invalido(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("usuarioIncorrecto", "Password123")

    wait = WebDriverWait(driver, 10)
    error_element = wait.until(EC.visibility_of_element_located((By.ID, "error")))
    error_message = error_element.text

    assert error_message == "Your username is invalid!"

    time.sleep(2)

def test_login_password_invalida(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("student", "contraseñaIncorrecta")

    wait = WebDriverWait(driver, 10)
    error_element = wait.until(EC.visibility_of_element_located((By.ID, "error")))
    error_message = error_element.text

    assert error_message == "Your password is invalid!"

    time.sleep(2)

