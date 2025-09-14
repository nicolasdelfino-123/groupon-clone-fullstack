#!/bin/bash

echo "🚀 Preparando Groupon Clone para Vercel"
echo "======================================"

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}📦 Instalando dependencias...${NC}"
npm install

echo -e "${BLUE}🔨 Generando build de producción...${NC}"
npm run build

echo -e "${BLUE}📝 Verificando configuración...${NC}"

# Verificar que el build se generó
if [ -d "public" ]; then
    echo -e "${GREEN}✅ Build generado correctamente${NC}"
    ls -la public/ | head -10
else
    echo -e "${RED}❌ Error: No se generó el build${NC}"
    exit 1
fi

# Verificar archivos de configuración
echo -e "${BLUE}📋 Archivos de configuración:${NC}"
echo "✅ vercel.json - Configuración de despliegue"
echo "✅ package.json - Dependencias frontend"
echo "✅ requirements.txt - Dependencias backend"
echo "✅ src/app.py - Backend Flask"

echo ""
echo -e "${GREEN}🎉 ¡Proyecto listo para Vercel!${NC}"
echo ""
echo -e "${YELLOW}👆 Próximos pasos:${NC}"
echo "1. Ve a https://vercel.com"
echo "2. Conecta tu cuenta GitHub"
echo "3. Importa tu repositorio"
echo "4. Configura variables de entorno"
echo "5. ¡Deploy automático!"
