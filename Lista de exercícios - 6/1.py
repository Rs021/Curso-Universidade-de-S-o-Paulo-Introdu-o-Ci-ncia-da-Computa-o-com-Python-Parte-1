def remove_repetidos(lst):
    return list(sorted(dict.fromkeys(lst)))
    