#!/bin/bash

# Cambiar permisos del archivo creado a root
echo "Ingresar archivo para cambiar permisos a root"
read archivo
chown root:root "$archivo"

#Mostrar los archivos del directorio y su detalle
ls -l

# Mostrar la ruta del directorio actual
pwd

