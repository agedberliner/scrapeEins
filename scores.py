from rouge import Rouge
import csv
from matplotlib import pyplot as plt
rouge = Rouge()


with open('brandeins.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    comple = []  # list for all complex paragraphs
    compleinv = []  # list for all complex paragraphs in reverse order
    simple = []  # list for all simple paragraphs
    simpleinv = []  # list for all simple paragraphs in inverse order

    # filling the lists with content from the brandeins.csv file
    for row in reader:
        if len(row) == 0:
            continue
        comple.append(row[0])
        compleinv.insert(0, row[0])
        simple.append(row[1])
        simpleinv.insert(0, row[1])


# calculating scores of different combinations of complex and simple and "inverse" as random data
scoresComSim = rouge.get_scores(comple, simple)
scoresComSimInv = rouge.get_scores(comple, simpleinv)
scoresComComInv = rouge.get_scores(comple, compleinv)

scoresSimCom = rouge.get_scores(simple, comple)
scoresSimComInv = rouge.get_scores(simple, compleinv)
scoresSimSimInv = rouge.get_scores(simple, simpleinv)

# get the relevant data from the calculated rouge score
def getrouge1(scores):
    counter = 0
    rouge1 = []
    while counter < len(scores):
        rouge1.append(scores[counter]["rouge-1"]["f"])
        counter = counter + 1
    return rouge1

def getrouge2(scores):
    counter = 0
    rouge2 = []
    while counter < len(scores):
        rouge2.append(scores[counter]["rouge-2"]["f"])
        counter = counter + 1
    return rouge2

def getrougel(scores):
    counter = 0
    rougel = []
    while counter < len(scores):
        rougel.append(scores[counter]["rouge-l"]["f"])
        counter = counter + 1
    return rougel


# normalize y axis from 0-1
yaxis = plt.gca()
yaxis.set_ylim([0, 1])


plt.plot(getrougel(scoresComSim))
plt.plot(getrougel(scoresComSimInv))
plt.show()



def log(string):
    if False:
        print(string)
