from flask import Blueprint, jsonify, request
from .models import db, Viajes, Ofertas, Belleza, Gastronomia, Top, User, NewsletterSubscriptions
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask_bcrypt import Bcrypt
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

# Obtener todas las ofertas
@api.route('/ofertas', methods=['GET'])
def obtener_ofertas():
    try:
        ofertas = Ofertas.query.all()
        ofertas_serializadas = [oferta.serialize() for oferta in ofertas]
        return jsonify({"ofertas": ofertas_serializadas}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

# Error handlers para el Blueprint
@api.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Ruta no encontrada"}), 404

@api.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Error interno del servidor"}), 500

# Health check para pruebas
@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "API funcionando correctamente"}), 200

# Registro de usuarios
@api.route('/registro', methods=['POST'])
def crear_usuario():
    try:
        # Imprimir información de depuración detallada
        print("\n==== DATOS DE LA SOLICITUD DE REGISTRO ====")
        print(f"Método: {request.method}")
        print(f"Content-Type: {request.headers.get('Content-Type')}")
        
        # Intentar obtener datos como JSON y mostrar versión segura (sin password)
        try:
            data = request.get_json(force=True)
            datos_seguros = {k: v if k != 'password' else '*****' for k, v in data.items()}
            print(f"Datos parseados como JSON: {datos_seguros}")
        except Exception as e:
            print(f"Error al parsear JSON: {e}")
            return jsonify({"error": f"Error al procesar datos: {str(e)}"}), 400
        
        # Extraer y validar campos obligatorios
        print("Procesando campos...")
        
        # Campos principales - validación exhaustiva
        campos_obligatorios = ['nombre', 'apellido', 'correo', 'password']
        for campo in campos_obligatorios:
            valor = data.get(campo)
            tipo = type(valor).__name__
            valor_mostrado = '*****' if campo == 'password' and valor else valor
            print(f"{campo}: '{valor_mostrado}' (tipo: {tipo})")
            
            if valor is None or valor == '':
                print(f"ERROR: El campo '{campo}' está vacío o no fue enviado")
                return jsonify({"error": f"El campo {campo} es obligatorio"}), 400
        
        nombre = data.get('nombre')
        apellido = data.get('apellido')
        correo = data.get('correo')
        password = data.get('password')
            
        # Verificar si el usuario ya existe
        usuario_existente = User.query.filter_by(correo=correo).first()
        if usuario_existente:
            print(f"Usuario ya existe: {correo}")
            return jsonify({"error": "El usuario ya existe"}), 409

        # Extraer campos opcionales con valores por defecto
        telefono = data.get('telefono', '')
        direccion = data.get('direccion_line1', data.get('direccion', ''))
        ciudad = data.get('ciudad', '')
        role = data.get('role', 'cliente')

        print(f"Campos opcionales: telefono='{telefono}', direccion='{direccion}', ciudad='{ciudad}', role='{role}'")

        # Hash de contraseña
        from flask_bcrypt import Bcrypt
        bcrypt = Bcrypt()
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        print("Creando nuevo usuario...")
        nuevo_usuario = User(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            password=pw_hash,
            telefono=telefono,
            direccion_line1=direccion,
            ciudad=ciudad,
            role=role,
            is_active=True
        )
        
        # Guardar en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()
        print(f"Usuario creado con éxito: ID={nuevo_usuario.id}, correo={correo}")
        
        # Respuesta exitosa
        return jsonify({
            "mensaje": "Usuario creado correctamente",
            "user": {
                "id": nuevo_usuario.id,
                "nombre": nuevo_usuario.nombre,
                "apellido": nuevo_usuario.apellido,
                "correo": nuevo_usuario.correo,
                "role": nuevo_usuario.role
            }
        }), 201
        
    except Exception as e:
        print(f"ERROR CRÍTICO EN REGISTRO: {str(e)}")
        import traceback
        traceback.print_exc()
        db.session.rollback()
        return jsonify({"error": f"Error del servidor: {str(e)}"}), 500

# Login de usuarios
@api.route('/login', methods=['POST'])
def iniciar_sesion():
    try:
        print("\n==== INTENTO DE LOGIN ====")
        
        # Validar formato de los datos
        if not request.is_json:
            print("ERROR: No es JSON")
            return jsonify({"error": "Se esperaba formato JSON"}), 400
            
        data = request.get_json()
        print(f"Datos recibidos: {data}")
        
        # Validar campos requeridos
        correo = data.get('correo')
        contraseña = data.get('password')
        
        if not correo or not contraseña:
            print("ERROR: Faltan correo o contraseña")
            return jsonify({"error": "Correo y contraseña son obligatorios"}), 400
        
        # Buscar usuario
        print(f"Buscando usuario con correo: {correo}")
        usuario = User.query.filter_by(correo=correo).first()
        
        if not usuario:
            print(f"ERROR: Usuario no encontrado con correo {correo}")
            return jsonify({"error": "Correo o contraseña incorrectos"}), 401
        
        print(f"Usuario encontrado: ID={usuario.id}, Nombre={usuario.nombre}")
        
        # Verificar contraseña
        from flask_bcrypt import Bcrypt
        bcrypt = Bcrypt()
        if not bcrypt.check_password_hash(usuario.password, contraseña):
            print("ERROR: Contraseña incorrecta")
            return jsonify({"error": "Correo o contraseña incorrectos"}), 401
        
        # Generar token
        print("Inicio de sesión exitoso - Generando token")
        from flask_jwt_extended import create_access_token
        access_token = create_access_token(identity=usuario.correo)
        
        print(f"Token generado para usuario {usuario.correo}")
        print(f"Rol del usuario: {usuario.role}")
        
        return jsonify({
            "mensaje": f"Bienvenido, {usuario.nombre} {usuario.apellido}",
            "access_token": access_token,
            "user_id": usuario.id,
            "user": {
                "id": usuario.id,
                "correo": usuario.correo,
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "role": usuario.role,
                "activo": usuario.is_active,
                "telefono": usuario.telefono,
                "direccion1": usuario.direccion_line1,
                "direccion2": usuario.direccion_line2,
                "ciudad": usuario.ciudad,
                "pais": usuario.pais
            }
        }), 200
    
    except Exception as e:
        print(f"ERROR EN LOGIN: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Error del servidor: {str(e)}"}), 500

# Verificar token
@api.route('/verify-token', methods=['GET'])
@jwt_required()
def verificar_token():
    usuario = get_jwt_identity()
    return jsonify({"user": usuario, "valid": True}), 200

# Newsletter suscripción
@api.route('/newsletter', methods=['POST'])
def agregar_a_newsletter():
    data = request.get_json()
    email = data.get('correo')

    if not email:
        return jsonify({"error": "Correo es obligatorio"}), 400

    sub = NewsletterSubscriptions.query.filter_by(correo=email).first()

    if sub:
        return jsonify({"error": "Usted ya esta suscrito a nuestro newsletter"}), 404

    sub = NewsletterSubscriptions(
        correo = email
    )

    db.session.add(sub)
    db.session.commit()

    # Envío de confirmación...
    return jsonify({"mensaje": "Suscripción exitosa"}), 201
