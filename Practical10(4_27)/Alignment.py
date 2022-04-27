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
# in this data we can know that the mouse's amino acid sequence is similar to the human's which showings a close species affinity.
# Only minor changes in amino acid sequences occured during biological evolution.
