from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

'''
Conexión a MySQL, se usa en todas las rutas
'''
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Contabilidad123$",
        database="contabilidad"
    )

'''
Login simple sin seguridad avanzada,
devuelve user_id y el frontend lo guarda y lo manda en cada request.
'''
# Registro
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO usuarios (usuario, email, password) VALUES (%s, %s, %s)",
        (data["usuario"], data["email"], data["password"])
    )

    db.commit()
    return jsonify({"message": "Usuario creado"})

# Login
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM usuarios WHERE email=%s AND password=%s",
        (data["email"], data["password"])
    )

    user = cursor.fetchone()

    if not user:
        return jsonify({"error": "Credenciales incorrectas"}), 401

    return jsonify({"usuario_id": user["id"]})

'''
Ingresos
'''
# Añadir ingreso
@app.route("/ingresos", methods=["POST"])
def add_ingreso():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO ingresos (cantidad, date, nota, categoria_id, usuario_id)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            data["cantidad"],
            data["date"],
            data.get("nota"),
            data["categoria_id"],
            data["usuario_id"]
        )
    )

    db.commit()
    return jsonify({"message": "Ingreso añadido"})

# Historial de ingresos
@app.route("/ingresos/<int:usuario_id>")
def get_ingresos(usuario_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM ingresos WHERE usuario_id=%s ORDER BY date DESC",
        (usuario_id,)
    )

    return jsonify(cursor.fetchall())

'''
Gastos
'''
# Añadir gasto
@app.route("/gastos", methods=["POST"])
def add_gasto():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO gastos (cantidad, date, nota, categoria_id, usuario_id)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            data["cantidad"],
            data["date"],
            data.get("nota"),
            data["categoria_id"],
            data["usuario_id"]
        )
    )

    db.commit()
    return jsonify({"message": "Gasto añadido"})

# Historial de gastos
@app.route("/gastos/<int:usuario_id>")
def get_gastos(usuario_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM gastos WHERE usuario_id=%s ORDER BY date DESC",
        (usuario_id,)
    )

    return jsonify(cursor.fetchall())

'''
DASHBOARD (saldo y resumen)
'''
@app.route("/dashboard/<int:usuario_id>")
def dashboard(usuario_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT SUM(cantidad) FROM ingresos WHERE usuario_id=%s",
        (usuario_id,)
    )
    total_ingresos = cursor.fetchone()[0] or 0

    cursor.execute(
        "SELECT SUM(cantidad) FROM gastos WHERE usuario_id=%s",
        (usuario_id,)
    )
    total_gastos = cursor.fetchone()[0] or 0

    saldo = total_ingresos - total_gastos

    return jsonify({
        "ingresos": total_ingresos,
        "gastos": total_gastos,
        "saldo": saldo
    })

'''
PRESUPUESTOS
'''
@app.route("/presupuesto", methods=["POST"])
def set_presupuesto():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO presupuestos (cantidad, periodo, usuario_id)
        VALUES (%s, %s, %s)
        """,
        (data["cantidad"], data["periodo"], data["usuario_id"])
    )

    db.commit()
    return jsonify({"message": "Presupuesto guardado"})

'''
ESTADÍSTICAS
'''
@app.route("/stats/gastos/<int:usuario_id>")
def stats_gastos(usuario_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT c.nombre AS categoria, SUM(g.cantidad) AS total
        FROM gastos g
        JOIN categorias c ON g.categoria_id = c.id
        WHERE g.usuario_id=%s
        GROUP BY c.nombre
    """, (usuario_id,))

    return jsonify(cursor.fetchall())

'''
INICIAR EL SERVIDOR
'''
if __name__ == "__main__":
    app.run(debug=True)
