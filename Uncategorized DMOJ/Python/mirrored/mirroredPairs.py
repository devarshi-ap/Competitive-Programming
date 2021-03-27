print('Ready')

while True:
    letters = input()
    if not letters.strip():
        break
    elif letters == 'qp' or letters == 'db' or letters == 'pq' or letters == 'bd':
        print("Mirrored pair")
    else:
        print("Ordinary pair")
