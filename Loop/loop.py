list_a = [0.0025956, 0.0015444, 0.0011628, 0.0010404, 0.0010728, 0.0011052, 0.0013356, 0.0021564, 0.0030816,
                    0.004968, 0.006804, 0.008568, 0.010224, 0.013284, 0.016092, 0.02718, 0.04356, 0.05796, 0.07236, 0.0864]
list_energy = [0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.1,
                0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1, 2, 4, 6, 8, 10]


d = {'Kair': list_a, 'Energy': list_energy}

def loop_dict():
    for i, (key, list_value) in enumerate(d.items()):
        print(i, key)
        for value in list_value:
            print(value)

loop_dict()