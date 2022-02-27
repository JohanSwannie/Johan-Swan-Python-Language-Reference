
def convert_Bin_toDecimal(bin_String):
    res = 0
    chkin = ('0', '1')
    bin_List = list(bin_String)
    for chk in bin_List:
        if chk in chkin:
            continue
        else:
            return "The Binary String consists of NON Binary Digits"
    print('list is : ', bin_List)
    rev_Bin_List = bin_List[::-1]
    for bitty in range(len(rev_Bin_List)):
        res += int(rev_Bin_List[bitty]) * (2 ** bitty)
    return res

x = 1
go = True
ret_Msg = "The Result after the Conversion Process is : "
except_List = ['Y', 'y', 'YES', 'Yes', 'yes']
d1 = 'a'
d2 = 'another'

while go:
    if input("\n {0})Do you want to do {1} conversion from binary to decimal? : ".format(x, d1 if x == 1 else d2)).strip() in except_List:
        print(ret_Msg + str(convert_Bin_toDecimal(input("\nProvide your Binary digits : "))))
    else:
        print("\nHave a nice day Mate")
        go = False
    x += 1

