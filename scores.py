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


scores = rouge.get_scores(comple, simple)
scoresSimInv = rouge.get_scores(comple, simpleinv)
#scoresComInv = rouge.get_scores(compleinv, simple)


counter = 0
rouge1 = []
rouge1SimInv = []
rouge2 = []
rougel = []
rougelSimInv = []
while counter < len(scores):
    rouge1.append(scores[counter]["rouge-1"]["f"])
    rouge1SimInv.append(scoresSimInv[counter]["rouge-1"]["f"])
    rouge2.append(scores[counter]["rouge-2"]["f"])
    rougel.append(scores[counter]["rouge-l"]["f"])
    rougelSimInv.append(scoresSimInv[counter]["rouge-l"]["f"])
    counter = counter + 1

yaxis = plt.gca()
yaxis.set_ylim([0, 1])
plt.plot(rouge1)
plt.plot(rouge1SimInv)
plt.show()
