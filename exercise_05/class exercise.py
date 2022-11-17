from tkinter import HORIZONTAL
import pandas as pd;
import matplotlib.pyplot as plt

titanic = pd.read_csv('notebooks/data/titanic_train.csv')
titanic = titanic.set_index("PassengerId")
titanic = titanic.sort_values("Fare")

def reformat_name(name):
    first_name = name.split(', ')[1].split(' ')[1].strip()
    last_name = name.split(',')[0].strip()
    
    return f'{first_name} {last_name}'

# titanic['Name'] = titanic['Name'].apply(reformat_name)

# def formatNames(name):
#         name = name.replace("Mr.", "").replace("Miss.", "").replace("Mrs.", "").replace("Dr.", "")
#         names = name.split(", ")
#         name = str(names[1] + " " + names[0])
#         return name
        
# for index, row in titanic.iterrows():
#     formName = formatNames(row["Name"])
#     titanic.at[index,"Name"] = formName


# def get_last_name(name):
#     return name.split(',')[0].strip()

# for index, row in titanic.iterrows():
#     print(get_last_name(row["Name"]))

# titanic = titanic[titanic["Ticket"].isin(["350406","248706","382652","244373","345763","2649","239865"])]
# titanic = titanic[titanic["Age"].notna()]
# titanic = titanic[titanic["Age"] < 18]

titanic["Relations"] = titanic["SibSp"] + titanic["Parch"]

bob = titanic.groupby("Relations")["Survived"].sum().reset_index()

bob.plot(kind="bar", x="Relations",y="Survived")
plt.xticks(rotation=0, horizontalalignment='right', fontweight='light')
plt.show()



#print(titanic)













