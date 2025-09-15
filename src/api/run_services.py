from api.models import db, User, Categoria
from api.services import inicializar_servicios
from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

with app.app_context():
    # Buscar el primer usuario (admin)
    user = User.query.filter_by(role='admin').first()
    if not user:
        print('No se encontró usuario admin. Ejecuta primero create_admin_user o crea el usuario manualmente.')
        exit(1)
    # Buscar las categorías por nombre
    def get_cat_id(nombre):
        cat = Categoria.query.filter_by(nombre=nombre).first()
        if not cat:
            print(f'No existe la categoría: {nombre}')
            exit(1)
        return cat.id
    viajes_category_id = get_cat_id('Viajes')
    top_category_id = get_cat_id('Top')
    belleza_category_id = get_cat_id('Belleza')
    gastronomia_category_id = get_cat_id('Gastronomia')
    ofertas_category_id = get_cat_id('Ofertas')
    # Inicializar servicios
    inicializar_servicios(user.id, viajes_category_id, top_category_id, belleza_category_id, gastronomia_category_id, ofertas_category_id)
    print('¡Servicios inicializados correctamente!')
