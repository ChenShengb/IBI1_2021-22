with open('/Users/yefen/IBI1_2021-22/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') as a:
    fout=open('/Users/yefen/IBI1_2021-22/Practical8/cut_genes.fa','w') #output the results in a new fasta file
    # I got help from mt classmate Xu Ziyi to indentify genes
    EcoRI = 'GAATTC'
    order = 0
    seqs = []
    gene_name = []
    for line in a:        #to indentify each gene name
        if line.startswith('>'):
            gene_name.append(line)   #add gene name to the list
            order = order + 1
        if (line.startswith('>')) and (order != 1):   #order started from 0,
            gene = ''
            for seq in seqs:
                gene = gene + str(seq) #add sequence and delete return
            seqs = [] #remove the content in the seqs for the next cycle
            i = 0
            judge = True   #to indentify sequence with "GAATTC"
            while (i <= len(gene) - 5) and judge:
                i = i + 1
                if gene[i:i + 6] == EcoRI:
                    judge = False #Exit loop if find the sequence
                    name = gene_name[order-2]
                    d= re.findall(r'gene:(\S+)',name) #identify the gene name
                    a=str(d)+'      '
                    b=str(len(gene))+'\n'
                    c=(gene)+'\n'
                    line1=a
                    line2=b
                    line3=c
                    fout.write(line1)     #write the file
                    fout.write(line2)
                    fout.write(line3)
        if not line.startswith('>'):
            seqs.append(line.replace('\n', '')) #to delete return back

