import io

from flask import Blueprint, render_template, request, url_for, make_response, session
from flask_paginate import Pagination, get_page_args
from werkzeug.utils import redirect
import pandas as pd
from scr.models.model_Tienda_ventas import model_Tienda_ventas
from scr.models.entities.Tienda_ventas import Tienda_ventas

main = Blueprint('Tienda_ventas_bp', __name__)


def get_Tienda_ventas_data_from_request():
    ventaId = request.form['ventaId']
    clienteId = request.form['clienteId']
    fechaVenta = request.form['fechaVenta']
    total = request.form['total']

    return ventaId, clienteId, fechaVenta, total


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

    clienteId = model_Tienda_ventas.get_tienda_ventas_list_activos(search_query)

    for ventas in ventas:
        ventas_dict = {
            'ventaId': ventas.productoId,
            'clienteId': ventas.nombre,
            'fechaVenta': ventas.descripcion,
            'total': ventas.precio,
        }
        data.append(ventas_dict)

    total = len(data)
    paginated_data = data[offset: offset + per_page]

    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template('index.html', search_query=search_query,
                           attentions=paginated_data, pagination=pagination)


# insert
@main.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        clienteId, fechaVenta, total \
            = get_Tienda_ventas_data_from_request()

        retorno = model_Tienda_ventas.add_tienda_ventas(
            Tienda_ventas(clienteId, fechaVenta, total))

        if retorno == 1:
            print('Registrado')
        else:
            print('No registrado')

        return redirect(url_for('Tienda_ventas_bp.Index'))


# update
@main.route('/update', methods=['POST'])
def update():
    if request.method == "POST":

        clienteId, fechaVenta, total \
            = get_Tienda_ventas_data_from_request()

        ventaId = request.form['ventaId']
        Tienda_ventas_model = Tienda_ventas(ventaId, clienteId, fechaVenta, total)

        retorno = model_Tienda_ventas.update_tienda_ventas(Tienda_ventas_model)
        if retorno == 1:
            print('Actualizado')
        else:
            print('No Actualizado')

        return redirect(url_for('Tienda_ventas_bp.Index'))


# delete primer enfoque
@main.route('/delete/<string:id>')
def delete(id):
    retorno = model_Tienda_ventas.delete_tienda_ventas(id)
    if retorno == 1:
        print('Eliminado')
    else:
        print('No Eliminado')

    return redirect(url_for('Tienda_ventas_bp.Index'))
