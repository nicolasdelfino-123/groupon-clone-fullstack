#!/usr/bin/env python3
"""
Script simple para crear las tablas usando el SQL directo
"""

import psycopg2
import sys

# URL de la base de datos Neon
DATABASE_URL = "postgresql://neondb_owner:npg_jvRyU5bz2acJ@ep-rough-wildflower-ad63vfpv-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

def execute_sql_file():
    """Ejecutar el archivo database_setup.sql"""
    try:
        print("🔗 Conectando a Neon PostgreSQL...")
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        
        print("📂 Leyendo database_setup.sql...")
        with open('database_setup.sql', 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        print("🗄️ Ejecutando script SQL...")
        cursor.execute(sql_script)
        conn.commit()
        
        print("✅ ¡Todas las tablas creadas exitosamente!")
        print("🔍 Verificando tablas creadas...")
        
        cursor.execute("""
            SELECT table_name FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        """)
        
        tables = cursor.fetchall()
        print(f"\n📊 Tablas creadas ({len(tables)}):")
        for table in tables:
            print(f"  ✓ {table[0]}")
            
        cursor.close()
        conn.close()
        print("\n🚀 ¡Base de datos lista para producción!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    execute_sql_file()
