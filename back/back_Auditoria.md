| Carpeta     | Responsabilidad           |
| ----------- | ------------------------- |
| `auth`      | Login / register / logout |
| `users`     | Datos del usuario         |
| `expenses`  | Gastos                    |
| `incomes`   | Ingresos                  |
| `budgets`   | Presupuestos              |
| `stats`     | Estadísticas              |
| `messages`  | Frases                    |
| `dashboard` | Resumen general           |

---

📘 AUDITORÍA DEL BACKEND — ÍNDICE FUNCIONAL
📁 /backend

Responsabilidad:
Raíz del backend. Contiene configuración global, arranque de la app y dependencias.

app.py

Punto de entrada de Flask.

Crea la aplicación.

Registra todos los Blueprints.

Define el entorno (debug).

No contiene lógica de negocio.

config.py

Centraliza configuración global.

Credenciales de DB.

Claves de sesión.

No debe tener lógica.

requirements.txt

Dependencias del backend.

Controla el entorno de ejecución.

Debe mantenerse mínimo y limpio.

📁 /db

Responsabilidad:
Acceso único y controlado a la base de datos.

db/**init**.py

Marca la carpeta como paquete.

No contiene lógica.

db/connection.py

Crea conexiones MySQL.

Único punto autorizado de conexión a DB.

Facilita cambiar DB en el futuro.

Nunca ejecuta consultas.

📁 /auth

Responsabilidad:
Autenticación y sesiones.

auth/**init**.py

Inicializa el módulo.

Sin lógica.

auth/routes.py

Endpoints de login y registro.

Maneja requests HTTP.

Gestiona sesión (session["user_id"]).

No contiene SQL.

auth/services.py

Verifica credenciales.

Registra usuarios.

Llama a DB.

Aplica hashing de contraseñas.

No devuelve respuestas HTTP.

📁 /users

Responsabilidad:
Gestión del usuario autenticado.

users/**init**.py

Inicialización del módulo.

users/routes.py

Endpoints:

Obtener perfil

Actualizar perfil

Eliminar cuenta

Requiere login.

No contiene SQL.

users/services.py

Consultas a tabla users.

Actualización y borrado de usuario.

No gestiona sesiones.

📁 /categories

Responsabilidad:
Gestión de categorías personalizadas.

categories/**init**.py

Inicializa el módulo.

categories/routes.py

Crear categorías.

Asociadas al usuario.

Requiere login.

No contiene lógica compleja.

categories/services.py

Inserción en DB.

Asegura relación usuario–categoría.

No maneja HTTP.

📁 /expenses

Responsabilidad:
Gestión de gastos.

expenses/**init**.py

Inicializa módulo.

expenses/routes.py

Crear gastos.

Validación básica.

Requiere login.

No contiene SQL.

expenses/services.py

Inserción de gastos.

Lógica de negocio (importe, fechas).

Acceso a DB.

No conoce el contexto HTTP.

📁 /incomes

Responsabilidad:
Gestión de ingresos.

incomes/**init**.py

Inicializa módulo.

incomes/routes.py

Crear ingresos.

Requiere login.

No ejecuta consultas.

incomes/services.py

Inserción en DB.

Lógica asociada a ingresos.

No maneja sesión.

📁 /budgets

Responsabilidad:
Gestión de presupuestos.

budgets/**init**.py

Inicializa módulo.

budgets/routes.py

Crear y listar presupuestos.

Requiere login.

No contiene lógica de cálculo.

budgets/services.py

Inserta y obtiene presupuestos.

Relación categoría–usuario.

No compara gastos (aún).

📁 /dashboard

Responsabilidad:
Resumen general del usuario.

dashboard/**init**.py

Inicializa módulo.

dashboard/routes.py

Endpoints de resumen (saldo).

Requiere login.

No calcula directamente.

dashboard/services.py

Calcula saldo total.

Combina ingresos y gastos.

No genera gráficos.

📁 /stats

Responsabilidad:
Estadísticas y datos para gráficos.

stats/**init**.py

Inicializa módulo.

stats/routes.py

Endpoints JSON para frontend.

Parámetros de fecha.

Requiere login.

No contiene SQL.

stats/services.py

Consultas agregadas (SUM, GROUP BY).

Datos para Chart.js.

No guarda resultados.

📁 /messages

Responsabilidad:
Mensajes motivacionales y educativos.

messages/**init**.py

Inicializa módulo.

messages/routes.py

Endpoint para obtener mensaje aleatorio.

Público (opcional).

No escribe DB.

messages/services.py

Recupera mensajes de DB.

Selección aleatoria.

No conoce usuarios.

📁 /utils

Responsabilidad:
Funciones transversales reutilizables.

utils/**init**.py

Inicializa módulo.

utils/auth.py

Hash y verificación de contraseñas.

No gestiona sesiones.

utils/decorators.py

Decoradores comunes.

Protección de rutas (login_required).

No contiene lógica de negocio.

🧠 RESUMEN EJECUTIVO (importante)

✔ Arquitectura modular
✔ Separación clara de responsabilidades
✔ Fácil de mantener y escalar
✔ Ideal para aprendizaje y producción
✔ Backend “clean”

👉 Esta estructura ya es defendible en una entrevista técnica.

🚀 Próximos pasos naturales

Middleware de errores

Validaciones con schemas

Tests unitarios

JWT

Docker
