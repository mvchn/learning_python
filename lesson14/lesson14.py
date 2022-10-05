variable = 1


def print_variable(v):
    print(v)


if variable > 1:
    print_variable("More 1")
else:
    print_variable("Less or = 1")

while variable < 4:
    print_variable('Loop ...')
    variable += 1

print_variable(variable)
