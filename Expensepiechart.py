import matplotlib as plt
import numpy as np

file1 = open('expenses.txt','r')
with file1 as f:
    lines = f.readlines()
def main():
    for l in lines:
        l = l.rstrip('\n')
        row = l.split('\t')
        h = (row[0])
        j = (row[1])
        expenses = []
        expenses.append(j)
        labelie = []
        labelie.append(h)
    plt.pie(expenses, labels=labelie)
    plt.title('expenses')
    plt.show()
    print(expenses, labels)
if __name__ =='__main__':
    main()
