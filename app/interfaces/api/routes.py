from flask import Blueprint, jsonify, request
from application.ventas.ventas_service import VentasService
from application.inventario.inventario_service import InventarioService
from application.entregas.entrega_service import EntregaService


api = Blueprint("api", __name__)

@api.route("/pedidos", methods=["GET"])
def obtener_pedidos():
    pedidos = VentasService.listar_pedidos()

    return jsonify([
        {
            "id": p.id,
            "estado": p.estado,
            "total": p.calcular_total()
        } for p in pedidos
    ])


@api.route("/pedidos", methods=["POST"])
def crear_pedido():
    pedido = VentasService.crear_pedido(vendedor_id=1)

    return jsonify({
        "id": pedido.id,
        "estado": pedido.estado,
        "total": pedido.calcular_total()
    })


@api.route("/inventario/<int:producto_id>", methods=["GET"])
def consultar_stock(producto_id):
    stock = InventarioService.consultar_stock(producto_id)

    return {
        "producto_id": producto_id,
        "stock": stock
    }

@api.route("/inventario/<int:producto_id>", methods=["POST"])
def actualizar_stock(producto_id):
    data = request.json
    cantidad = data.get("cantidad", 0)

    nuevo_stock = InventarioService.actualizar_stock(producto_id, cantidad)

    return {
        "producto_id": producto_id,
        "nuevo_stock": nuevo_stock
    }

@api.route("/entregas/<int:pedido_id>", methods=["POST"])
def generar_entrega(pedido_id):
    entrega = EntregaService.generar_entrega(pedido_id)

    return {
        "id": entrega.id,
        "estado": entrega.estado
    }