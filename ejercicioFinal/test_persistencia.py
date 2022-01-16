import persistencia
import pytest
def test_guardar_pedido():
    with open("pedidos.txt", "w+", encoding="utf-8") as file:
        persistencia.guardar_pedido("Pedro", "Gil de Diego",file)
        persistencia.guardar_pedido("Michael", "Jordan",file)
        firstline = file.readline()
        secondline = file.readline()
        print(firstline)
        assert firstline == "-Pedro Gil de Diego"
        assert secondline == "-Michael Jordan"
        file.close()
        