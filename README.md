# Proyecto Final — Marina Mallol

Este proyecto forma parte de mi proyecto de entrega para el curso de automatización de pruebas. Está desarrollado en Python y tiene como objetivo practicar la comprobación de una tienda web de demostración, un servicio API y algunas funciones del propio proyecto mediante pruebas automáticas.

Las pruebas de interfaz utilizan [SauceDemo](https://www.saucedemo.com), una web de demostración de comercio electrónico. Las pruebas API utilizan [JSONPlaceholder](https://jsonplaceholder.typicode.com), un servicio con datos ficticios.

## Tecnologías

Python, pytest, Selenium WebDriver, Requests y pytest-html. El proyecto también incluye una configuración de GitHub Actions para ejecutar las pruebas automáticamente.

## Alcance de las pruebas

La suite contiene **17 pruebas: 10 de interfaz, 3 de API y 4 unitarias**.

| Área | Escenarios |
|---|---|
| Autenticación | Inicio de sesión correcto y comprobación de errores con usuario bloqueado, credenciales incorrectas o usuario vacío |
| Carrito | Añadir un producto, comprobar su presencia, verificar un carrito vacío y eliminarlo |
| Inventario | Ordenar los productos por precio de menor a mayor y de mayor a menor |
| Compra | Completar una compra y comprobar el mensaje de confirmación; verificar el error cuando falta el nombre |
| API | Consultar un post existente, comprobar la respuesta para uno inexistente y crear un post de prueba |
| Unitarias | Comprobar la configuración y el funcionamiento del cliente API, incluido el comportamiento ante un timeout |

## Organización y diseño

El proyecto utiliza **Page Object Model** para separar las acciones realizadas en las páginas de las comprobaciones de las pruebas. Los datos de inicio de sesión se guardan en un archivo CSV y se usan fixtures para preparar el navegador y las conexiones HTTP.

| Carpeta | Contenido |
|---|---|
| `src/qa_automation` | Configuración, cliente API, navegador y Page Objects |
| `tests` | Pruebas de interfaz, API y unitarias |
| `data` | Datos de prueba |
| `reports` | Reportes, registros y evidencias |
| `.github/workflows` | Configuración para ejecutar las pruebas automáticamente |

## Instalación y ejecución

Necesitas tener Python instalado. Desde la carpeta del proyecto, instala las dependencias y ejecuta todas las pruebas:

```bash
python -m pip install -r requirements.txt
pytest
```

Para ejecutar solamente las pruebas de interfaz:

```bash
pytest tests/ui
```

Las pruebas de interfaz requieren Chrome instalado. En GitHub Actions se ejecutan en modo sin ventana.

## Reportes y evidencias

Cada ejecución genera un reporte HTML en `reports/report.html` y un registro en `reports/pytest.log`. Si falla una prueba de interfaz, se guarda una captura de pantalla, la dirección de la página y una copia de su HTML en `reports/diagnostics/`. El reporte HTML también incluye la captura cuando se puede obtener.

El proyecto reúne pruebas de navegador, comprobaciones de servicios API y pruebas unitarias en una estructura organizada para practicar y ampliar la automatización.
