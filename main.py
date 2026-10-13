monto_total_diario = 0.0
caja_abierta = True
"si_metodo_pago" == 1
descuento = "total_iva_cliente"

while caja_abierta:
    print("1 Menu")
    print("2 Registrar venta")
    print("3 cerrar caja y salir")

    opcion = int(input("Ingrese opcion:"))

    if(opcion == 3):
        print("cerrar caja y salir")
        caja_abierta = False

    if  opcion == 1 :
        print ("Registro venta")

        subtotal_cliente = 0 
        registro_venta = 3 

    while registro_venta:

        print ("Ingrese precio ")

        entrada =  input ("precio ")

        if entrada  == "0" or entrada  == "fin":

           registro_venta = False 

        else :

           precio = float (entrada )

           subtotal_cliente= subtotal_cliente + precio 

 
print("Boleta")
print("Subtotal:", subtotal_cliente )
monto_iva = subtotal_cliente * 0.19
total_iva_cliente = subtotal_cliente + monto_iva 
print ("Monto IVA:", monto_iva)       
print ("Total Cliente (+IVA):", total_iva_cliente)

input("Presione cualquier tecla para continuar")
print("metodo de pago")
metodo_pago = input("1.Efectivo\n2.Tarjeta\nOpcion: ")
descuento = 0.0
if metodo_pago == "1":
   descuento = total_iva_cliente*0.05
   print("Descuento por efectivo (5%):", descuento)
total_final_cliente = total_iva_cliente - descuento
print("---")
print("Total Final:", total_final_cliente)
print("---")   

          

        