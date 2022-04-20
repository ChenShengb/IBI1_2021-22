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

i=input()
percentage_of_nucleotides (i)
# I use'ATTccg' for example. The results were 
# the percentage of A is 0.16666666666666666
# the percentage of T is 0.3333333333333333
# the percentage of C is 0.3333333333333333
# the percentage of G is 0.16666666666666666
