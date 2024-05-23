def calculate_structure_sum(*args):
    s = 0
    for x in args:

        if isinstance(x, (int, float)):
            s += x
        elif isinstance(x,str):
            s += len(x)
        elif isinstance(x,list):
            s += calculate_structure_sum(*x)
        elif isinstance(x, tuple):
            s += calculate_structure_sum(*x)
        elif isinstance(x, set):
            s += calculate_structure_sum(*x)
        elif isinstance(x, dict):
            s += calculate_structure_sum(list(x.items()))
        else:
            print(x, type(x),'xo-xo')
    return s


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)