def num_romanos(num):
    if 3 < num <= 5:
        res = (5 - num) * 'I' + 'V'
    elif  num > 5:
        res = 'V' + (num-5) * 'I'
    elif 0 <= num <= 3:
        res = num * 'I'
    else:
        print(f"não sei converter {num}!")
    return res
