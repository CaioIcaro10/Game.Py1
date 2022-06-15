from Models.calculate import Calculate


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    print('***' * 10, 'GAMEPY', '***' * 10, '\n')
    dificuldade: int = int(input('set the difficulty [1, 2, 3, 4]: '))
    if dificuldade > 5:
        print(f'\nYou Choose the difficulty number {dificuldade}\n')
    elif dificuldade >= 5:
        print('SO YOU HAVE CHOSEN DEATH!!!\n')

    calc: Calculate = Calculate(dificuldade)

    print('Show the results of the next operation')
    calc.show_operation()

    resultado: int = int(input(''))

    if calc.generate_results == resultado:
        pontos += 1
        print(f'You have {pontos} points')

    continuar: int = int(input('Want to Continue? [1 = Yes! / 0 = No!] '))

    if continuar:
        jogar(pontos)
    else:
        print(f'You have done the GamePy with {pontos} points')
        print('Until Next Time!')


if __name__ == '__main__':
    main()
