import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd


    date = "2023-10-25-08-45-57"
    csv_string = "mia-result/" + date + "/results.csv"
    data = pd.read_csv(csv_string)

    Number =[]
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

        Number.append(string[:P1])
        Label.append(string[P1+1:P2])
        Value_Dice.append(float(string[P2+1:P3]))
        #Value_Haus.append(float(string[P3 + 1:]))
    #sort data to labels
    #"Amygdala" "GreyMatter" "Hippocampus" "Thalamus" "WhiteMatter"

    print(Label[1::5])
    Matrix_DC = Matrix_HD  = np.zeros([5,20])

    for cnt in range(5):
        Matrix_DC[cnt][:] = Value_Dice[cnt::5]
        Matrix_HD[cnt][:] = Value_Dice[cnt::5]


    #boxplot2
    labels = ["Amygdala" ,"GreyMatter" ,"Hippocampus" ,"Thalamus", "WhiteMatter"]
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,figsize=(14, 5))
    ax1.boxplot(Matrix_DC.transpose(),labels=labels)
    ax1.set_title('Dice coefficients')
    ax1.set_ylabel('Dice Coeff.')

    ax2.boxplot(Matrix_HD.transpose(),labels=labels)
    ax2.set_title('Hausdorff distance')
    ax2.set_ylabel('Hausdorff')
    fig.suptitle(csv_string)
    plt.show()
