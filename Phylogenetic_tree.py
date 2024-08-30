from Bio import Entrez, Phylo, AlignIO
from Bio.Align.Applications import ClustalwCommandline


Entrez.email = "63050411@kmitl.ac.th"  # ต้องใส่อีเมลตัวเองนะ

# Step 2: ดึงข้อมูลลำดับพันธุกรรมของ
def fetch_primate_sequences(max_records=5):
    handle = Entrez.esearch(db="nucleotide", term="Primates[Organism]", retmax=max_records)
    record = Entrez.read(handle)
    handle.close()
    
    id_list = record["IdList"]
    handle = Entrez.efetch(db="nucleotide", id=id_list, rettype="fasta", retmode="text")
    sequences = handle.read()
    handle.close()
    return sequences

# ดึงข้อมูลลำดับพันธุกรรม
primates_sequences = fetch_primate_sequences()

# Step 3: บันทึกข้อมูลลงไฟล์ .fasta
with open("primates_sequences.fasta", "w") as file:
    file.write(primates_sequences)

# Step 4: จัดเรียงลำดับพันธุกรรมโดยใช้ ClustalW
clustalw_exe = "/Panuwid/Desktop/clustalw2"  # ระบุพาธของโปรแกรม ClustalW
clustalw_cline = ClustalwCommandline(clustalw_exe, infile="primates_sequences.fasta")
stdout, stderr = clustalw_cline()

# Step 5: อ่านไฟล์
alignment = AlignIO.read("primates_sequences.aln", "clustal")

# Step 6: สร้างtree
tree = Phylo.read("primates_sequences.dnd", "newick")

# Step 7: แสดงผล
Phylo.draw(tree)
