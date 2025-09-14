from flask import Blueprint, jsonify
from .models import Viajes, Ofertas, Belleza, Gastronomia, Top, User
from flask_jwt_extended import jwt_required, get_jwt_identity
import traceback

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return {"message": "API funcionando correctamente"}

@api.route('/hello', methods=['GET'])
def hello():
    try:
        # Verificar conexión a la base de datos
        user_count = User.query.count()
        return jsonify({
            "message": "Hello! API conectada correctamente", 
            "users_count": user_count
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Database connection failed",
            "details": str(e)
        }), 500

@api.route('/viajes', methods=['GET'])
def obtener_viajes():
    try:
        viajes_items = Viajes.query.order_by(Viajes.id.asc()).all()
        viajes_serializados = [viaje.serialize() for viaje in viajes_items]

        return jsonify({
            "success": True,
            "count": len(viajes_serializados),
            "viajes": viajes_serializados
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Error al obtener viajes",
            "details": str(e)
        }), 500

@api.route('/ofertas', methods=['GET'])
def obtener_ofertas():
    try:
        ofertas_items = Ofertas.query.order_by(Ofertas.id.asc()).all()
        ofertas_serializadas = [oferta.serialize() for oferta in ofertas_items]

        return jsonify({
            "success": True,
            "count": len(ofertas_serializadas),
            "ofertas": ofertas_serializadas
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Error al obtener ofertas", 
            "details": str(e)
        }), 500

@api.route('/belleza', methods=['GET'])
def obtener_belleza():
    try:
        belleza_items = Belleza.query.order_by(Belleza.id.asc()).all()
        belleza_serializada = [item.serialize() for item in belleza_items]

        return jsonify({
            "success": True,
            "count": len(belleza_serializada),
            "belleza": belleza_serializada
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Error al obtener servicios de belleza",
            "details": str(e)
        }), 500

@api.route('/gastronomia', methods=['GET'])
def obtener_gastronomia():
    try:
        gastronomia_items = Gastronomia.query.order_by(Gastronomia.id.asc()).all()
        gastronomia_serializada = [item.serialize() for item in gastronomia_items]

        return jsonify({
            "success": True,
            "count": len(gastronomia_serializada),
            "gastronomia": gastronomia_serializada
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Error al obtener servicios de gastronomía",
            "details": str(e)
        }), 500

@api.route('/top', methods=['GET'])
def obtener_top():
    try:
        top_items = Top.query.order_by(Top.id.asc()).all()
        top_serializado = [item.serialize() for item in top_items]

        return jsonify({
            "success": True,
            "count": len(top_serializado),
            "top": top_serializado
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Error al obtener top ofertas",
            "details": str(e)
        }), 500
