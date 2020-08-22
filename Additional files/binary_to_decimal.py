def bin_to_dec(bin_input):
    new_dec = 0
    j = len(str(bin_input))
    for i in range(j):
        new_dec += int(str(bin_input)[i]) * (2 ** (j - i - 1))
    print(new_dec)

bin_to_dec(10000001)
