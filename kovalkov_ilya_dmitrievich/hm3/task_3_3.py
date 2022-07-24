#   3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

name = 'Ivanou Ivan'

first_name = name[name.find(' ')+1:]
last_name = name[:name.find(' ')+1]

print(f'{first_name + " " + last_name}')
