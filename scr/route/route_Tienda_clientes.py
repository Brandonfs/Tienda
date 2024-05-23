import io

from flask import Blueprint, render_template, request, url_for, make_response, session
from flask_paginate import Pagination, get_page_args
from werkzeug.utils import redirect
import pandas as pd
from scr.models.model_Tienda_clientes import model_Tienda_clientes
from scr.models.entities.Tienda_clientes import Tienda_clientes

main = Blueprint('Tienda_clientes_bp', __name__)

def get_tienda_clientes_data_from_request():
    nombres = request.form['nombres']
    apellido = request.form['hora_ingreso']
    email = request.form['hora_salida']
    password = request.form('polo_gift')
    rol = request.form['catalog_book']
    # Obtener el estado del campo booleano (si está seleccionado o no)
    estado = request.form.get('estado', False)
    # Convertir el estado a un booleano
    estado = estado == 'on'  # Si 'estado' es 'on', estado es True, de lo contrario, False
    
    return nombres, apellido, apellido, email, password, rol, estado
