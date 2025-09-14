# 🛍️ Groupon Clone - Plataforma de Ofertas y Servicios

Una aplicación web Full Stack empresarial inspirada en Groupon que permite a los usuarios descubrir y comprar servicios con descuentos especiales. Incluye **panel de administración completo**, **sistema de newsletters**, **pagos con Stripe** y **arquitectura escalable**.

![React](https://img.shields.io/badge/React-18.3.1-blue?logo=react&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-1.1.2-green?logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.6-purple?logo=bootstrap&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-Payment-blue?logo=stripe&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-orange?logo=jsonwebtokens&logoColor=white)
![React Admin](https://img.shields.io/badge/React_Admin-Dashboard-purple?logo=react&logoColor=white)

## 🚀 Características Principales

### 🛒 **Experiencia de Usuario Completa**
- **Exploración por categorías**: Belleza, Gastronomía, Viajes, Top Ofertas
- **Sistema de búsqueda avanzada** con filtros inteligentes y resultados instantáneos
- **Carrito de compras persistente** con almacenamiento local y sincronización
- **Pagos seguros** integrados con Stripe (test y producción)
- **Perfil de usuario personalizable** con historial de compras
- **Sistema de autenticación** robusto con JWT y roles de usuario

### 👨‍💼 **Panel de Administración Empresarial**
- **Dashboard React Admin** con métricas en tiempo real y análisis de ventas
- **Gestión CRUD completa** para todas las categorías de servicios
- **Sistema de newsletters** con editor visual y envío masivo
- **Gestión de usuarios** con roles y permisos granulares
- **Reportes de ventas** detallados por proveedor y categoría
- **Políticas y términos** configurables desde el panel

### 🔧 **Arquitectura Técnica Avanzada**
- **API RESTful** documentada con endpoints seguros
- **Autenticación JWT** con tokens de acceso y refresh
- **Base de datos relacional** optimizada con migraciones Alembic
- **Middleware CORS** configurado para desarrollo y producción
- **Variables de entorno** para configuración por ambiente
- **Sistema de logging** y manejo de errores centralizado

### 🎨 **Diseño y UX Profesional**
- **Diseño responsive** Mobile-First optimizado para todos los dispositivos
- **Interfaz moderna** con Bootstrap 5 y componentes personalizados
- **Navegación intuitiva** con breadcrumbs, filtros y paginación
- **Imágenes optimizadas** con lazy loading y fallbacks automáticos
- **Estados de carga** elegantes y manejo de errores UX-friendly
- **Accesibilidad WCAG** implementada para inclusión total

## 🛠️ Stack Tecnológico

### **Frontend - React Ecosystem**
- **React 18.3.1** - Biblioteca principal con Hooks y Context API
- **React Router 6.30.0** - Navegación SPA con lazy loading
- **Bootstrap 5.3.6** - Framework CSS responsivo y modular
- **React Bootstrap 2.10.10** - Componentes React/Bootstrap integrados
- **React Admin** - Dashboard administrativo con CRUD automático
- **Stripe React** - Integración de pagos segura y PCI-compliant
- **Context API + Flux Pattern** - Gestión de estado global escalable

### **Backend - Python Enterprise**
- **Flask 1.1.2** - Framework web ligero y extensible
- **SQLAlchemy** - ORM avanzado con lazy loading y relaciones
- **Flask-JWT-Extended** - Autenticación JWT con refresh tokens
- **Flask-CORS** - Configuración CORS para APIs seguras
- **Flask-Migrate + Alembic** - Sistema de migraciones versionado
- **Flask-Bcrypt** - Hashing seguro de contraseñas con salt
- **Stripe Python SDK** - Procesamiento de pagos y webhooks

### **Base de Datos y Persistencia**
- **PostgreSQL 16** - Base de datos relacional ACID-compliant
- **Alembic** - Migraciones automáticas y rollback
- **Connection Pooling** - Optimización de conexiones DB
- **Índices y Constraints** - Performance y integridad de datos

### **DevOps y Herramientas**
- **Webpack 5** - Bundling, code splitting y optimización
- **Babel** - Transpilación ES6+ con polyfills automáticos
- **ESLint + Prettier** - Linting y formateo de código
- **Pipenv** - Gestión de dependencias Python reproducible
- **Environment Variables** - Configuración por ambiente (.env)
- **Hot Module Replacement** - Desarrollo con recarga instantánea

## 📋 Requisitos del Sistema

Antes de comenzar, asegúrate de tener instalado:

- **Node.js** >= 14.0.0 (recomendado: 18.x LTS)
- **Python** >= 3.8.0 (recomendado: 3.11.x)
- **PostgreSQL** >= 12.0 (recomendado: 16.x)
- **Git** >= 2.20.0
- **NPM** >= 6.0.0 o **Yarn** >= 1.22.0

### **Verificación de Requisitos**
```bash
node --version    # v18.x.x
python3 --version # Python 3.11.x
psql --version    # psql (PostgreSQL) 16.x
git --version     # git version 2.x.x
```

## 🚀 Instalación y Configuración

### **1. Clonar el Repositorio**
```bash
git clone https://github.com/tuusuario/groupon-clone.git
cd groupon-clone/FullStack
```

### **2. Configurar Base de Datos PostgreSQL**
```bash
# Crear base de datos
sudo -u postgres psql
CREATE DATABASE example;
CREATE USER groupon_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE example TO groupon_user;
\q

# O usando createdb (alternativa)
createdb example
```

### **3. Configurar Variables de Entorno**
```bash
# Crear archivo de configuración
cp .env.example .env
```

Editar `.env` con tus configuraciones de producción:
```properties
# Base de datos PostgreSQL
DATABASE_URL=postgresql://postgres:TU_PASSWORD_SEGURA@localhost:5432/example

# Flask Security
FLASK_APP_KEY="clave_secreta_super_segura_para_produccion_256_bits"
FLASK_APP=src/app.py
FLASK_DEBUG=0  # Producción: 0, Desarrollo: 1

# Stripe (claves reales para producción)
STRIPE_SECRET_KEY=sk_live_tu_clave_secreta_stripe_real

# Gmail SMTP para notificaciones
GMAIL_USER=tu_email_empresarial@empresa.com
GMAIL_PASSWORD=tu_app_password_gmail

# URLs de aplicación
FRONT_END_URL=https://tu-dominio.com
BACKEND_URL=https://api.tu-dominio.com
BASENAME=/
```

### **4. Configurar Backend (Flask)**
```bash
# Activar entorno virtual Python
cd /ruta/al/proyecto && source .venv/bin/activate

# Instalar dependencias de producción
pip install -r requirements.txt

# Ejecutar migraciones de base de datos
flask db upgrade

# Crear usuario administrador
flask create-admin

# Opcional: Poblar con datos de prueba
flask insert-test-users 5
```

### **5. Configurar Frontend (React)**
```bash
# Instalar dependencias Node.js
npm install --production

# Optimizar para producción
npm run build  # Para producción
# npm start    # Para desarrollo
```

## 🏃‍♂️ Ejecutar el Proyecto

### **Desarrollo Local**

#### **Opción 1: Ejecución Manual**

##### Terminal 1 - Backend:
```bash
# Activar entorno virtual
cd /ruta/al/proyecto && source .venv/bin/activate
cd FullStack
python src/app.py
```
📡 **Backend disponible en**: `http://localhost:3001`

##### Terminal 2 - Frontend:
```bash
cd FullStack
npm start
```
🎨 **Frontend disponible en**: `http://localhost:3000`

#### **Opción 2: Script de Desarrollo Automatizado**
```bash
# Crear script de inicio para desarrollo
cat > start-dev.sh << 'EOF'
#!/bin/bash
echo "🚀 Iniciando Groupon Clone - Entorno de Desarrollo"

# Función de limpieza
cleanup() {
    echo "🛑 Deteniendo servicios..."
    pkill -f "python src/app.py" 2>/dev/null
    pkill -f "webpack-dev-server" 2>/dev/null
    exit 0
}
trap cleanup SIGINT

# Activar entorno virtual
source .venv/bin/activate

# Verificar dependencias
echo "🔍 Verificando dependencias..."
pip check && npm audit --audit-level=moderate

# Iniciar backend
echo "📡 Iniciando Backend Flask (Puerto 3001)..."
python src/app.py &
BACKEND_PID=$!

# Esperar inicialización del backend
sleep 5

# Verificar que el backend esté funcionando
if curl -f http://localhost:3001/test >/dev/null 2>&1; then
    echo "✅ Backend iniciado correctamente"
else
    echo "❌ Error: Backend no responde"
    exit 1
fi

# Iniciar frontend
echo "🎨 Iniciando Frontend React (Puerto 3000)..."
npm start &
FRONTEND_PID=$!

echo ""
echo "✅ 🎉 Aplicación iniciada correctamente:"
echo "   🔗 Frontend:     http://localhost:3000"
echo "   🔗 Backend API:  http://localhost:3001"
echo "   � Admin Panel:  http://localhost:3000/admin"
echo "   📧 Newsletter:   http://localhost:3000/newsletter"
echo ""
echo "👤 Credenciales de Admin:"
echo "   📧 Email: admin@outlook.com"
echo "   🔑 Password: admin"
echo ""
echo "⌨️  Presiona Ctrl+C para detener todos los servicios"

# Mantener script ejecutándose
wait
EOF

chmod +x start-dev.sh
./start-dev.sh
```

### **Producción**

#### **Usando PM2 (Recomendado)**
```bash
# Instalar PM2 globalmente
npm install -g pm2

# Configurar ecosystem para producción
cat > ecosystem.config.js << 'EOF'
module.exports = {
  apps: [
    {
      name: 'groupon-backend',
      script: 'src/app.py',
      interpreter: 'python3',
      cwd: './FullStack',
      env: {
        FLASK_DEBUG: 0,
        NODE_ENV: 'production'
      },
      error_file: './logs/backend-error.log',
      out_file: './logs/backend-out.log',
      log_file: './logs/backend-combined.log'
    }
  ]
};
EOF

# Iniciar aplicación
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

#### **Usando Docker (Alternativa)**
```bash
# Crear Dockerfile optimizado para producción
cat > Dockerfile << 'EOF'
FROM node:18-alpine AS frontend-build
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY --from=frontend-build /app/dist ./dist
EXPOSE 3001
CMD ["python", "src/app.py"]
EOF

# Build y run
docker build -t groupon-clone .
docker run -p 3001:3001 --env-file .env groupon-clone
```

## 💳 Integración Stripe - Datos de Prueba

### **✅ Tarjetas de Prueba Exitosas**
```
💳 Visa                 4242 4242 4242 4242
💳 Mastercard           5555 5555 5555 4444  
💳 American Express     3782 822463 10005
💳 Visa (debit)         4000 0566 5566 5556
💳 Mastercard (prepaid) 5555 5555 5555 4444
```

### **❌ Tarjetas de Prueba con Errores (para testing)**
```
🚫 Tarjeta declinada            4000 0000 0000 0002
🚫 Fondos insuficientes         4000 0000 0000 9995
🚫 CVC incorrecto               4000 0000 0000 0127
🚫 Tarjeta expirada             4000 0000 0000 0069
🚫 Procesamiento incorrecto     4000 0000 0000 0119
```

### **📋 Datos Adicionales para Testing**
```
📅 Fecha de vencimiento: Cualquier fecha futura (ej: 12/25, 01/30)
🔢 CVC:                 Cualquier 3 dígitos (ej: 123, 456)
📮 Código postal:       Cualquier código válido (ej: 12345, 28001)
👤 Nombre:              Cualquier nombre (ej: Juan Pérez)
```

### **🔧 Configuración Stripe**
- **Webhooks configurados** para confirmación de pagos
- **Modo sandbox** para desarrollo y testing
- **Validación PCI-compliant** implementada
- **Manejo de errores** robusto con retry automático
- **Logs de transacciones** para auditoría

## 👥 Credenciales de Acceso

### **🔐 Usuario Administrador**
```
📧 Email:    admin@outlook.com
🔑 Password: admin
👤 Rol:      Administrador completo
✅ Acceso:   Panel Admin + Newsletter + CRUD completo
```

### **👤 Usuario Cliente**
- Crear cuenta nueva desde el registro `/registro`
- **Rol**: Cliente estándar
- **Acceso**: Compras, perfil, historial

### **🛡️ Características de Seguridad**
- **Autenticación JWT** con tokens de acceso seguros
- **Hashing BCrypt** para contraseñas con salt automático
- **Validación de roles** en rutas protegidas
- **Middleware CORS** configurado para producción
- **Sanitización de inputs** en formularios
- **Rate limiting** implementado en endpoints críticos

## 📁 Estructura del Proyecto

```
FullStack/
├── 📁 src/                    # Backend Flask
│   ├── 📄 app.py             # Aplicación principal
│   ├── 📁 api/               # Lógica de la API
│   │   ├── 📄 models.py      # Modelos de base de datos
│   │   ├── 📄 routes.py      # Rutas de la API
│   │   ├── 📄 payment.py     # Integración Stripe
│   │   └── 📄 services.py    # Servicios de negocio
│   ├── 📁 front/             # Frontend React
│   │   ├── 📁 js/
│   │   │   ├── 📁 component/ # Componentes React
│   │   │   ├── 📁 pages/     # Páginas principales
│   │   │   └── 📁 store/     # Gestión de estado
│   │   └── 📁 styles/        # Estilos CSS
│   └── 📁 migrations/        # Migraciones de BD
├── 📄 package.json          # Dependencias Node.js
├── 📄 requirements.txt      # Dependencias Python
├── 📄 webpack.*.js          # Configuración Webpack
└── 📄 .env                  # Variables de entorno
```

## 🔧 Funcionalidades Detalladas

### **🛍️ Sistema de Compras**
- Carrito persistente con localStorage
- Checkout con múltiples elementos
- Integración completa con Stripe
- Confirmación por email (opcional)

### **🎨 Categorías de Servicios**
1. **💄 Belleza**: Spa, masajes, tratamientos
2. **🍽️ Gastronomía**: Restaurantes, experiencias culinarias
3. **✈️ Viajes**: Paquetes turísticos, aventuras
4. **⭐ Top Ofertas**: Servicios premium destacados
5. **🎯 Ofertas**: Descuentos especiales temporales

### **📧 Sistema de Newsletters**
- Creación de campañas personalizadas
- Selección de servicios específicos
- Envío masivo a suscriptores
- Plantillas responsive automáticas

### **🔐 Autenticación y Autorización**
- JWT tokens seguros
- Roles de usuario (Admin/Cliente)
- Protección de rutas sensibles
- Sesiones persistentes

## 🌐 API Documentation

### **🔑 Autenticación**
```http
POST /login                    # Inicio de sesión con JWT
POST /registro                 # Registro de nuevos usuarios  
PUT  /api/change-password      # Cambio de contraseña seguro
GET  /api/verify-token         # Verificación de token JWT
```

### **🛍️ Servicios y Categorías**
```http
GET  /viajes                   # Listar servicios de viajes
GET  /belleza                  # Listar servicios de belleza  
GET  /gastronomia             # Listar servicios de gastronomía
GET  /top                     # Listar top ofertas destacadas
GET  /ofertas                 # Listar ofertas especiales
GET  /categorias              # Listar todas las categorías
```

### **💳 Pagos y Transacciones**
```http
POST /create-checkout-session  # Crear sesión de pago Stripe
POST /webhook                  # Webhook confirmación Stripe
GET  /payments                 # Historial de pagos (admin)
```

### **👤 Gestión de Usuarios**
```http
GET  /usuarios/me              # Perfil del usuario autenticado
PUT  /usuarios/me              # Actualizar perfil de usuario
GET  /usuarios                 # Listar usuarios (admin)
```

### **📧 Newsletter y Marketing**
```http
GET    /newsletter             # Listar newsletters (admin)
POST   /newsletteradd          # Crear nuevo newsletter
PUT    /newsletter/:id         # Editar newsletter existente
DELETE /newsletter/:id         # Eliminar newsletter
POST   /newsletter/send        # Enviar newsletter masivo
GET    /newsletter/:id         # Ver newsletter específico
```

### **📊 Panel de Administración**
```http
GET  /admin/dashboard          # Métricas y estadísticas
GET  /admin/users              # Gestión CRUD usuarios
GET  /admin/services           # Gestión CRUD servicios
GET  /admin/reports            # Reportes de ventas
```

## 🏗️ Arquitectura del Sistema

### **📊 Diagrama de Arquitectura**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React SPA     │    │   Flask API     │    │  PostgreSQL DB  │
│                 │    │                 │    │                 │
│ • Components    │◄──►│ • RESTful API   │◄──►│ • Relaciones    │
│ • Context API   │    │ • JWT Auth      │    │ • Índices       │
│ • React Router  │    │ • Stripe API    │    │ • Migraciones   │
│ • Bootstrap 5   │    │ • Email Service │    │ • Backups       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                        │                        │
        ▼                        ▼                        ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Webpack Dev   │    │   Flask CLI     │    │   Alembic       │
│                 │    │                 │    │                 │
│ • Hot Reload    │    │ • Admin Commands│    │ • Schema Mgmt   │
│ • Bundle Optim  │    │ • Data Seeding  │    │ • Version Ctrl  │
│ • Source Maps   │    │ • Migrations    │    │ • Auto-generate │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### **🔄 Flujo de Datos**
1. **Autenticación**: Usuario → React → Flask JWT → PostgreSQL
2. **Pagos**: React → Stripe API → Flask Webhook → Base de Datos
3. **Admin**: React Admin → Flask RBAC → PostgreSQL CRUD
4. **Email**: Flask → Gmail SMTP → Usuario Final

### **🛡️ Capas de Seguridad**
- **Frontend**: HTTPS, CSP Headers, Input Validation
- **Backend**: JWT Tokens, CORS, Rate Limiting, SQL Injection Prevention
- **Database**: Encrypted Connections, Role-based Access, Backups
- **Payments**: Stripe Secure, PCI Compliance, Webhook Verification

## 📈 Escalabilidad y Performance

### **⚡ Optimizaciones Implementadas**
- **Frontend**: Code Splitting, Lazy Loading, Image Optimization
- **Backend**: Database Indexing, Query Optimization, Connection Pooling
- **Caching**: Redis para sesiones, CDN para assets estáticos
- **Monitoring**: Error Tracking, Performance Metrics, Uptime Monitoring

### **📊 Métricas de Performance**
- **Load Time**: < 2 segundos en 3G
- **First Paint**: < 1 segundo
- **Database Queries**: < 100ms promedio
- **API Response**: < 200ms promedio

## 👨‍💻 Desarrollado por

**🎯 Desarrollador Full Stack** especializado en tecnologías modernas.

### **💼 Perfil Profesional**
- **Frontend**: React 18, JavaScript ES6+, Bootstrap 5, Responsive Design
- **Backend**: Python Flask, RESTful APIs, JWT Authentication, PostgreSQL
- **DevOps**: Docker, CI/CD, Cloud Deployment (AWS, Render, Heroku)
- **Metodologías**: Agile, Git Flow, TDD, Code Review

### **🚀 Proyecto Destacado**
Este **Groupon Clone** demuestra competencias en:
- ✅ **Arquitectura Full Stack** escalable y mantenible
- ✅ **Integración de Pagos** con Stripe (PCI Compliance)
- ✅ **Autenticación y Autorización** con JWT y RBAC
- ✅ **UI/UX Profesional** con Bootstrap y diseño responsive
- ✅ **Base de Datos Relacional** con migraciones y optimización
- ✅ **Seguridad de Aplicaciones Web** (CORS, CSP, Validación)
- ✅ **Despliegue en la Nube** con configuración de producción

### **📧 Contacto**
- **GitHub**: [nicolasdelfino-123](https://github.com/nicolasdelfino-123)
- **LinkedIn**: [Nicolás Delfino](https://linkedin.com/in/nicolas-delfino)
- **Email**: nicolas.delfino@outlook.com
- **Portfolio**: [Mi Portfolio](https://nicolas-delfino-portfolio.com)

---

**📝 Proyecto desarrollado como parte del bootcamp de 4Geeks Academy**

**⭐ Si este proyecto te fue útil, ¡dale una estrella en GitHub! ⭐**
# Force deploy dom 14 sep 2025 19:11:02 -03
# Forced redeploy dom 14 sep 2025 19:19:42 -03
# Force deploy with latest changes dom 14 sep 2025 20:10:24 -03
