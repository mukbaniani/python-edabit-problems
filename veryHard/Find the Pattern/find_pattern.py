def find_pattern(dict_, p):
    result_list = []
    for keys, value in dict_.items():
        if p in value:
            result_list.append(f'{keys} = {p}')
        else:
            result_list.append(f'{keys} = None')
    return result_list
