# 7321 - NANDHA COLLEGE OF TECHNOLOGY

#ADS_Phase 5: Predicting IMDb Scores

# Project by ROSHINI S

import pandas as pd
import numpy as np
df=pd.read_csv("C:\Users\roshh\Downloads\Project-PredictingIMDbScores\Dataset\NetflixOriginals.csv")
df
df.info()
df.describe()
df.isnull().sum()
df.loc[df['director'].isnull()]
df.loc[df['date_added'].isnull()]
df = df.dropna()

df.head()
df.tail()
df["date_added"] = pd.to_datetime(df["date_added"])
df = df.rename(columns={"date_added": "date"})
df.head()
df.info()
df["rating"].describe()

import matplotlib.pyplot as plt
numeric_cols = df.select_dtypes(include=[np.number])
numeric_cols
plt.figure(figsize=(13,9))
plt.hist(df["duration"], bins = 10)
plt.xlabel("duratioin")
plt.show()
print(df.groupby("type")["duration"].mean())

# Use a box plot to compare the duration of movies & shows by type
plt.figure(figsize=(13,9))
plt.boxplot([df[df["type"] == "Movie"]["duration"], df[df["type"] == "TV Show"]["duration"]], labels = ["Movies", "TV Shows"])
plt.ylabel("duration")

plt.show()
df.director.unique()
mean_duration = df.groupby("director")["duration"].mean()


mean_duration.plot()
plt.xlabel("Director")
plt.ylabel("Average Duration (minutes)")
plt.title("Relationship between Director and Average Duration")
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(13,8))
plt.scatter(df['release_year'], df['duration'])
plt.xlabel('Release Year')
plt.ylabel('Duration (minutes)')
plt.title('Scatter plot of Release Year against Duration')
plt.show()

#reading the data
df1=pd.read_csv("C:\Users\roshh\Downloads\Project-PredictingIMDbScores\Dataset\NetflixOriginals.csv')
df1

df1.info()
df1["Premiere"] = pd.to_datetime(df1["Premiere"])
df1.info()
df1.columns
plt.figure(figsize=(15,9))
plt.hist(df1["Runtime"], df1["IMDB Score"])
plt.xlabel("Run Time (minutes)")
plt.ylabel("Duration (days)")

plt.title("Relationship between Run Time and Duration")
plt.show()