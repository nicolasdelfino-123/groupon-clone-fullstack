
import click
from api.models import db, User
from flask_bcrypt import Bcrypt

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    bcrypt = Bcrypt(app)
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("insert-test-users") # name of our command
    @click.argument("count") # argument of out command
    def insert_test_users(count):
        print("Creating test users")
        for x in range(1, int(count) + 1):
            user = User()
            user.email = "test_user" + str(x) + "@test.com"
            user.password = "123456"
            user.is_active = True
            db.session.add(user)
            db.session.commit()
            print("User: ", user.email, " created.")

        print("All test users created")

    @app.cli.command("create-admin")
    def create_admin():
        """Crear o actualizar usuario administrador"""
        print("🔧 Creando/actualizando usuario administrador...")
        
        # Buscar si ya existe
        admin_user = User.query.filter_by(correo='admin@outlook.com').first()
        
        if admin_user:
            print("✅ Usuario admin encontrado, actualizando rol...")
            admin_user.role = 'admin'
            admin_user.activo = True
        else:
            print("➕ Creando nuevo usuario admin...")
            admin_user = User(
                correo='admin@outlook.com',
                nombre='Admin',
                apellido='Sistema',
                password=bcrypt.generate_password_hash('admin').decode('utf-8'),
                role='admin',
                activo=True,
                telefono='123456789',
                direccion1='Admin Address',
                ciudad='Admin City',
                pais='Admin Country'
            )
            db.session.add(admin_user)
        
        db.session.commit()
        print(f"✅ Usuario admin configurado correctamente:")
        print(f"   📧 Email: {admin_user.correo}")
        print(f"   🔑 Password: admin")
        print(f"   👤 Rol: {admin_user.role}")
        print(f"   ✅ Activo: {admin_user.activo}")

    @app.cli.command("insert-test-data")
    def insert_test_data():
        pass