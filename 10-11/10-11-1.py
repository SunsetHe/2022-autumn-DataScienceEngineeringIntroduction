def mao_pao(num_list):
    num_len = len(num_list)
    for j in range(num_len):
        sign = False
        for i in range(num_len - 1 - j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                sign = True
            if not sign:
                break


a = [5,4,3,2,1]

