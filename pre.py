class Matriz():
    def __init__(self, n_mat, col, fil, opc):
        self.n_mat = n_mat
        self.col = col
        self.fil = fil
        self.__crear()
        if opc==1:
            self.__sumar()
        elif opc==2:
            self.__restar()
        elif opc==3:
            self.__multiplicar()
        else:
            self.__dividir()
    def __crear(self):
        for i in range(1):
            print("Matriz n°: 1")
            self.main = []
            for x in range(self.fil):
                print(f"Ingresar fila n°: {x}")
                u = []
                for y in range(self.col):
                    n = int(input(f"Ingresar Posicion: {x}, {y}: "))
                    u.append(n)
                self.main.append(u)  
    def __sumar(self):
        i=2
        for z in range(self.n_mat-1):
            print(f"Matriz n°: {i}")
            for x in range(self.fil):
                print(f"Ingresar fila n°: {x}")
                for y in range(self.col):
                    n = int(input(f"Ingresar Posicion: {x}, {y}: "))
                    self.main[x][y] += n
            i += 1
        for i in self.main:
            print(i)
    def __restar(self):
        i=2
        for z in range(self.n_mat-1):
            print(f"Matriz n°: {i}")
            for x in range(self.fil):
                print(f"Ingresar fila n°: {x}")
                for y in range(self.col):
                    n = int(input(f"Ingresar Posicion: {x}, {y}: "))
                    self.main[x][y] -= n
            i+=1
        for i in self.main:
            print(i)
    def __multiplicar(self):
        i = 2
        r = []
        for z in range(self.n_mat-1):
            print(f"Matriz n°: {i}")
            f = int(input("Ingrese el numero de filas: "))
            self.c = int(input("Ingrese el numero de columnas: "))
            if self.c == self.fil or f==self.col:
                for x in range(self.c):
                    print(f"Ingresar columna n°: {x}")
                    res = 0
                    j = []
                    for y in range(f):
                        n = int(input(f"Ingresar Posicion: {y}, {x}: "))
                        j.append(n)          
                    r.append(j)
                i+=1
            else:
                print("Multiplicacion no valida")
                break
        for x in self.main:
            res = []
            for y in range(self.c):
                l = [a*b for a,b in zip(x, r[y])]
                res.append(sum(l))
            print(res)
    def __dividir(self):
        n = int(input("Ingresar escalar: "))
        for x in range(self.fil):
            for y in range(self.col):
                self.main[x][y] = self.main[x][y]/n
        for i in self.main:
            print(i)



def main():
    n_mat = int(input("Ingrese el numero de matrices: "))
    opc = int(input("1: Sumar | 2: restar | 3: Multiplicar | 4:Dividir "))
    if opc != 3:
        col = int(input("Ingrese el numero de columnas: "))
        fil = int(input("Ingrese el numero de filas: "))
    else:
        col = int(input("Ingrese el numero de columnas de la primera matriz: "))
        fil = int(input("Ingrese el numero de filas de la primera matriz: "))
    matriz = Matriz(n_mat, col, fil, opc)
main()

        


