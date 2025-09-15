# src/app.py
import os
import traceback
from decimal import Decimal
from datetime import date, datetime

from flask import Flask, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, inspect

from api.services import inicializar_servicios

app = Flask(__name__)

# --- DB CONFIG: Neon si está DATABASE_URL, sino SQLite en /tmp ---
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL  # ej: ...?sslmode=require
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/app.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# --- Helpers JSON seguros (Decimal/datetime) ---
def _to_json_safe(val):
    if isinstance(val, Decimal):
        return float(val)
    if isinstance(val, (datetime, date)):
        return val.isoformat()
    return val

def rows_to_dicts(rows, columns):
    out = []
    for r in rows:
        item = {}
        # soporta RowMapping y tuplas
        if hasattr(r, "_mapping"):
            for k in r._mapping.keys():
                item[str(k)] = _to_json_safe(r._mapping[k])
        else:
            for idx, col in enumerate(columns):
                item[col] = _to_json_safe(r[idx])
        out.append(item)
    return out

# --- Blueprint /api ---
api_bp = Blueprint("api", __name__)

@api_bp.get("/health")
def health():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@api_bp.get("/viajes")
def get_viajes():
    try:
        sql = text("""SELECT id,title as nombre,descripcion as description,price as original_price,discountPrice as discounted_price,
                      image,city as location,rating,reviews,buyers,user_id
                      FROM viajes ORDER BY id DESC""")
        rows = db.session.execute(sql).fetchall()
        return jsonify({"viajes": rows_to_dicts(rows, [])})
    except Exception as e:
        return jsonify({"viajes": [], "error": str(e)})

@api_bp.get("/ofertas")
def get_ofertas():
    try:
        sql = text("""SELECT id,title as nombre,descripcion as description,price as original_price,discountPrice as discounted_price,
                      image,city as location,rating,reviews,buyers,user_id
                      FROM ofertas ORDER BY id DESC""")
        rows = db.session.execute(sql).fetchall()
        return jsonify({"ofertas": rows_to_dicts(rows, [])})
    except Exception as e:
        return jsonify({"ofertas": [], "error": str(e)})

@api_bp.get("/gastronomia")
def get_gastro():
    try:
        sql = text("""SELECT id,title as nombre,descripcion as description,price as original_price,discountPrice as discounted_price,
                      image,city as location,rating,reviews,buyers,user_id
                      FROM gastronomia ORDER BY id DESC""")
        rows = db.session.execute(sql).fetchall()
        return jsonify({"gastronomia": rows_to_dicts(rows, [])})
    except Exception as e:
        return jsonify({"gastronomia": [], "error": str(e)})

@api_bp.get("/belleza")
def get_belleza():
    try:
        sql = text("""SELECT id,title as nombre,descripcion as description,price as original_price,discountPrice as discounted_price,
                      image,city as location,rating,reviews,buyers,user_id
                      FROM belleza ORDER BY id DESC""")
        rows = db.session.execute(sql).fetchall()
        return jsonify({"belleza": rows_to_dicts(rows, [])})
    except Exception as e:
        return jsonify({"belleza": [], "error": str(e)})

@api_bp.get("/top")
def get_top():
    try:
        sql = text("""SELECT id,title as nombre,descripcion as description,price as original_price,discountPrice as discounted_price,
                      image,city as location,rating,reviews,buyers,user_id
                      FROM top ORDER BY id DESC""")
        rows = db.session.execute(sql).fetchall()
        return jsonify({"top": rows_to_dicts(rows, [])})
    except Exception as e:
        return jsonify({"top": [], "error": str(e)})

@api_bp.get("/hello")
def hello():
    return jsonify({"message": "Hello from the API!"})

app.register_blueprint(api_bp, url_prefix="/api")

# --- Handler global de errores: siempre JSON, y log en consola ---
@app.errorhandler(Exception)
def handle_any_error(e):
    print("UNHANDLED EXCEPTION:", e)
    traceback.print_exc()
    return jsonify({"error": "server_error", "message": str(e)}), 500

# --- Ruta raíz para SPA ---
@app.route('/')
def serve_spa():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def serve_spa_routes(path):
    # Si es un archivo estático, servirlo
    if '.' in path:
        return app.send_static_file(path)
    # Si no, servir el SPA
    return app.send_static_file('index.html')

# --- Poblar BD si está vacía (solo si no hay servicios) ---
def poblar_si_vacia():
    try:
        inspector = inspect(db.engine)
        # Verifica si existen datos en la tabla 'viajes'
        viajes_count = db.session.execute(text('SELECT COUNT(*) FROM viajes')).scalar()
        if viajes_count == 0:
            # Buscar IDs
            user_id = db.session.execute(text("SELECT id FROM user WHERE role='admin' LIMIT 1")).scalar()
            viajes_category_id = db.session.execute(text("SELECT id FROM categoria WHERE nombre='Viajes' LIMIT 1")).scalar()
            top_category_id = db.session.execute(text("SELECT id FROM categoria WHERE nombre='Top' LIMIT 1")).scalar()
            belleza_category_id = db.session.execute(text("SELECT id FROM categoria WHERE nombre='Belleza' LIMIT 1")).scalar()
            gastronomia_category_id = db.session.execute(text("SELECT id FROM categoria WHERE nombre='Gastronomia' LIMIT 1")).scalar()
            ofertas_category_id = db.session.execute(text("SELECT id FROM categoria WHERE nombre='Ofertas' LIMIT 1")).scalar()
            if None in [user_id, viajes_category_id, top_category_id, belleza_category_id, gastronomia_category_id, ofertas_category_id]:
                print("No se encontraron los IDs necesarios para poblar la BD. Skipping init.")
                return
            inicializar_servicios(user_id, viajes_category_id, top_category_id, belleza_category_id, gastronomia_category_id, ofertas_category_id)
            print("BD poblada automáticamente en el arranque.")
        else:
            print("La BD ya tiene servicios, no se puebla.")
    except Exception as e:
        print("Error al poblar la BD:", e)

# Ejecutar al iniciar la app
with app.app_context():
    poblar_si_vacia()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3001)
