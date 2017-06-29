import difflib


def get_list(fname):
    with open(fname, 'r') as f:
        return [i.strip() for i in f.readlines()]


old = r242 = get_list('r242_sorted.gcode')
new = b561 = get_list('b561_sorted.gcode')

