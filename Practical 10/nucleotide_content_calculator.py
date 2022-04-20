# nucleotide content calculator
#creat the function
def percentage_of_nucleotides (i):
    i=i.upper()  #to let the function recognice both upper and lower canses
    count= len(i)
    res=str(i)
    count_A= res.count('A')      #count the number then caulate the percentage
    print("the percentage of A is",count_A/count )
    count_T = res.count('T')
    print("the percentage of T is", count_T/ count)
    count_c = res.count('C')
    print("the percentage of C is", count_c / count)
    count_G = res.count('G')
    print("the percentage of G is", count_G/ count)
i='GattccGGGAAATTTCcattttg'       #a example
i=input()
percentage_of_nucleotides (i)
