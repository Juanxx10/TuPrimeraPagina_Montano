# 🏍️ Motos de Alta Gama - TuPrimeraPagina_Montano

Proyecto web desarrollado en **Django** como parte del curso de **Python**, con el objetivo de aplicar el patrón **MVT (Model–View–Template)** y la herencia de plantillas utilizando **Bootstrap 5**.

---

## 🚀 Descripción

**Motos de Alta Gama** es una aplicación web que permite gestionar una base de datos de motos nuevas y usadas.  
Incluye la posibilidad de agregar **Marcas**, **Motos** y **Clientes**, además de realizar búsquedas mediante diferentes tipos de filtro.

---

## ⚙️ Funcionalidades

- 🧩 Herencia de plantillas con **Bootstrap 5**  
- 🏷️ Modelos: **Marca**, **Moto**, **Cliente**  
- 📝 Formularios para agregar registros a la base de datos  
- 🔍 Búsqueda de motos por diferentes filtros
- 🧱 Implementación completa del patrón **MVT**  

---

## 🗂️ Modelos

1. **Marca:** nombre, país de origen
2. **Moto:** marca, modelo, cilindrada, precio, año, estado (nueva/usada), kilómetros
3. **Cliente:** nombre, email, telefono

---

## 🧰 Tecnologías utilizadas

- **Python 3.x**
- **Django 5**
- **Bootstrap 5**
- **HTML5 / CSS3**
- **SQLite3** (base de datos por defecto)

---

## 🖥️ Instrucciones de ejecución

1. ***Clonar el repositorio***

   git clone https://github.com/Juanxx10/TuPrimeraPagina_Montano.git

2. ***Crear y Activar el entorno virtual***

    python -m venv venv
    venv\Scripts\activate     # En Windows
    source venv/bin/activate  # En Linux/Mac

3. ***Instalar dependencias***

    pip install -r requirements.txt

4. ***Aplicar Migraciones***

    python manage.py migrate

5. ***Ejecutar el servidor***

    python manage.py runserver

6. ***Abrir el servidor***

    👉 http://127.0.0.1:8000/

---

## 🧾 Estructura de prueba recomendada

1 - Ingresar desde la página de inicio.

2 - Agregar algunas Marcas.

3 - Crear una o varias Motos (asociadas a marcas).

4 - Agregar Clientes.

5 - Probar el buscador de motos por modelo.

---

## 🧑‍💻 Autor

Juan I. Montano
TP3 - Curso de Python
📅 Pre-entrega - Octubre 2025