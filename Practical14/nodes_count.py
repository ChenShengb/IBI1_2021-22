from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import matplotlib.pyplot as plt

# read and parse the go_obo.xml using DOM that I learned in the Monday IBI CLass
DOMTree =xml.dom.minidom.parse("/Users/yefen/IBI1_2021-22/Practical14/go_obo.xml")
collection = DOMTree.documentElement
terms= collection.getElementsByTagName("term")
print('the total number of terms:', len(terms)) # to show the total number of terms

# define a function that count the childnotes of terms and subtract a subset of duplicates
def sum_nodes(id):       # Consistent internal and external variables
    global childNodes_term, childNodes_term_nore
    for j in range(len(is_a_all)):
        for k in range(len(is_a_all[j])):
            if is_a_all[j][k] == id:   #this means term has a childnote
                childNodes_term.append(id_all[j])
                sum_nodes(id_all[j])
    for l in childNodes_term:
        if l not in childNodes_term_nore:
            childNodes_term_nore.append(l)
id_all=[]
is_a_all=[]
for i in range(len(terms)):
    is_a= terms[i].getElementsByTagName("is_a") #to find the is_a line
    id_all.append(terms[i].getElementsByTagName("id")[0].childNodes[0].data)#to find the id line
    is_a_all.append([])
    # add the is_a in a term
    for j in range(len(is_a)):
        is_a_all[i].append(terms[i].getElementsByTagName("is_a")[j].childNodes[0].data)
term_childNodes_all=[]
translation=[]
for i in range(len(id_all)):
        childNodes_term=[]
        childNodes_term_nore=[]
        # count the childnotes
        sum_nodes(id_all[i])
        term_childNodes_all.append(len(childNodes_term_nore))
#to get the translation related terms
        if terms[i].getElementsByTagName("defstr")[0].childNodes[0].data.find("translation") != -1:
            translation.append(len(childNodes_term_nore))
plt.boxplot(term_childNodes_all)
plt.title=('distribution of child nodes across terms')
plt.xlabel=("all terms in GO")
plt.ylabel=('number')
plt.show()
plt.boxplot(translation)
plt.title=('distribution of child nodes across terms associated with translation')
plt.xlabel=('related to translation')
plt .ylabel=('number')
plt.show()
a= sum(term_childNodes_all )/len(term_childNodes_all)
b=sum(translation)/len(translation)
if a > b:
    print('The translation terms contain, on average, a lower number of childnodes than the overall Gene Ontology.')
else:
    print('The translation terms contain, on average, a greater number of childnodes than the overall Gene Ontology.')
