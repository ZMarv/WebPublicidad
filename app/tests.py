import time
from django.test import TestCase

# Create your tests here.
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions

# class TestHomePage(LiveServerTestCase):

#     def setUp(self):
#         options = ChromeOptions()
#         options.headless = True  # Ejecuta el navegador en modo headless (sin interfaz gráfica)
#         self.selenium = webdriver.Chrome(service=ChromeService(executable_path=r'C:\Users\anton\OneDrive\Escritorio\chrome-win64\chrome.exe'), options=options)
#         self.selenium.implicitly_wait(10)

#     def test_home_page_title(self):
#         self.selenium.get(self.live_server_url)
#         print("Page title:", self.selenium.title)
#         self.assertEqual(self.selenium.title, 'Mercado Adds')

#     def tearDown(self):
#         self.selenium.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

# Configura Selenium para usar el navegador Chrome
driver = webdriver.Chrome()

try:
    # Abre la página web
    driver.get("http://127.0.0.1:8000/")

    # Espera hasta que el formulario esté presente y visible
    form_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "contactoForm"))
    )

    # Llena el formulario
    nombre_apellido = driver.find_element(By.ID, "nombreApellido")
    nombre_apellido.send_keys("Nombre Apellido")

    telefono = driver.find_element(By.ID, "telefono")
    telefono.send_keys("123456789")

    correo = driver.find_element(By.ID, "correo")
    correo.send_keys("correo@example.com")

    empresa = driver.find_element(By.ID, "empresa")
    empresa.send_keys("Nombre de la Empresa")

    mensaje = driver.find_element(By.ID, "mensaje")
    mensaje.send_keys("Este es un mensaje de prueba")

    # Función para intentar hacer clic en el botón de enviar
    def click_enviar():
        try:
            enviar_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "enviarBtn"))
            )
            enviar_btn.click()
            return True
        except ElementClickInterceptedException:
            return False

    # Intentar hacer clic en el botón de enviar con un máximo de 3 intentos
    attempts = 0
    while attempts < 3:
        if click_enviar():
            break
        attempts += 1
        time.sleep(1)  # Espera antes de reintentar

    # Esperar a que la página cambie de URL después de enviar el formulario
    try:
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    except TimeoutException:
        print("Timeout waiting for URL change after clicking enviarBtn")
        # You can choose to handle this error gracefully or raise it

    # Puedes añadir aquí más validaciones o acciones después de enviar el formulario si es necesario

finally:
    # Cierra el navegador al finalizar
    driver.quit()
