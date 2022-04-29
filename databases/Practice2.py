# Comparing a list to values in a dictionary
my_list = [1, 22, 3, 5, 42]
my_dict = {"one":1, "three":3, "forty two":42, "seventeen":17}

for item in my_list:
    if item == item in my_dict.values():
        print(item)

