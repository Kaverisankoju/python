# PANDAS
# SERIES
import pandas as pd
s1 = pd.Series([10,20,30])
print(s1[0])
print(s1.values)
print(s1.index)
print(s1>20)
print(s1[s1>20])  #here we can have & operator | operator too


import pandas as pd
s1 = pd.Series([10,20,30],index=['a','b','c'])
print(s1)


# DATAFRAME
#Manullay write the data
#EXAMPLE
data = {
    'name' :['Alice','Bob','Charlie'],
    'Age':[25,30,35]
}

df = pd.DataFrame(data)
print(df)

# ASSIGNMENT
df = pd.read_csv('Titanic-Dataset.csv')

print(df.head(10))
print(df.columns)
print(df.shape)
print(df.dtypes)
print("null values:",df.isnull().sum())
print("value_count",df['Survived'].value_counts())
survived = df['Survived'].sum()
total = df.shape[0]
percentage_survied = (survived/total) * 100
print("Percentage of Passengers who survied:",round(percentage_survied,2),"%")
average_age = df['Age'].mean()
print("Average age of the passengers:",round(average_age,2))
max_fare = df['Fare'].max()
min_fare = df['Fare'].min()
print("Maximum fare paid:",max_fare)
print("Minimum fare paid:",min_fare)
gender_count = df["Sex"].value_counts()
print("gender count:",gender_count)
embarked_count = df["Embarked"].value_counts()
print("embarked count:",embarked_count)
unique_classes = df["Pclass"].unique()
print("unique Classes:",unique_classes)
average_age_by_survival = df.groupby('Survived')['Age'].mean()
print("Average age of survivours vs non-survivors:")
print(average_age_by_survival)
survival_rate_gender = df.groupby('Sex')['Survived'].mean() * 100
print("Survival rate by gender:")
print(survival_rate_gender)

survival_rate_pclass = df.groupby('Pclass')['Survived'].mean()*100
print("survival rate by passenger class:")
print(survival_rate_pclass)

avg_fade_by_class = df.groupby("Pclass")['Fare'].mean()
print("average fare paid by each class")
print(avg_fade_by_class)

#
df['AgeGroup'] = pd.cut(df['Age'],bins = [0,18,60,100],labels=['Chils','Adult','Senior'])
print(df.groupby('AgeGroup')['Survived'].mean()*100)

#
with_family = (df['SibSp'] > 0).sum()
alone = (df['SibSp'] == 0).sum()
print("Passengers with siblings/spouses:",with_family)
print("Passengers who traveled alone:",alone)

#
most_common_age = df['Age'].mode()[0]
print("Most common passenger age:",most_common_age)

#
avg_fare = df.groupby('Survived')['Fare'].mean()
print("Average fare of non-survivors(0):",round(avg_fare[0],2))
print("Average fare of survivors(1):",round(avg_fare[1],2))

df['family_size'] = df['SibSp'] + df['Parch'] + 1
print(df[['SibSp','Parch','family_size']].head())




