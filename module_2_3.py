my_list_ = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list_):
    if my_list_[a] < 0:
        break
    if my_list_[a] > 0:
        print(my_list_[a])
    a += 1