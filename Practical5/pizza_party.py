n=0
active = True  #set a judje variable
while active:  #set while-loop to increase until p>=64 
    p = (n * n + n + 2) / 2 #set the equation of p
    if p<64:     
        n = n+1 
        print(n,p) #print slices for each number of straight cuts
    else:
        print("the enough pieces is", n) #print final correct answer
        active = False
