print('Enter "q" to Quit')
conti = True
while(conti):
    input_str = input("Enter String: ")
    bracket_front = 0
    bracket_back = 0
    rpt_front = []
    rpt = ""
    cnt = -1
    if input_str == "q":
        conti = False
        break
    for char in input_str:
        cnt = cnt + 1
        if char == "(":
            rpt = rpt + " "
            bracket_front = bracket_front + 1
            rpt_front.append(cnt)
        elif char == ")":
            bracket_back = bracket_back + 1
            if bracket_back > bracket_front:
                rpt = rpt + "?"
                bracket_back = bracket_back - 1
            else:
                rpt = rpt + " "
                bracket_back = bracket_back - 1
                bracket_front = bracket_front - 1
        else:
            rpt = rpt + " "

    while bracket_front > 0:
        index = rpt_front.pop()
        rpt = rpt[0:index] + "x" + rpt[index+1:len(rpt)]
        bracket_front = bracket_front - 1

    print(input_str)
    print(rpt)