from random import randint


class Calculate:
    def __init__(self: object, dificult: int):
        self.__dificult: int = dificult
        self.__value1: float = self.generate_value
        self.__value2: float = self.generate_value
        self.__operations: int = randint(1, 3)  # 1 = Somar / 2 = Diminuir / 3 = Multiplicar
        self.__results: float = self.generate_results


    @property
    def dificult(self: object) -> int:
        return self.__dificult

    @property
    def value1(self: object) -> int:
        return self.__value1

    @property
    def value2(self: object) -> int:
        return self.__value2

    @property
    def operations(self: object) -> int:
        return self.__operations

    @property
    def results(self: object) -> int:
        return self.__results

    def __str__(self: object) -> str:
        op: str = ' '
        if self.operations == 1:
            op = 'Somar'
        elif self.operations == 2:
            op = 'Diminuir'
        elif self.operations == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação Desconhecida'
        return f'Valor1 {self.value1} \nValor2: {self.value2} \nDificult: {self.dificult} \nOperation: {op}'

    @property
    def generate_value(self: object) -> int:
        if self.dificult == 1:
            return randint(0, 10)
        elif self.dificult == 2:
            return randint(0, 50)
        elif self.dificult == 3:
            return randint(0, 100)
        elif self.dificult == 4:
            return randint(0, 1000)
        else:
            return randint(100000, 1000000)

    @property
    def generate_results(self: object) -> bool:
        if self.operations == 1:
            return self.value1 + self.value2
        elif self.operations == 2:
            return self.value1 - self.value2
        else:
            return self.value1 * self.value2

    def _op_symbols(self: object) -> str:
        if self.operations == 1:
            return '+'
        elif self.operations == 2:
            return '-'
        else:
            return '*'

    def check_results(self: object, answer: int) -> bool:
        certo: bool = False

        if self.results == answer:
            print('Correct Answer!!')
            certo = True
        else:
            print('Wrong Answer')
        print(f'{self.value1} {self._op_symbols()} {self.value2} = ? ')
        return certo

    def show_operation(self: object):
        print(f'{self.value1} {self._op_symbols()} {self.value2} ' )
