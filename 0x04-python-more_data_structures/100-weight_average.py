def weight_average(my_list=[]):
    if not my_list:
        return None

    n = 0
    d = 0
    for i in my_list:
            n += (i[0] * i[1])
            dem += i[1]
        return (n/ d)
