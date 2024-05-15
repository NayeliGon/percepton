class Perceptron:
    def __init__(self):
        self.w0 = 0.5
        self.w1 = 0.3
        self.w2 = 0.4
        self.entrenado = False

    def evaluar(self, x1, x2):
        w0 = -3.4
        w1 = 2.5
        w2 = 1.4

        neti = x1 * w1 + x2 * w2 + w0
        if neti >= 0:
            return 1
        else:
            return 0

    def entrenar(self):
        mat = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1]
        ]

        while not self.entrenado:
            self.entrenado = True
            for i in range(4):
                neti = mat[i][0] * self.w1 + mat[i][1] * self.w2 + self.w0
                if neti >= 0:
                    sp = 1
                else:
                    sp = 0
                er = mat[i][2] - sp
                if er != 0:
                    self.entrenado = False
                    self.w0 += er * 1
                    self.w1 += er * mat[i][0]
                    self.w2 += er * mat[i][1]

        print("Entrenamiento completado.")
        print("w0 =", self.w0)
        print("w1 =", self.w1)
        print("w2 =", self.w2)

# Uso del perceptrón
if __name__ == "__main__":
    perceptron = Perceptron()
    perceptron.entrenar()

    x1 = int(input("Introduce el valor de x1: "))
    x2 = int(input("Introduce el valor de x2: "))

    resultado = perceptron.evaluar(x1, x2)
    print("Resultado:", resultado)
