from rouge import Rouge
import csv
from matplotlib import pyplot as plt
rouge = Rouge()


with open('brandeins.csv', newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    comple = []
    compleinv = []
    simple = []
    simpleinv = []

    for row in reader:
        if len(row) == 0:
            continue
        comple.append(row[0])
        compleinv.insert(0, row[0])
        simple.append(row[1])
        simpleinv.insert(0, row[1])

scoresComSim = rouge.get_scores(comple, simple)
scoresComSimInv = rouge.get_scores(comple, simpleinv)
scoresComComInv = rouge.get_scores(comple, compleinv)

scoresSimCom = rouge.get_scores(simple, comple)
scoresSimComInv = rouge.get_scores(simple, compleinv)
scoresSimSimInv = rouge.get_scores(simple, simpleinv)


rouge1 = []
rouge2 = []
rougel = []


def calculaterouge(scores):
    counter = 0
    while counter < len(scores):
        rouge1.append(scores[counter]["rouge-1"]["f"])
        rouge2.append(scores[counter]["rouge-2"]["f"])
        rougel.append(scores[counter]["rouge-l"]["f"])
        counter = counter + 1


calculaterouge(scoresSimCom)


yaxis = plt.gca()
yaxis.set_ylim([0, 1])

plt.plot(rouge1)
plt.show()


log = False


def log(string):
    if log:
        print(string)
