import io

from flask import Blueprint, render_template, request, url_for, make_response, session
from flask_paginate import Pagination, get_page_args
from werkzeug.utils import redirect
import pandas as pd
from scr.models.model_Tienda_detallesVentas import model_Tienda_detallesVentas
from scr.models.entities.Tienda_detallesVentas import Tienda_detallesVentas

main = Blueprint('Tienda_detallesVentas_bp', __name__)


def get_Tienda_detallesVentas_data_from_request():
    detalleId = request.form['detalleId']
    ventaId = request.form['ventaId']
    productoId = request.form['productoId']
    cantidad = request.form['cantidad']
    precioUnitario = request.form('precioUnitario')
    subtotal = request.form('subtotal')

    return detalleId, ventaId, productoId, cantidad, precioUnitario, subtotal


# Select
@main.route('/', methods=['GET', 'POST'])
def Index():
    paginated_data = []
    data = []
    pagination = None

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    search_query = request.args.get('q', '')  # Obtener el parámetro de búsqueda de la URL

    if request.method == 'POST':
        
        pass

    clientes = model_Tienda_detallesVentas.get_tienda_detallesVentas_list_activos(search_query)

    
    for detallesVentas in detallesVentas:
        detallesVentas_dict = {
            'detalleId': detallesVentas.detalleId,
            'ventaId': detallesVentas.ventaId,
            'productoId': detallesVentas.productoId,
            'cantidad': detallesVentas.cantidad,
            'precioUnitario': detallesVentas.precioUnitario,
            'subtotal': detallesVentas.subtotal,
        }
        data.append(detallesVentas_dict)

    # Calcular el número total de elementos y la lista de elementos para la página actual
    total = len(data)
    paginated_data = data[offset: offset + per_page]

    # Crear objeto Pagination
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template('index.html', search_query=search_query,
                           attentions=paginated_data, pagination=pagination)


# insert
@main.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        # obtener los datos comunes de la solicitud
        ventaId, productoID, cantidad, precioUnitario, subtotal \
            = get_Tienda_detallesVentas_data_from_request()

        retorno = model_Tienda_detallesVentas.add_tienda_detallesVentas(
            Tienda_detallesVentas(ventaId, productoID, cantidad, precioUnitario, subtotal))

        if retorno == 1:
            print('Registrado')
        else:
            print('No registrado')

        return redirect(url_for('Tienda_detallesVentas_bp.Index'))


# update
@main.route('/update', methods=['POST'])
def update():
    if request.method == "POST":

        ventaId, productoID, cantidad, precioUnitario, subtotal \
            = get_Tienda_detallesVentas_data_from_request()

        detalleId = request.form['id']
        Tienda_detallesVentas_model = Tienda_detallesVentas(ventaId, productoID, cantidad,
                                                            precioUnitario, subtotal, detalleId)

        retorno = model_Tienda_detallesVentas.update_tienda_detallesVentas(Tienda_detallesVentas_model)
        if retorno == 1:
            print('Actualizado')
        else:
            print('No Actualizado')

        return redirect(url_for('Tienda_detallesVentas_bp.Index'))


# delete primer enfoque
@main.route('/delete/<string:id>')
def delete(id):
    retorno = model_Tienda_detallesVentas.delete_tienda_detallesVentas(id)
    if retorno == 1:
        print('Eliminado')
    else:
        print('No Eliminado')

    return redirect(url_for('Tienda_detallesVentas_bp.Index'))
