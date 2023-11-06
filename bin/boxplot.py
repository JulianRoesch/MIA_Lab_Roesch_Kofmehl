import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd


def main():
    # todo: load the "results.csv" file from the mia-results directory
    # todo: read the data into a list
    # todo: plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    #  in a boxplot

    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')

    date = "2023-10-25-08-45-57"
    csv_string = "mia-result/" + date + "/results.csv"
    data = pd.read_csv(csv_string)

    Number =[]
    Label = []
    Value = []

    for cnt in range(data.shape[0]):
        string = data.values[cnt][0]
        P1 = string.find(";")
        string = string.replace(';', '!', 1)
        P2 = string.find(";")

        Number.append(string[:P1])
        Label.append(string[P1+1:P2])
        Value.append(float(string[P2+1:]))

    #sort data to labels
    #"Amygdala" "GeryMatter" "Hippocampus" "Thalamus" "WhiteMatter"

    print(Label[1::5])
    Matrix = np.zeros([5,20])

    Matrix[0][:] = Value[0::5]
    Matrix[1][:] = Value[1::5]
    Matrix[2][:] = Value[2::5]
    Matrix[3][:] = Value[3::5]
    Matrix[4][:] = Value[4::5]


    #boxplot
    labels = ["Amygdala" ,"GeryMatter" ,"Hippocampus" ,"Thalamus", "WhiteMatter"]
    fig, axs = plt.subplots()
    axs.boxplot(Matrix.transpose(),labels=labels)
    axs.set_title('Dice Coefficients')
    plt.show()

if __name__ == '__main__':
    main()
