from msilib.schema import File


def guardar_pedido(nombre, apellido,file):
    file.write("-"+nombre+" "+apellido+"\n")
    


