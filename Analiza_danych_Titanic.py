import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
train_file = pd.read_csv(r"D:\titanic\train.csv")
train_file = train_file.drop(["SibSp", "Ticket", "Parch", "Cabin", "Embarked"], axis=1)
sns.set_style("darkgrid")
def menu():
    decyzja = str(input("Menu programu do analizy danych katastrofy Titanica. Aby wyświetlić interesujące Cię dane \n"
                        "wybierz odpowiednią literę. Aby poznać dane dotyczące zgonów wybierz A. "))
    while True:
        if decyzja == "A" or decyzja == "a":
            jakie_dane1 = str(input("A - ile osób zginęło, a ile przeżyło. \n"
                                    "B - relacja między klasą podróżniczą, a przeżywalnością. \n"
                                    "C - relacja między wiekiem, a przeżywalnością. \n"
                                    "D - relacja między płcią, a przeżywalnością. \n"
                                    "E - histogram wieku ofiar. \n"
                                    "F - relacja między opłatą pasażerską, a przeżywalnością. \n"
                                    ""))
            if jakie_dane1 == "A" or jakie_dane1 == "a":
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.catplot(data=train_file, x="Survived", kind="count")
                plt.show()
            elif jakie_dane1 == "B" or jakie_dane1 == "b":
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.catplot(data=train_file, x="Pclass",  kind="count", hue="Survived")
                plt.show()
            elif jakie_dane1 == "C" or jakie_dane1 == "c":
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.distplot(train_file[train_file["Survived"]=="No"]["Age"], bins=20)
                sns.distplot(train_file[train_file["Survived"]=="Yes"]["Age"], bins=20)
                plt.show()
            elif jakie_dane1 == "D" or jakie_dane1 == "b":
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.catplot(data=train_file, x="Sex", hue="Survived", kind="count")
                plt.show()
            elif jakie_dane1 == "E" or jakie_dane1 == "e":
                train_file["Age"].plot.hist(bins=20)
                plt.show()
            elif jakie_dane1 == "F" or jakie_dane1 == "f":
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.distplot(train_file[train_file["Survived"]=="No"]["Fare"], bins=20)
                sns.distplot(train_file[train_file["Survived"]=="Yes"]["Fare"], bins=20)
                plt.show()
            else:
                break
menu()
