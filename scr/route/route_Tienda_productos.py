import io

from flask import Blueprint, render_template, request, url_for, make_response, session
from flask_paginate import Pagination, get_page_args
from werkzeug.utils import redirect
import pandas as pd
from scr.models.model_Tienda_productos import model_Tienda_productos
from scr.models.entities.Tienda_productos import Tienda_productos

main = Blueprint('Tienda_productos_bp', __name__)


def get_Tienda_productos_data_from_request():
    productoId = request.form['productoId']
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    stock = request.form['stock']
    fechaRegistro = request.form('fechaRegistro')

    return productoId, nombre, descripcion, stock, fechaRegistro


# Select
@main.route('/', methods=['GET', 'POST'])
def Index():
    paginated_data = []
    data = []
    pagination = None

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    search_query = request.args.get('q', '')  

    if request.method == 'POST':
        pass

    productos = model_Tienda_productos.get_tienda_productos_list_activos()

    for producto in productos: 
        producto_dict = {
            'productoId': producto.productoId,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
            'fechaRegistro': producto.fechaRegistro,
        }
        data.append(producto_dict)

    total = len(data)
    paginated_data = data[offset: offset + per_page]

    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template('index.html', search_query=search_query,
                           attentions=paginated_data, pagination=pagination)

# insert
@main.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        nombre, descripcion, precio, stock, fechaRegistro \
            = get_Tienda_productos_data_from_request()

        retorno = model_Tienda_productos.add_tienda_productos(
            Tienda_productos(nombre, descripcion, precio, stock, fechaRegistro))

        if retorno == 1:
            print('Registrado')
        else:
            print('No registrado')

        return redirect(url_for('Tienda_productos_bp.Index'))


# update
@main.route('/update', methods=['POST'])
def update():
    if request.method == "POST":

        nombre, descripcion, precio, stock, fechaRegistro \
            = get_Tienda_productos_data_from_request()

        productoId = request.form['productoId']
        Tienda_productos_model = Tienda_productos(productoId, nombre, descripcion, 
                                                  precio, stock, fechaRegistro)

        retorno = model_Tienda_productos.update_tienda_productos(Tienda_productos_model)
        if retorno == 1:
            print('Actualizado')
        else:
            print('No Actualizado')

        return redirect(url_for('Tienda_productos_bp.Index'))


# delete primer enfoque
@main.route('/delete/<string:id>')
def delete(id):
    retorno = model_Tienda_productos.delete_tienda_productos(id)
    if retorno == 1:
        print('Eliminado')
    else:
        print('No Eliminado')

    return redirect(url_for('Tienda_productos_bp.Index'))
