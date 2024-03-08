from flask import Blueprint, render_template
from binary import convert, decimal_to_hexa, decimal_to_octal
from requests import request

converter_bp = Blueprint('converter', __name__)

@converter_bp.route('/number_converter')
def main():
    decimal = None
    return render_template('index.html', decimal=decimal)


from flask import jsonify

@converter_bp.route('/number_converter/decimal_to_binary/<int:decimal>', methods=['GET', 'POST'])
def decimal_to_binary(decimal: int):
    binary = convert(decimal)
    hexadecimal = decimal_to_hexa(decimal)
    octal = decimal_to_octal(decimal)

    return jsonify([{'type': 'Binary', 'value': binary},
                    {'type': 'Hexadecimal', 'value': hexadecimal},
                    {'type': 'Octal', 'value': octal}])
