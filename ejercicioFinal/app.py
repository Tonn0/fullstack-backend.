from flask import Flask, request, redirect


app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def pizza():
    nombre=request.form.get("p1")
    apellido=request.form.get("p2")
    print("La persona que solicito la pizza se llama "+nombre+" "+apellido)
    return redirect("http://localhost/ejercicioFinal/solicita_pedido.html", code=302)
    