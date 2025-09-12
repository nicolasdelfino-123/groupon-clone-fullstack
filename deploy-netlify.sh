#!/bin/bash

echo "🚀 Preparando despliegue en Netlify - Groupon Clone"
echo "=================================================="

# Función de colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Verificar que estemos en el directorio correcto
if [ ! -f "package.json" ]; then
    echo -e "${RED}❌ Error: No se encontró package.json. Ejecuta desde el directorio del proyecto.${NC}"
    exit 1
fi

echo -e "${BLUE}📦 Instalando dependencias...${NC}"
npm install

echo -e "${BLUE}🔨 Generando build de producción...${NC}"
npm run build

echo -e "${BLUE}📊 Verificando tamaño del build...${NC}"
if [ -d "public" ]; then
    BUILD_SIZE=$(du -sh public | cut -f1)
    echo -e "${GREEN}✅ Build generado exitosamente: ${BUILD_SIZE}${NC}"
else
    echo -e "${RED}❌ Error: No se generó el directorio public${NC}"
    exit 1
fi

echo -e "${YELLOW}📋 Archivos listos para Netlify:${NC}"
echo "   📁 public/ (build de React)"
echo "   ⚙️  netlify.toml (configuración)"
echo "   🔀 public/_redirects (SPA routing)"

echo ""
echo -e "${GREEN}🎉 ¡Proyecto listo para desplegar en Netlify!${NC}"
echo ""
echo -e "${BLUE}👆 Próximos pasos:${NC}"
echo "1. Ve a https://netlify.com"
echo "2. Arrastra la carpeta 'public' a Netlify"
echo "3. O conecta tu repositorio GitHub"
echo "4. Configura tu dominio personalizado"
echo ""
echo -e "${YELLOW}💡 Tip: Para URL personalizada, necesitarás un dominio propio${NC}"
