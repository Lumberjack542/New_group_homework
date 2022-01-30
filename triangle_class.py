class TriangleCheker():
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def is_triangle(self):
        if f"{self.num1}".isalpha() or f"{self.num2}".isalpha() or f"{self.num3}".isalpha():
            return 'Нужно вводить только числа !'

        elif int(self.num1) < 0 or int(self.num2) < 0 or int(self.num3) < 0:
            print('С отрицательными числами ничего не выйдет !')

        elif int(self.num1) + int(self.num2) > int(self.num3):
            if int(self.num3) + int(self.num2) > int(self.num1):
                if int(self.num3) + int(self.num1) > int(self.num2):
                    return 'Ура, можно построить'

        else:
            return f'Жаль, но из этого треугольник не сдлеать'


site1 = input()
site2 = input()
site3 = input()


example = TriangleCheker(site1, site2, site3)

print(example.is_triangle())