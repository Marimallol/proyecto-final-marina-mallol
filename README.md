# Proyecto Final — Marina Mallol

Proyecto de automatización de pruebas desarrollado en Python para validar
interfaces web, servicios API y componentes del framework. Su objetivo es
organizar escenarios reproducibles y generar evidencias de sus resultados.

Las pruebas de interfaz utilizan [SauceDemo](https://www.saucedemo.com), una
aplicación de demostración de comercio electrónico. Las pruebas API utilizan
[JSONPlaceholder](https://jsonplaceholder.typicode.com), un servicio de datos
ficticios que simula las operaciones de escritura.

## Tecnologías

Python, pytest, Selenium WebDriver, Requests y pytest-html. El proyecto incluye
un workflow de GitHub Actions preparado para la ejecución automatizada.

## Alcance de las pruebas

La suite contiene **14 casos: 8 de interfaz, 3 de API y 3 unitarios**.

| Área | Escenarios |
|---|---|
| Autenticación | Inicio de sesión válido, usuario bloqueado, credenciales incorrectas y usuario vacío |
| Carrito | Agregar un producto, verificar su presencia y eliminarlo |
| Inventario | Ordenamiento de precios ascendente y descendente |
| Compra | Flujo completo desde la selección del producto hasta la confirmación del pedido |
| API | Consulta de un post existente, respuesta 404 para uno inexistente y creación simulada de un post |
| Unitarias | Configuración, validación de timeout y comportamiento del cliente HTTP |

## Organización y diseño

El framework aplica **Page Object Model** para separar las interacciones con
las páginas de las aserciones de los tests. Utiliza datos de login en CSV,
configuración mediante variables de entorno y fixtures para gestionar el
navegador y las sesiones HTTP.

| Carpeta | Contenido |
|---|---|
| `src\qa_automation` | Configuración, cliente API, navegador y Page Objects |
| `tests` | Pruebas UI, API y unitarias |
| `data` | Datos de prueba |
| `reports` | Reportes, logs y capturas |
| `.github\workflows` | Workflow de integración continua |

## Reportes

Cada ejecución genera un reporte HTML con el estado y la duración de las pruebas,
además de un log de ejecución. Los fallos durante la ejecución de pruebas UI
generan capturas de pantalla que se incorporan al reporte.

El proyecto reúne automatización de navegador, validación HTTP y pruebas aisladas
en una estructura modular orientada al mantenimiento y la ampliación de escenarios.
