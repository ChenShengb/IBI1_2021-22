# read the sequence of each file
a = open('/Users/yefen/IBI1_2021-22/Practical10(4_27)/DLX5_human.fa')
b = open('/Users/yefen/IBI1_2021-22/Practical10(4_27)/RandomSeq(1).fa')
c = open('/Users/yefen/IBI1_2021-22/Practical10(4_27)/DLX5_mouse.fa')
seq_human=[]
seq_random=[]
seq_mouse=[]
#add each sequence and delete the return
for line in a:
    line= line.replace('\n','')
    if not line.startswith('>'):
        seq_human += line
for line in b:
    line= line.replace('\n','')
    if not line.startswith('>'):
        seq_random += line
for line in c:
    line= line.replace('\n','')
    if not line.startswith('>'):
        seq_mouse += line
edit_distance_huamn = 0 #set initial distance as zero
edit_distance_random=0
for i in range(len(seq_mouse)):       #compare each amino acid
    if seq_mouse[i]!=seq_human[i]:
        edit_distance_huamn += 1 #add a score 1 if amino acids are different
for i in range(len(seq_mouse)):
    if seq_mouse[i]!=seq_random [i]:
        edit_distance_random +=1
e= edit_distance_random/len(seq_mouse)    #culcalate the percentage of identical amino acid compraing with the mouse
e= (1-e)*100
f= edit_distance_huamn/len(seq_mouse)
f=(1-f)*100
print ('the difference between mouse and random is', edit_distance_random, 'the percentage of identical amino acids is',e,'%')
print ('the difference between human and mouse is',  edit_distance_huamn,'the percentage of identical amino acids is',f,'%')
#  the code of geting scores
amino_acid=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*']    #set the list of amino acid
# set the list of score row and index
BLOSUM62 = [
            [ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
            [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
            [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
            [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
            [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
            [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
            [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
            [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
            [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
            [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
            [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
            [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
            [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
            [ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
            [ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
            [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
            [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
            [ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
            [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
            [-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
            [ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
            [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],]
# a function to get the score between two sequence
def blo_score(s1,s2):
    blosum_score=0
    for i in range(len(seq_mouse)):
        index1=amino_acid.index(s1[i])
        index2=amino_acid.index(s2[i])
        blosum_score=blosum_score+BLOSUM62[index1][index2]   #Add up the scores of each amino acid one by one
    return blosum_score
x=blo_score(seq_mouse,seq_human)
y=blo_score(seq_mouse,seq_random)
z=blo_score(seq_human,seq_random)
print('The BLOSUM score between mouse and human is:',x)
print('The BLOSUM score between mouse and random is:',y)
print('The BLOSUM score between random and human is:',z)
# in this data we can know that the mouse's amino acid sequence is similar to the human's which showings a close species affinity.
# Only minor changes in amino acid sequences occured during biological evolution.
