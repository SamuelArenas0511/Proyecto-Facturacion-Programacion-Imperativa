from tkinter import *      #Importacion de la libreria Tktinter
from tkinter import ttk     #Importar libreria para hacer ventanas (notebooks) y listas despegables (combobox)
import tkinter.font as tkFont #Importar libteria de fuentes tkinter
from tkinter import messagebox
import numpy

################CREACION DE LA VENTANA PRINCIPAL###########

ventana = Tk()
ventana.geometry("1344x756") #Medidas
ventana.title("PROGRAMA DE FACTURACIÓN") #Titulo
ventana.iconbitmap("icono.ico") #Icono

################CREACION DE LA MATRIZ####################

matriz = numpy.array([[None]*8]*3)
matriz[0][0] = "Hamburguesa"
matriz[0][1] = "Salchipapa"
matriz[0][2] = "Perro"
matriz[0][3] = "Arepa con todo"
matriz[0][4] = "Gaseosa"
matriz[0][5] = "Jugo Hit"
matriz[0][6] = "Agua"
matriz[0][7] = "Cerveza"
for f in range(1,len(matriz)):
    for c in range(0,len(matriz[0])):
        matriz[f][c] = 0

################FUNCIONES DENTRO DEL PROGRAMA###########

def prueba(e):
    if e == 1:
        newventana = Toplevel(ventana)
        newventana.geometry("290x350") 
        newventana.title("FACTURA")

        texto = Label(newventana, text="Hola soy factura")
        boton = Button(newventana, text="Hola soy boton para salir o para imprimir")
        texto.pack()
        boton.pack(side="top", pady=50)

        newventana.mainloop()
     
    if e == 2:
       messagebox.showwarning(message="Valor incorrecto")
    
    if e == 3:
       messagebox.showerror(message="Valor incorrecto")

def salir(panel): #Función al presionar sobre los botones
    panel.lift() #Determina el Frame que se va a mostrar en pantalla, en funcion del parametro que da cada boton

def hover(e): #Función cuando el cursos este sobre los botones
    if e == 1: #Cambia la imagen de cada boton en funcion del parametro, el cual cambia en base a sobre que boton tenemos el cursor encima
        bFacturacion["image"] = bImagenClick1 
        bFacturacion.config(cursor="hand2") #Cambia el tipo de cursor 
    elif e == 2:
        bStockI["image"] = bImagenClick2
        bStockI.config(cursor="hand2")
    elif e == 3:
        bBuscar["image"] = bImgBuscarClick
        bBuscar.config(cursor="hand2")
    elif e == 4:
        bAgregar["image"] = bImgAgregarClick
        bAgregar.config(cursor="hand2")
    elif e == 5:
        bDevuelto["image"] = bImgDevueltoClick
        bDevuelto.config(cursor="hand2")
    elif e == 6:
        bVenta["image"] = bImgVentaClick
        bVenta.config(cursor="hand2")
    elif e == 7:
        bFactura["image"] = bImgFacturaClick
        bFactura.config(cursor="hand2")
    elif e == 8:
        bBorrar["image"] = bImgBorrarClick
        bBorrar.config(cursor="hand2")
    elif e == 9:
        bSalir["image"] = bImgSalirClick
        bSalir.config(cursor="hand2")
    elif e == 10:
        bBuscarStock["image"] = bImgBuscarStockClick
        bBuscarStock.config(cursor="hand2")
    elif e == 11:
        bStock["image"] = bImgStockClick
        bStock.config(cursor="hand2")
    elif e == 12:
        bAgregarStock["image"] = bImgAgregarStockClick
        bAgregarStock.config(cursor="hand2")
    elif e == 13:
        bSalirStock["image"] = bImgSalirStockClick
        bSalirStock.config(cursor="hand2")
        
        
        
def over(e): #Función cuando el cursos deje de estar encima del boton
    if e == 1:
     bFacturacion["image"] = bImagen1 #Cambia la imagen a su estado original 
    elif e == 2:
     bStockI["image"] = bImagen2
    elif e == 3:
     bBuscar["image"] = bImgBuscar
    elif e == 4:
     bAgregar["image"] = bImgAgregar
    elif e == 5:
        bDevuelto["image"] = bImgDevuelto
    elif e == 6:
        bVenta["image"] = bImgVenta
    elif e == 7:
        bFactura["image"] = bImgFactura
    elif e == 8:
        bBorrar["image"] = bImgBorrar
    elif e == 9:
        bSalir["image"] = bImgSalir
    elif e == 10:
        bBuscarStock["image"] = bImgBuscarStock
    elif e == 11:
        bStock["image"] = bImgStock
    elif e == 12:
        bAgregarStock["image"] = bImgAgregarStock
    elif e == 13:
        bSalirStock["image"] = bImgSalirStock


        
def buscar():#Funcion que recoge informacion de cbProducto y pone la info de lNombre y lPrecio con la matriz
    buscar = cbProducto.get()
    if(buscar == ""):
        messagebox.showwarning(message="Seleccione algun producto en el combo")
    else:
        for fila in range(0,1):
            for col in range(0,len(matriz[0])):   
                if(buscar == matriz[fila][col]):
                    lNombre.config(text = matriz[fila][col])
                    lPrecio.config(text = matriz[fila + 2][col])

def agregarStock():#Recoge la información de los entry de nueva cantidad y nuevo precio y cambia el valor de la matriz
    agregar = cbProducto2.get()
    cantidad = eCantidadN.get()
    precio = ePrecio.get()
    if(agregar == ""):
        messagebox.showwarning(message="Seleccione algun producto en el combo")
    elif(cantidad == "" and precio == ""):
        messagebox.showwarning(message="Digite una cantidad o precio para agregar")
    elif(cantidad == "" and precio != ""):
        if(precio.isnumeric()):
            for fila in range(0,1):
                for col in range(0,len(matriz[0])):   
                    if(agregar == matriz[fila][col]):
                        matriz[fila + 2][col] = precio
        else:
            messagebox.showwarning(message="Porfavor solo digite numeros enteros en precio y cantidad")
    elif(cantidad != "" and precio == ""):
        if(cantidad.isnumeric()):
            for fila in range(0,1):
                for col in range(0,len(matriz[0])):   
                    if(agregar == matriz[fila][col]):
                        matriz[fila + 1][col] = cantidad
        else:
            messagebox.showwarning(message="Porfavor solo digite numeros enteros en precio y cantidad")
    elif(cantidad != "" and precio != ""):
        if(cantidad.isnumeric() and precio.isnumeric()):
            for fila in range(0,1):
                for col in range(0,len(matriz[0])):   
                    if(agregar == matriz[fila][col]):
                        matriz[fila + 1][col] = cantidad
                        matriz[fila + 2][col] = precio
        else:
            messagebox.showwarning(message="Porfavor solo digite numeros enteros en precio y cantidad")



def buscarStock():#recoge la info del entry del producto, y lo pone en los label de cantidad de producto, y precio del producto
    buscarStock = cbProducto2.get()
    if(buscarStock == ""):
        messagebox.showwarning(message="Seleccione algun producto en el combo")
    else:
        for fila in range(0,1):
            for col in range(0,len(matriz[0])):   
                if(buscarStock == matriz[fila][col]):
                    lCantidad.config(text = matriz[fila + 1][col])
                    lPrecioAc.config(text = matriz[fila + 2][col])

def listaStock():#Muestra una ventana emergente de una lista de los productos y su respectiva cantidad con la matriz
    lista = ""
    for fila in range(0,len(matriz)):
        for col in range(0,len(matriz[0])):
            if(fila == 0 and col == 0):
                lista += "\t\t"
            if(fila == 1 and col == 0):
                lista += "Cantidad:" + "\t\t"
            if(fila == 2 and col == 0):
                lista += "Precio:" + "\t\t"       
            lista += str(matriz[fila][col]) + "\t\t"
        lista += "\n"   
    texto = Toplevel(ventana)
    texto.geometry("1200x100")
    texto.title("Lista productos")
    mostrarMatriz = Text(texto, width = 300, height = 4)
    mostrarMatriz.pack()
    mostrarMatriz.delete("1.0", END)
    mostrarMatriz.insert(INSERT,lista)
        
    








################CREACION DE LAS VENTANA###########
    
ventana1 = Frame(ventana)  #Ventana de Inicio
ventana2 = Frame(ventana)  #Ventana de Facturación
ventana3 = Frame(ventana)  #Ventana de Stock










################ELEMENTOS VENTANA DE INICIO###########

################IMAGEN DE FONDO###########

imagenBg= PhotoImage(file="bg1.png")
canvasBg = Canvas(ventana1, width = 1344, height = 756)
canvasBg.pack(fill = "both", expand = True)
canvasBg.create_image( 0, 0, image = imagenBg, anchor = "nw")

###########BOTONES###########

#####IMAGENES####
bImagen1 = PhotoImage(file = "btn.png") #Imagen del boton "facturacion"
bImagenClick1= PhotoImage(file = "btnclick.png")
bImagen2 = PhotoImage(file = "btn2.png") #Imagen del boton "Stock"
bImagenClick2= PhotoImage(file = "btn2click.png")

#####DECLARACION DE LOS BOTONES####
bFacturacion = Button(canvasBg, image=bImagen1, borderwidth = 0, highlightthickness=0, bd=0, bg="white", command=lambda: salir(ventana2))
bStockI = Button(canvasBg, image=bImagen2, borderwidth = 0, highlightthickness=0, bd=0, bg="white", command=lambda: salir(ventana3))

#####FUNCIONES PARA CUANDO SE TENGA EL CURSO ENCIMA O NO DE LOS BOTONES####

bFacturacion.bind("<Enter>",lambda event: hover(1)) #Funcion para el curso sobre el botón
bFacturacion.bind("<Leave>",lambda event: over(1))  #Funcion para el cursor fuera del botón
bStockI.bind("<Enter>",lambda event: hover(2))
bStockI.bind("<Leave>",lambda event: over(2))

#####COLOCAR ELEMENTOS DE LA VENTANA PRINCIPAL####
bFacturacion.place(x=100, y =300)
bStockI.place(x=100, y =450)







################ELEMENTOS VENTANA DE FACTURACIÓN###########

################IMAGEN DE FONDO###########

imagenBg2= PhotoImage(file="bg2.png")
canvasBg2 = Canvas(ventana2, width = 1344, height = 756)
canvasBg2.pack(fill = "both", expand = True)
canvasBg2.create_image( 15, -10, image = imagenBg2, anchor = "nw")

################FUENTES###########

fuenteT= tkFont.Font(family="Montserrat", size=16, weight="normal")
fuenteCB= tkFont.Font(family="Montserrat", size=20, weight="normal")
fuenteF= tkFont.Font(family="Montserrat", size=14, weight="normal")
fuenteF2= tkFont.Font(family="Montserrat", size=14, weight="bold")
fuenteN= tkFont.Font(family="Montserrat", size=19, weight="bold")
fuenteP= tkFont.Font(family="Montserrat", size=18, weight="bold")
fuenteC= tkFont.Font(family="Montserrat", size=16, weight="bold")
fuenteD= tkFont.Font(family="Montserrat", size=20, weight="bold")

################IMAGENES###########

bImgBuscar = PhotoImage(file = "btnBuscar.png") #Imagen del boton "Buscar"
bImgBuscarClick = PhotoImage(file = "btnBuscarClick.png") #Imagen del boton "Buscar" en click
bImgAgregar = PhotoImage(file = "btnAgregar.png") #Imagen del boton "Agregar" 
bImgAgregarClick = PhotoImage(file = "btnAgregarClick.png") #Imagen del boton "Buscar" en click
bImgDevuelto = PhotoImage(file = "btnDevuelta.png") #Imagen del boton "Devuelta" 
bImgDevueltoClick = PhotoImage(file = "btnDevueltaClick.png") #Imagen del boton "Devuelta" en click
bImgVenta= PhotoImage(file = "btnVenta.png") #Imagen del boton "Confirmar venta" 
bImgVentaClick= PhotoImage(file = "btnVentaClick.png") #Imagen del boton "Confirmar venta" en click
bImgFactura= PhotoImage(file = "btnFactura.png") #Imagen del boton "Generar factura"
bImgFacturaClick=PhotoImage(file = "btnFacturaClick.png") #Imagen del boton "Generar factura" en click
bImgBorrar= PhotoImage(file = "btnBorrar.png") #Imagen del boton "Borrar Factura"
bImgBorrarClick=PhotoImage(file = "btnBorrarClick.png") #Imagen del boton "Borrar factura" en click
bImgSalir= PhotoImage(file = "btnSalir.png") #Imagen del boton "Salir"
bImgSalirClick=PhotoImage(file = "btnSalirClick.png") #Imagen del boton "Salir" en click

################ELEMENTOS FRAME 1###########
cbProducto = ttk.Combobox(canvasBg2, values=["Hamburguesa", "Salchipapa", "Perro", "Arepa con todo", "Gaseosa", "Jugo Hit", "Agua", "Cerveza"], width=25, state="readonly", font=fuenteT)
bBuscar = Button(canvasBg2, image=bImgBuscar, borderwidth =0, highlightthickness=0, bd=0, bg="#373F51",relief=FLAT, command = buscar)
lNombre = Label(canvasBg2, text="", font=fuenteN, background="#373F51", foreground="#EDEDED")
lPrecio = Label(canvasBg2, text="", font=fuenteP, background="#373F51", foreground="#EDEDED")
eCantidad = Entry(canvasBg2, background="#373F51", foreground= "white", font=fuenteC, width=4, relief=SUNKEN, justify="center", insertbackground="white")
bAgregar = Button(canvasBg2, image=bImgAgregar, borderwidth =0, highlightthickness=0, bd=0, bg="#373F51",relief=FLAT)


################ELEMENTOS FRAME 2###########

eDevuelto = Entry(canvasBg2, background="#373F51", foreground= "white", font=fuenteN, width=20, relief=SUNKEN, justify="center", insertbackground="white")
eDevuelto.insert(0,"$$$")
bDevuelto = Button(canvasBg2, image=bImgDevuelto, borderwidth =0, highlightthickness=0, bd=0, bg="#373F51",relief=FLAT)
lDevuelto = Label(canvasBg2, text="", font=fuenteN, background="#373F51", foreground="#EDEDED")

################ELEMENTOS FRAME 3###########

lSubtotal = Label(canvasBg2, text="", font=fuenteD, background="#373F51", foreground="#FFD87F")
lDescuento = Label(canvasBg2, text="", font=fuenteD, background="#373F51", foreground="#FFD87F")
lTotal = Label(canvasBg2, text="", font=fuenteD, background="#373F51", foreground="#FFD87F")
bVenta = Button(canvasBg2, image=bImgVenta, borderwidth =0, highlightthickness=0, bd=0, bg="#373F51",relief=FLAT)

################ELEMENTOS FRAME 4###########

bFactura = Button(canvasBg2, image=bImgFactura, borderwidth =0, highlightthickness=0, bd=0, bg="#373F51",relief=FLAT)
bBorrar = Button(canvasBg2, image=bImgBorrar, borderwidth =0, highlightthickness=0, bd=0, bg="#373F51",relief=FLAT)
bSalir = Button(canvasBg2, image=bImgSalir, borderwidth =0, highlightthickness=0, bd=0, bg="#373F51",relief=FLAT, command=lambda: salir(ventana1) )

################ELEMENTOS FRAME 5 TABLA DE LA PREVISUALIZACION DE LA FACTURA###########

tvFactura= ttk.Treeview(canvasBg2, columns=("colC","colPU","colPT")) #Definir la tabla

tvFactura.column("#0", width=95, anchor=CENTER)  #Definir el tamaño y colocación de cada columna de la tabla
tvFactura.column("colC", width=80, anchor=CENTER)
tvFactura.column("colPU", width=72, anchor=CENTER)
tvFactura.column("colPT", width=73, anchor=CENTER)

tvFactura.heading("#0", text="DESCRIPCIÓN", anchor=CENTER) #Definir el titulo de los encabezados de cada columna
tvFactura.heading("colC", text="CANTIDAD", anchor=CENTER)
tvFactura.heading("colPU", text="PRECIO U", anchor=CENTER)
tvFactura.heading("colPT", text="PRECIO T.", anchor=CENTER)

tvFactura.insert("", END, text = "Perro", values=("2", "$18.000", "$36.000"))
tvFactura.insert("", END, text = "Gaseosa", values=("2", "$2.000", "$4.000"))
tvFactura.insert("", END, text = "Gaseosa", values=("2", "$2.000", "$4.000"))

style = ttk.Style()
style.configure("Treeview", font=fuenteF, rowheight=40)
style.configure("Treeview.Heading", font=fuenteF2, padding=10)
style.layout("Treeview", [("Treeview.border", None)])



#####FUNCIONES PARA CUANDO SE TENGA EL CURSO ENCIMA O NO DE LOS BOTONES####

bBuscar.bind("<Enter>",lambda event: hover(3)) #Cursor sobre el boton
bBuscar.bind("<Leave>",lambda event: over(3))  #Cursor fuera del boton
bAgregar.bind("<Enter>",lambda event: hover(4))
bAgregar.bind("<Leave>",lambda event: over(4))
bDevuelto.bind("<Enter>",lambda event: hover(5))
bDevuelto.bind("<Leave>",lambda event: over(5))
bVenta.bind("<Enter>",lambda event: hover(6))
bVenta.bind("<Leave>",lambda event: over(6))
bFactura.bind("<Enter>",lambda event: hover(7))
bFactura.bind("<Leave>",lambda event: over(7))
bBorrar.bind("<Enter>",lambda event: hover(8))
bBorrar.bind("<Leave>",lambda event: over(8))
bSalir.bind("<Enter>",lambda event: hover(9))
bSalir.bind("<Leave>",lambda event: over(9))

#####COLOCAR ELEMENTOS DE LA VENTANA FACTURACIÓN####
cbProducto.place(x = 240, y =140)
bBuscar.place(x = 240, y =200)
lPrecio.place(x = 175, y =295)
lNombre.place(x = 200, y =262)
eCantidad.place(x = 420, y =350)
bAgregar.place(x = 75, y =415)

eDevuelto.place(x = 240, y =547)
bDevuelto.place(x = 200, y =600)
lDevuelto.place(x = 340, y =650)

lSubtotal.place(x = 850, y =483)
lDescuento.place(x = 890, y =537)
lTotal.place(x = 790, y =590)
bVenta.place(x = 687, y =645)

bFactura.place(x = 1070, y =480)
bBorrar.place(x = 1070, y =550)
bSalir.place(x = 1070, y =620)

tvFactura.place(x = 675, y =20, width=650, height=350)





################ELEMENTOS VENTANA DE STOCK###########

################IMAGEN DE FONDO###########

imagenBg3= PhotoImage(file="bg3.png")
canvasBg3 = Canvas(ventana3, width = 1344, height = 756)
canvasBg3.pack(fill = "both", expand = True)
canvasBg3.create_image( 9, 0, image = imagenBg3, anchor = "nw")









################IMAGENES###########

bImgBuscarStock = PhotoImage(file = "btnBuscarStock.png") #Imagen del boton "Buscar"
bImgBuscarStockClick = PhotoImage(file = "btnBuscarStockClick.png") #Imagen del boton "Buscar" en click
bImgStock = PhotoImage(file = "btnStock.png") #Imagen del boton "Lista de stock"
bImgStockClick = PhotoImage(file = "btnStockClick.png")  #Imagen del boton "Lista de stock" en click
bImgAgregarStock = PhotoImage(file = "btnAgregarStock.png") #Imagen del boton "Agregar Stock y precio"
bImgAgregarStockClick = PhotoImage(file = "btnAgregarStockClick.png") #Imagen del boton "Agregar Stock y precio" en click
bImgSalirStock = PhotoImage(file = "btnSalirStock.png") #Imagen del boton "Agregar Stock y precio"
bImgSalirStockClick = PhotoImage(file = "btnSalirStockClick.png") #Imagen del boton "Agregar Stock y precio" en click

################ELEMENTOS###########

cbProducto2 = ttk.Combobox(canvasBg3, values=["Hamburguesa", "Salchipapa", "Perro", "Arepa con todo", "Gaseosa", "Jugo Hit", "Agua", "Cerveza"], width=35, state="readonly", font=fuenteCB)
bBuscarStock = Button(canvasBg3, image=bImgBuscarStock, borderwidth =0, highlightthickness=0, bd=0, bg="#EDEDED",relief=FLAT, command = buscarStock)
bStock = Button(canvasBg3, image=bImgStock, borderwidth =0, highlightthickness=0, bd=0, bg="#EDEDED",relief=FLAT, command = listaStock)
lCantidad = Label(canvasBg3, text="", font=fuenteD, background="#EDEDED", foreground="#373F51") #Texto de la cantidad actual del producto buscado 
lPrecioAc = Label(canvasBg3, text="", font=fuenteD, background="#EDEDED", foreground="#373F51") #Texto del precio actual del producto buscado

eCantidadN = Entry(canvasBg3, background="white", foreground= "#373F51", font=fuenteC, width=12, relief=SUNKEN, justify="center", insertbackground="#373F51", highlightbackground="#9F9D9D", highlightcolor="#373F51", highlightthickness=1)
ePrecio = Entry(canvasBg3, background="white", foreground= "#373F51", font=fuenteC, width=13, relief=SUNKEN,  justify="center", insertbackground="#373F51", highlightbackground="#9F9D9D", highlightcolor="#373F51", highlightthickness=1)
bAgregarStock = Button(canvasBg3, image=bImgAgregarStock, borderwidth =0, highlightthickness=0, bd=0, bg="#EDEDED",relief=FLAT, command = agregarStock)
bSalirStock = Button(canvasBg3, image=bImgSalirStock, borderwidth =0, highlightthickness=0, bd=0, bg="#EDEDED",relief=FLAT, command=lambda: salir(ventana1))

#####FUNCIONES PARA CUANDO SE TENGA EL CURSO ENCIMA O NO DE LOS BOTONES####

bBuscarStock.bind("<Enter>",lambda event: hover(10)) #Cursor sobre el boton
bBuscarStock.bind("<Leave>",lambda event: over(10))  #Cursor fuera del boton
bStock.bind("<Enter>",lambda event: hover(11))
bStock.bind("<Leave>",lambda event: over(11))  
bAgregarStock.bind("<Enter>",lambda event: hover(12))
bAgregarStock.bind("<Leave>",lambda event: over(12))  
bSalirStock.bind("<Enter>",lambda event: hover(13))
bSalirStock.bind("<Leave>",lambda event: over(13))  

#####COLOCAR ELEMENTOS DE LA VENTANA FACTURACIÓN####

cbProducto2.place(x = 440, y =248)
bBuscarStock.place(x = 390, y =315)
bStock.place(x = 750, y =315)
lCantidad.place(x = 480, y =413)
lPrecioAc.place(x = 940, y =413)

eCantidadN.place(x = 480, y =518)
ePrecio.place(x = 465, y =588)
bAgregarStock.place(x = 800, y =495)
bSalirStock.place(x = 800, y =565)

#####COLOCAR LAS 3 VENTANAS PRINCIPALES####
ventana1.place(x=0, y=0, width=1344, height=756)  #INICIO
ventana2.place(x=0, y=0,width=1344, height=756)   #FACTURACIÓN 
ventana3.place(x=0, y=0,width=1344, height=756)   #STOCK


salir(ventana1) #Mostrar la ventana de inicio al empezar el programa

ventana.mainloop()
