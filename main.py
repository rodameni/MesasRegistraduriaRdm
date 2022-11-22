
from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS


from Controladores.MesaControlador import MesaControlador


app = Flask(__name__)
cors = CORS(app)


##############################
##     VARIABLES GLOBALES   ##
##############################

miControladorMesa = MesaControlador()


####################################
##    PROBAR EL SERVICIO          ##
####################################
@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = " Welcome to services of votes  ..."
    return jsonify(json)

#

#####################################
##           ENDPOINT MESAS        ##
#####################################

@app.route("/mesas", methods=["GET"])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas", methods=["POST"])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=["GET"])
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=["PUT"])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=["DELETE"])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)



if __name__ == "__main__":
    app.run(debug=False, port=9000)