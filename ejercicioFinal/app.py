from flask import Flask, request, redirect, Response


app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def pizza():
    nombre=request.form.get("p1")
    apellido=request.form.get("p2")
    print("La persona que solicito la pizza se llama "+nombre+" "+apellido)
    return redirect("http://localhost/ejercicioFinal/solicita_pedido.html", code=302)

@app.route("/checksize", methods=['POST'])
def checksize():
    
    pequenna=request.form.get("size")
    mensaje="Disponible"
    if(pequenna=="S"):
        mensaje="No disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
    
    