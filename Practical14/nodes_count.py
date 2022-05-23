import matplotlib.pyplot as plt
import xml.dom.minidom
from numpy import*

def find_parents(node_id, parent_ids):
    immediate_parent_ids = node_map[node_id]
    if len(immediate_parent_ids):
        for immediate_parent_id in immediate_parent_ids:
            parent_ids.add(immediate_parent_id)
            find_parents(immediate_parent_id, parent_ids)

nodes = xml.dom.minidom.parse("/Users/yefen/IBI1_2021-22/Practical14/go_obo.xml").documentElement.getElementsByTagName("term")
print("There are", len(nodes), "terms in go_obo.xml")
node_map = {}
result = {}
resu = []
judge=[]
pic=[]
for node in nodes:
    node_id = node.getElementsByTagName("id")[0].childNodes[0].data
    immediate_parent_ids = []
    for is_a in node.getElementsByTagName("is_a"):
        immediate_parent_ids.append(is_a.childNodes[0].data)
    node_map[node_id] = immediate_parent_ids
    if node.getElementsByTagName("defstr")[0].childNodes[0].data.find("translation") != -1:
        judge.append(1)
    else:
        judge.append(0)
    result[node_id] = 0

for key in node_map.keys():

    parent_ids = set()
    find_parents(key, parent_ids)
    for parent_id in parent_ids:
        result[parent_id] += 1

for i, (k, v) in enumerate(result.items()):
    resu.append(v)
    if judge[i]==1:
        pic.append(v)

plt.boxplot(result.values(), vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=True)
plt.title('Distribution of child node number of all GO terms')
plt.xlabel("all GO terms")
plt.ylabel("Number")
plt.show()
plt.boxplot(pic, vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=True)
plt.title('Distribution of child node number of terms associated with ‘translation’')
plt.xlabel("associated with ‘translation’")
plt.ylabel("Number")
plt.show()

if mean(pic)<mean(resu):
	print("the translation terms contain, on average, a smaller number of child nodes than the overall Gene Ontology")
elif mean(pic)>mean(resu):
	print("the translation terms contain, on average, a greater number of child nodes than the overall Gene Ontology")
else:
	print ("They contain an equal number of average child nodes")
#comment: The "translation" terms contain, on average, a greater number of child nodes than the overall Gene Ontology
