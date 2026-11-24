import pandas as pd
import numpy as np
df = pd.read_csv("titanic_folder/titanic.csv")#df stands for dataframe (pulling excel file into tabular)
print(df.head())
print("")
#1st question
print(df.shape)
print("there are",df.shape[0],"rows")
print("there are",df.shape[1],"coloumns")
print("")
#2nd question
survived = df[(df["Survived"]== 1)&(df["Pclass"]== 3)]
print("these are the people in 3rd passenger class who survived")
print("")
print(survived)
#3rd question
print("")
survived2 = df[(df["Survived"]== 1)&(df["Pclass"]== 1)]
print("these are the people in 1st passenger class who survived")
print("")
print(survived2)
print("")
#4th question
survivedall = df[df["Survived"]==1]
print(survivedall,"is the toal amount of people who survived")
#5th question
print("")
print("the oldest passenger was",df["Age"].max(),"years old")
#6th question
print("")
agelessthan25 = df[df["Age"] <= 25]
print(agelessthan25)
#7th question
print("")
agemorethan50 = df[df["Age"] >= 50]
print(agemorethan50)
#8th question
print("")
didnotsurvive = df[df["Survived"] == 0]
print(didnotsurvive["Name"])
#9th question
print("")
female = df[df["Sex"] == "female"]
print(female["Name"])
#10th question
print("")
last10 = df.tail(10)
print(last10["Name"])
#11th question
#clientswhopaidbetween60to100
print("")
cwpb60t100 = df[(df["Fare"]>= 60) & (df["Fare"]<= 100)]
print(cwpb60t100["Name"])