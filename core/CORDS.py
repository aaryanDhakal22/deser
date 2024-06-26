CORD_PASSKEY = [840, 644]
CORD_ENTER = [928, 756]
CORD_DISPATCH = [979, 291]

addr_cords = []

x = 710
y = 425
l = 125
b = 15
for i in range(5):
    addr_cords.append([y, y + b, x, x + l])
    y += 45


print(addr_cords)
