@echo off

rem Inicia el servidor de desarrollo en segundo plano
start /B python C:\Users\anton\OneDrive\Documentos\GitHub\WebPublicidad\manage.py runserver

rem Espera unos segundos para que el servidor inicie completamente
timeout /t 5 > nul

rem Ejecuta las pruebas
python C:\Users\anton\OneDrive\Escritorio\WebPublicidad\manage.py test

rem Cierra el servidor después de que las pruebas terminen
taskkill /f /im python.exe
