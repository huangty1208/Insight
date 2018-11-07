
import os


# function for building variable and corresponding count pairs in dict 
def word_cnt(word, bag):  
    if word != '':
        if word in bag:
            bag[word] += 1
        else:
            bag[word] = 1


# sort the generated dict by count and then alphabets
def order_cnt(d1, desc = False):  
    words = [(word, cnt) for word, cnt in d1.items()]
    s = sorted(words, key=lambda x: x[0], reverse=False)
    return sorted(s, key=lambda x: x[1], reverse=desc)

# variables for indexing and counting
cnt_occu = {}
cnt_stat = {}
cer_cnt = 0

status_ind = 0
stat_ind = 0
occu_ind = 0

status_match = "STATUS"
stat_match = "EMPLOYER_STATE"
occu_match = "JOB_TITLE"

# environment pathway
path = os.getcwd()

filepath = path+"/input/h1b_input.csv"  
outpath = path+"/output/"


# open input file and read lin by line
with open(filepath) as fp:  
   for cnt, line in enumerate(fp):
       temp = line.strip().split(';')


# find corresponding columns
       if cnt == 0:
          for c1, c2 in enumerate(temp):
             if status_match in c2:
                 status_ind = c1

             if stat_match in c2:
                 stat_ind = c1

             if occu_match in c2:
                 occu_ind = c1

# count only certified cases       
       if temp[status_ind].strip() == 'CERTIFIED':
          word_cnt(temp[stat_ind].strip(),cnt_stat)
          word_cnt(temp[occu_ind].strip(),cnt_occu)
          cer_cnt += 1

# sort dict by values
sorted_stat = order_cnt(cnt_stat, desc = True)
sorted_occu = order_cnt(cnt_occu, desc = True)
          

#write files to output

f1 = open(outpath+"top_10_occupations.txt", "w")
f2 = open(outpath+"top_10_states.txt", "w")
f1.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
f2.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")


linec = 0

while linec < 10 : 

  f1.write(sorted_occu[linec][0]+";"+str(sorted_occu[linec][1])+";"+str(round(100*(sorted_occu[linec][1]/cer_cnt),1))+'%'+"\n")

  f2.write(sorted_stat[linec][0]+";"+str(sorted_stat[linec][1])+";"+str(round(100*(sorted_stat[linec][1]/cer_cnt),1))+'%'+"\n")

  linec += 1


f1.close()
f2.close() 




