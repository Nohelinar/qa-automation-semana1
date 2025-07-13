# Proyecto QA Automation – Semana 1

Este repositorio contiene mis primeras pruebas automatizadas usando **Python**, **Selenium** y **PyTest**.  
La estructura sigue el patrón **Page Object Model (POM)** para mantener el código ordenado y reutilizable.

---

## 📂 Estructura del proyecto

```plaintext
Automation/
├── pages/
│   └── login_page.py       # Funciones para interactuar con la página
├── tests/
│   └── test_login.py       # Tests automatizados para login
├── conftest.py             # Configuración de fixtures (setup y teardown)
├── requirements.txt        # Dependencias necesarias
├── README.md               # Documentación del proyecto
├── testenv/                # Entorno virtual (ignorarlo en Git)
└── .pytest_cache/          # Cache de Pytest (ignorar en Git)
```

---

##  ¿Cómo empezar?

1. Cloná este repositorio o descargá los archivos.

2. Activá tu entorno virtual (opcional pero recomendado):

```bash
python -m venv testenv
source testenv/bin/activate   # Linux/Mac
testenv\Scripts\activate    # Windows
```

3. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecutar los tests

Desde la raíz del proyecto, ejecutá:

```bash
pytest
```

Pytest va a detectar automáticamente los tests en la carpeta `tests` y correrlos.

---

## Detalles importantes

- Se utiliza **Page Object Model (POM)** para separar la lógica de interacción con la web de los tests.
- El archivo `conftest.py` contiene fixtures que preparan y limpian el navegador antes y después de cada test.
- Los tests cubren casos de login exitoso, usuario inválido y contraseña inválida.
- Usamos **WebDriver Manager** para manejar el driver de Chrome automáticamente.

---

## Tecnologías usadas

- Python  
- Selenium  
- Pytest  
- WebDriver Manager  

---

## Contribuciones

Este proyecto es una práctica personal, pero cualquier sugerencia o mejora es bienvenida.  
Hacé un pull request si querés aportar.
