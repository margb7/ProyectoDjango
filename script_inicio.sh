echo "Creando tablas de la base de datos"

python web/manage.py makemigrations misitio
python web/manage.py sqlmigrate misitio misitio

echo "Creando usuario admin"


