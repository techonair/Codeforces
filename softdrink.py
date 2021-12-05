n, k, l, c, d, p, nl, np = input().split()

drink_quant = int(k)*int(l)
n_drink_toast = drink_quant / int(nl)

lime_slices = int(c)*int(d)

n_salt_toast = int(p) / int(np)

# toast per friend
print(int(min(n_drink_toast, lime_slices, n_salt_toast) / int(n)))