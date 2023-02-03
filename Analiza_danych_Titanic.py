import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
train_file = pd.read_csv(r".\train.csv")
train_file = train_file.drop(["PassengerId", "Name", "SibSp", "Ticket", "Parch", "Embarked"], axis=1)
sns.set_style("darkgrid")
def menu():
    while True:
        jakie_dane1 = str(input("A - Wyświetl dane w postaci tabeli. \n"
                                "B - ile osób zginęło, a ile przeżyło. \n"
                                "C - relacja między klasą podróżniczą, a przeżywalnością. \n"
                                "D - relacja między wiekiem, a przeżywalnością. \n"
                                "E - relacja między płcią, a przeżywalnością. \n"
                                "F - histogram wieku ofiar. \n"
                                "Q - quit").lower())
        match jakie_dane1:
            case "a":
                print(train_file.head(891))
            case "b":
                df = train_file["Survived"].sum()
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.catplot(data=train_file, x="Survived", kind="count")
                plt.show()
                print(df)
            case "c":
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.catplot(data=train_file, x="Pclass",  kind="count", hue="Survived")
                plt.show()
            case "d":
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.relplot(data=train_file, x="Fare", y="Age", hue="Survived")
                plt.show()
            case "e":
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.catplot(data=train_file, x="Sex", hue="Survived", kind="count")
                plt.show()
            case "f":
                train_file.loc[:, "Survived"][train_file["Survived"] == 0] = "No"
                train_file.loc[:, "Survived"][train_file["Survived"] == 1] = "Yes"
                sns.kdeplot(data=train_file, x="Age", hue="Survived")
                plt.show()
            case "q":
                break
menu()
