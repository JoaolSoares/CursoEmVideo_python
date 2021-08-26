def maior(*nums):
    maiornum = 0
    for c, n in enumerate(nums):
        if c == 0:
            maiornum = n
        else:
            if n > maiornum:
                maiornum = n

    print(f'{nums} são {len(nums)} valores ao todo')
    print(f'O maior valor é o {maiornum}')
    print('-=' * 20)


maior(10, 6, 3, 4, 89, 5, 3, 9, 77)
maior(5, 3, 7, 10, 55, 44)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
