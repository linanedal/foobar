def solution(s):


    def splits(list, size):
        # split list into chunks of the same size
        for i in range(0, len(list), size):
            yield list[i:i + size]

    def checklength(list):
        check = iter(list)
        length = len(next(check))
        if not all(len(l) == length for l in check):
            sol_options = [1]
            return sol_options
        else:
            return "same length"

    def checkcontent(list):
        check = iter(list)
        content = next(check)
        if not all(l == content for l in check):
            return "not identical"
        else:
            return "identical"

    # make an m&m list
    mm_list = list(s)
    firstchar = mm_list[0]
    # make solution options list
    sol_options = []


    i = 1 # counter, start at 1

    while i < len(mm_list):

        if mm_list[i]==firstchar:

            mm_generator = splits(mm_list, i)

            mm_splits = [m for m in mm_generator]

            lengthresult = checklength(mm_splits)
            contentresult = checkcontent(mm_splits)

            if lengthresult == "same length":
                if contentresult == "identical":
                    sol_option = len(mm_splits)
                    sol_options.append(sol_option)
                    break
            else:
                sol_options = lengthresult

        i += 1

    return max(sol_options)




solution('abcabcabcabc')
solution('abccbaabccba')
solution('abababc')

    # for i in range(len(mm_list)):
    #     if mm_list[i]!=firstchar:
    #         print(mm_list[i], firstchar)
    #         print("False")
    #     else:
    #         print(mm_list[i], firstchar)
    #         print("True")

    # eg. string is len()=24.
    # search for patterns of 2 and 3 (2*2*2*3 = 24)
    # then search for patterns of 4, 6, 8, 12, 24 (and of course 1)
    # these are all factors of 24
