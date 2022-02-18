def loves_me(n):
    loves_me_list = ['Loves me, ' if i % 2 == 0 else 'Loves me not, ' for i in range(n)]
    if loves_me_list:
        loves_me_list[-1] = loves_me_list[-1].upper().replace(', ', '')
        return ''.join(loves_me_list)
