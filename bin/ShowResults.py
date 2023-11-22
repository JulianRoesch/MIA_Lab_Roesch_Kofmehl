import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

#find folders in mia-results
root='mia-result/'
dirlist = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
print(dirlist)

show_boxplot = True
save_boxplot = False


Data_DC = Data_HD = np.zeros([5,10,np.size(dirlist)])
for c in range(np.size(dirlist)):
    csv_string = "mia-result/" + dirlist[c] + "/results.csv"
    data = pd.read_csv(csv_string)

    Number = []
    Label = []
    Value_Dice = []
    Value_Haus = []

    for cnt in range(data.shape[0]):
        string = data.values[cnt][0]
        P1 = string.find(";")
        string = string.replace(';', '!', 1)
        P2 = string.find(";")
        string = string.replace(';', '!', 1)
        P3 = string.find(";")
        if(string[P1-1] != 'P'):
            Number.append(string[:P1])
            Label.append(string[P1+1:P2])
            Value_Dice.append(float(string[P2+1:P3]))
            Value_Haus.append(float(string[P3 + 1:]))
    #sort data to labels
    #"Amygdala" "GreyMatter" "Hippocampus" "Thalamus" "WhiteMatter"

    N = np.size(Number)
    Matrix_DC  = np.zeros([5,int(N/5)])
    Matrix_HD  = np.zeros([5,int(N/5)])

    for cnt2 in range(5):
        Matrix_DC[cnt2][:] = Value_Dice[cnt2::5]
        Matrix_HD[cnt2][:] = Value_Haus[cnt2::5]
    print("\n Dice", Matrix_DC)
    print("\n Haus", Matrix_HD)
    if show_boxplot:
        # boxplot2
        labels = ["Amygdala", "GreyMatter", "Hippocampus", "Thalamus", "WhiteMatter"]
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))
        ax1.boxplot(Matrix_DC.transpose(), labels=labels)
        ax1.set_title('Dice coefficients')
        ax1.set_ylabel('Dice Coeff.')

        ax2.boxplot(Matrix_HD.transpose(), labels=labels)
        ax2.set_title('Hausdorff distance')
        ax2.set_ylabel('Hausdorff')
        fig.suptitle(csv_string)
        plt.show()

        if save_boxplot:
            plt.savefig(csv_string + ".pdf", dpi=150)


    # Data_DC[:,:,c] = Matrix_DC
    # Data_HD[:,:,c] = Matrix_HD