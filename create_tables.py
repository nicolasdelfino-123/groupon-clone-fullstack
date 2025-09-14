#!/usr/bin/env python3
"""
Script para crear todas las tablas en la base de datos de producción (Neon)
Ejecuta este script para inicializar la base de datos.
"""

import os
from src.app import app, db
from src.api.models import *
from src.api.services import inicializar_servicios

def create_tables():
    """Crear todas las tablas y datos iniciales"""
    print("🗄️ Creando todas las tablas...")
    
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        print("✅ Tablas creadas exitosamente!")
        
        # Inicializar servicios (datos de prueba)
        print("📊 Iniciando servicios y datos de prueba...")
        inicializar_servicios()
        print("✅ Datos iniciales creados!")
        
        print("\n🚀 ¡Base de datos lista para producción!")

if __name__ == "__main__":
    # Usar la URL de producción de Neon
    os.environ['DATABASE_URL'] = input("Ingresa la URL de tu base de datos Neon: ").strip()
    create_tables()
