def is_palindrome(data):
    data_str = str(data)
    #print(data)
    #print(data_str)

    # convert str to list
    data_lst = []
    for ch in data_str:
        data_lst.append(ch)
    #print(data_lst)

    # create a reverse list
    rev_list = []
    for index in range(len(data_lst) - 1, -1, -1):
        rev_list.append(data_lst[index])
    #print(rev_list)

    if data_lst == rev_list:
        return True
    else:
        return False
