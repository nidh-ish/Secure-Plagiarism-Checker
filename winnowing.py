import nltk
import sys
import math
import pickle
from nltk import word_tokenize
from nltk.util import ngrams
from nltk import cluster
from collections import Counter
from statistics import mean
import networkx as nx
import random
from bitarray import bitarray
from bitarray.util import *
from fpv import *
import sys
from generate_ast import *
import csv


class Winnowing:

    def Write2File(self, f0, f1, f2, inp1, v1):
        L = len(inp1)
        f0.write(f"{L}\n")
        f1.write(f"{L}\n")
        f2.write(f"{L}\n")
        for i in range(L):
            l1 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
            l2 = bitarray(bin(random.getrandbits(128))[2:].zfill(128))
            m = l1 ^ l2 ^ inp1[i] 
            f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
            f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
            f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")

        for i in range(L):
            l1 = int2ba(random.randint(0, 2**61 - 2), length=61)
            l2 = int2ba(random.randint(0, 2**61 - 2), length=61)
            m = int2ba((ba2int(l1) + ba2int(l2) + v1[i])%(2**61-1), length=61) 
            f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
            f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
            f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")
        s = 0
        for i in v1:
            s += i**2
        s = math.sqrt(s)
        s = 1/s
        fpv = FPVArithmetic()
        zmessage = None
        if s == 0.0:
            zmessage = bitarray("1")
        else:
            zmessage = bitarray("0")
        m = fpv.float_to_bin(s)
        smessage = bitarray(m[0:1])
        pmessage = bitarray(m[1:9])
        vmessage = bitarray("1" + m[9:])
        s = [vmessage, pmessage, zmessage, smessage]
        for i in s:
            l1 = int2ba(random.randint(0, 2**61 - 2), length=61)
            l2 = int2ba(random.randint(0, 2**61 - 2), length=61)
            m = int2ba((ba2int(l1) + ba2int(l2) + ba2int(i))%(2**61-1), length=61) 
            f0.write(f"{ba2base(2, l1)} {ba2base(2, l2)}\n")
            f1.write(f"{ba2base(2, l1)} {ba2base(2, m)}\n")
            f2.write(f"{ba2base(2, l2)} {ba2base(2, m)}\n")

    def cosine_similarity(self, l1, l2):

        vec1 = Counter(l1)
        vec2 = Counter(l2)
        
        v1key = []
        v1val = []
        for k in vec1.keys():
            v1key.append(k)
            v1val.append(vec1[k])
        print(v1key)
        print(v1val)
        
        v2key = []
        v2val = []
        for k in vec2.keys():
            v2key.append(k)
            v2val.append(vec2[k])
        print(v2key)
        print(v2val)

        intersection = set(vec1.keys()) & set(vec2.keys())
        
        
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        print("numac", numerator)

        sum1 = sum([vec1[x]**2 for x in vec1.keys()])
        sum2 = sum([vec2[x]**2 for x in vec2.keys()])
        print("sumac", sum1, sum2)
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
        print("denomac", denominator)

        if not denominator:
            return 0.0

        return float(numerator) / denominator

    # Could be changed to include rightmost minimum too
    def get_min(self, get_key = lambda x: x):
        def rightmost_minimum(l):
            minimum = float('inf')
            minimum_index = -1
            pos = 0

            
            while(pos < len(l)):
                if (get_key(l[pos]) < minimum):
                    minimum = get_key(l[pos])
                    minimum_index = pos
                pos += 1
            
            return l[minimum_index]
        return rightmost_minimum

    # Have used the inbuilt hash function (Should try a self defined rolling hash function)
    def winnowing(self, kgrams, k, t):
        modified_min_func = self.get_min(lambda key_value: key_value[0])
        
        document_fingerprints = []
        
        hash_table = [ (hash(kgrams[i]) , i)  for i in range(len(kgrams)) ]
        
        window_length = t - k + 1
        window_begin = 0
        window_end = window_length
        
        minimum_hash = None

        while (window_end < len(hash_table)):
            window = hash_table[window_begin:window_end]
            window_minimum = modified_min_func(window)
            
            if(minimum_hash != window_minimum):
                document_fingerprints.append(window_minimum[0]) #not taking positions into consideration
                minimum_hash = window_minimum

            window_begin = window_begin + 1
            window_end = window_end + 1

        return document_fingerprints

    def generate_kgrams(self, data, k):
        for text in data :
            token = nltk.word_tokenize(text)
            kgrams = ngrams(token, k)
            lst_kgrams = list(kgrams)
            return lst_kgrams

    # only conversion to lowercase for now
    def preprocess(self, document):
        preprocessed_document = []
        for item in document :
            item = item.lower()
            preprocessed_document.append(item) 
        return preprocessed_document

    def generate_fingerprints(self, file_name, k, t) :
        data = []
        f = open(file_name)
        data.append(f.read())
        f.close()
        preprocessed_data = self.preprocess(data)
        kgrams = self.generate_kgrams(preprocessed_data, k)
        # print(len(kgrams))
        document_fingerprints = self.winnowing(kgrams, k, t)
        return document_fingerprints

    def GentoFile(self, p1, p2):
        program1 = p1
        program2 = p2
        fingerprints1_0 = self.generate_fingerprints((program1+"_lev0.txt"), 13, 17)
        fingerprints2_0 = self.generate_fingerprints((program2+"_lev0.txt"), 13, 17)

        vec1 = Counter(fingerprints1_0)
        vec2 = Counter(fingerprints2_0)
        
        print(len(vec1))
        print(len(vec2))  
        
        v1key = []
        v1val = []
        for k in vec1.keys():
            v1key.append(int2ba(2**126 + k, length=128))
            v1val.append(vec1[k])
        v2key = []
        v2val = []
        for k in vec2.keys():
            v2key.append(int2ba(2**126 + k, length=128))
            v2val.append(vec2[k])
        f0 = open(os.path.join("Client1", "Client1_Server0_v2.dat"), "w+")
        f1 = open(os.path.join("Client1", "Client1_Server1_v2.dat"), "w+")
        f2 = open(os.path.join("Client1", "Client1_Server2_v2.dat"), "w+")
        self.Write2File(f0, f1, f2, v1key, v1val)
        f0.close()
        f1.close()
        f2.close()
        f0 = open(os.path.join("Client2", "Client2_Server0_v2.dat"), "w+")
        f1 = open(os.path.join("Client2", "Client2_Server1_v2.dat"), "w+")
        f2 = open(os.path.join("Client2", "Client2_Server2_v2.dat"), "w+")
        self.Write2File(f0, f1, f2, v2key, v2val)
        f0.close()
        f1.close()
        f2.close()

    def winnowingFinal(self, p1, p2):
        program1 = p1
        program2 = p2

        lev0s = []
        lev1s = []
        lev2s = []

        for i in range(10):
            fingerprints1_0 = self.generate_fingerprints((program1+"_lev0.txt"), 13, 17)
            fingerprints2_0 = self.generate_fingerprints((program2+"_lev0.txt"), 13, 17)
            cosine_similarity_lev0 = self.cosine_similarity(fingerprints1_0, fingerprints2_0)
            lev0s.append(cosine_similarity_lev0)
            
            vec1 = Counter(fingerprints1_0)
            vec2 = Counter(fingerprints2_0)
            
            fingerprints1_1 = self.generate_fingerprints((program1+"_lev1.txt"), 13, 17)
            fingerprints2_1 = self.generate_fingerprints((program2+"_lev1.txt"), 13, 17)
            cosine_similarity_lev1 = self.cosine_similarity(fingerprints1_1, fingerprints2_1)
            lev1s.append(cosine_similarity_lev1)

            fingerprints1_2 = self.generate_fingerprints((program1+"_lev2.txt"), 13, 17)
            fingerprints2_2 = self.generate_fingerprints((program2+"_lev2.txt"), 13, 17)
            cosine_similarity_lev2 = self.cosine_similarity(fingerprints1_2, fingerprints2_2)
            lev2s.append(cosine_similarity_lev2)

        final_cosine_similarity_lev0 = round(mean(lev0s), 2)
        final_cosine_similarity_lev1 = round(mean(lev1s), 2)
        final_cosine_similarity_lev2 = round(mean(lev2s), 2)
        print(lev0s[0])

        a_file = open(program1+"_count.txt")
        b_file = open(program2+"_count.txt")
        count_values=[]
        for c in range(3):
            a = int(a_file.readline())
            b = int(b_file.readline())
            count_values.append([a,b])
        a_file.close()
        b_file.close()

        normalization_score = 0
        t=0
        for c in range(3):
            x=count_values[c][0]
            y=count_values[c][1]
            if(x + y)!=0:
                t=t+1
                if x>y:
                    s = 1-((x-y)/(x+y))
                else:
                    s = 1-((y-x)/(x+y))    
                normalization_score+=(10*s)

        if t!=0:
            normalization_score=normalization_score/(t*10)
            total_similarity_score_win = ((0.5*final_cosine_similarity_lev0) + (0.3*final_cosine_similarity_lev1) + (0.2*final_cosine_similarity_lev2))
            normalization_score = normalization_score
            final_score = (total_similarity_score_win*60)+(normalization_score*40)
            print("Similarity score = : \n", final_score)
        else:
            total_similarity_score_win = ((0.5*final_cosine_similarity_lev0) + (0.3*final_cosine_similarity_lev1) + (0.2*final_cosine_similarity_lev2))
            final_score = (total_similarity_score_win*100)
            print("Similarity score = : \n", final_score)

        p1 = open(os.path.join("Program1", "program1.txt"), "r")
        p2 = open(os.path.join("Program2", "program2.txt"), "r")
        program1_name = p1.readline()
        program2_name = p2.readline()
        p1.close()
        p2.close()
        row = [program1_name, program2_name, total_similarity_score_win, final_score]
        with open("experiments_python-loops.csv", "a") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(row)
        
        # Cosine similarity seems to be highest for k = 11 and t = 15, should try others.

if __name__ == "__main__":
    filename1 = sys.argv[2]
    program_number1 = sys.argv[1]
    filename2 = sys.argv[4]
    program_number2 = sys.argv[3]
    gast = GenAST()
    gast.generate_ast(filename1, program_number1)
    gast2 = GenAST()
    gast2.generate_ast(filename2, program_number2)
    win = Winnowing()
    win.GentoFile(os.path.join("Program1", "program1"), os.path.join("Program2", "program2"))
