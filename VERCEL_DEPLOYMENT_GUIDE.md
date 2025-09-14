# 🚀 Guía de Despliegue en Vercel

## 📋 Variables de Entorno Requeridas

Configura estas variables en el panel de Vercel:

### **Base de Datos**
- `DATABASE_URL` = `postgresql://username:password@host:port/database`

### **Flask Security**  
- `FLASK_APP_KEY` = `tu_clave_secreta_super_segura_256_bits`
- `FLASK_APP` = `src/app.py`
- `FLASK_DEBUG` = `0`

### **Stripe (usar claves reales de tu cuenta)**
- `STRIPE_SECRET_KEY` = `sk_test_tu_clave_secreta_stripe`

### **Gmail SMTP**
- `GMAIL_USER` = `tu_email@gmail.com` 
- `GMAIL_PASSWORD` = `tu_app_password_gmail`

### **URLs de Aplicación**
- `FRONT_END_URL` = `https://tu-proyecto.vercel.app`
- `BACKEND_URL` = `https://tu-proyecto.vercel.app`
- `BASENAME` = `/`

## 🔧 Pasos para Desplegar

1. **Crear proyecto en Vercel**
2. **Conectar repositorio GitHub**
3. **Configurar variables de entorno** (usar valores reales)
4. **Crear base de datos PostgreSQL** en Vercel
5. **Actualizar DATABASE_URL** con la URL real
6. **Deploy!**

## ⚠️ Importante

- **NUNCA** subas claves reales a GitHub
- Usa solo claves de prueba en desarrollo
- Configura las variables directamente en Vercel
