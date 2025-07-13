import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Abre el navegador para el test
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver  # entrega el driver al test
    # Después del test, cierra el navegador
    driver.quit()
