
def update_dictionary(d, key, value):
    d = {}
    # key = input()
    # value = input()
    if key in d.keys():
        d.update(key,value)
        # print(d)
    else:
        if key is not d.keys() and key*2 in d.keys():
            d.setdefault(key, value*2)
        if key is not d.keys() and key*2 is not d.keys():
            d.setdefault(2*key, value)
    print(d)
    return update_dictionary(2,3,5)

        # d.setdefault(2*key, value)
        # print(d)
    # put your python code here

