import time
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

# Create your tests here.

# Configura Selenium para usar el navegador Chrome
driver = webdriver.Chrome()

try:
    # Abre la página web
    driver.get("http://127.0.0.1:8000/")

    # Espera hasta que el formulario esté presente y visible
    form_element = WebDriverWait(driver, 6).until(
        EC.visibility_of_element_located((By.ID, "contactoForm"))
    )

    # Llena el formulario
    nombre_apellido = driver.find_element(By.ID, "nombreApellido")
    nombre_apellido.send_keys("John Doe")

    telefono = driver.find_element(By.ID, "telefono")
    telefono.send_keys("+569 1204 7854")

    correo = driver.find_element(By.ID, "correo")
    correo.send_keys("johndoe03@gmail.com")



    empresa = driver.find_element(By.ID, "empresa")
    empresa.send_keys("Flex Pe")

    mensaje = driver.find_element(By.ID, "mensaje")
    mensaje.send_keys("Me gustaría información sobre los planes y si hay alguna otra oferta.")

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

finally:
    # Cierra el navegador al finalizar
    driver.quit()
