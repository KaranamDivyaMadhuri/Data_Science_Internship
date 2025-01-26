import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from colorama import Fore, Back, Style
from termcolor import colored
import warnings
warnings.filterwarnings("ignore")
Colors = ["#89CFF0","#FF69B4","#FFD700","#7B68EE","#FF4500",
          "#9370DB","#32CD32","#8A2BE2","#FF6347","#20B2AA",
          "#FF69B4","#00CED1","#FF7F50","#7FFF00","#DA70D6"]
df = pd.read_csv("shopping_trends.csv")
df.sample(5)
ax=df['Gender'].value_counts().plot(kind='bar', rot=0,color=color)
plt.show()
counts=df["Gender"].value_counts()
counts.plot(kind='pie', colors=color, explode=(0,0.1), autopct='%1.1f%%')
plt.xlabel('Gender', weight='bold')
plt.legend()
plt.show()
sns.histplot(data=df['Age'], color="skyblue")
plt.show()
df["Category"].value_counts()
ax=df["Category"].value_counts().plot(kind='bar', color=color, rot = 0)
for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x()+0.25,p.get_height()+1), ha='center')
plt.xlabel('Categories', weight="bold")
plt.ylabel('Number of Occurances', weight='bold')
plt.show()
plt.figure(figsize = (20, 6))
counts=df["Category"].value_counts()
explode=[0.1]*len(counts)
counts.plot(kind='pie', colors=colors, explode=explode, autopct='%1.1f%%')
plt.xlabel('Category', weight='bold')
plt.legend()
plt.show()
def get_pieChart(column):
           plt.figure(figsize = (20, 6))
           counts=df[column].value_counts()
           explode=[0]*(len(counts)-1)+ [0.1]
           counts.plot(kind='pie', colors=colors, explode=explode, autopct='%1.1f%%')
           plt.xlabel(column, weight='bold')
           plt.legend()
           plt.show()
get_pieChart("Subscription Status")
get_pieChart("Payment Method")
def getBarChart(column):
           plt.figure(figsize (20, 6))
           ax=df [column].value_counts().plot(kind='bar', color=colors, rot=0)
           for p in ax.patches:
               ax.annotate(int(p.get_height()), (p.get_x()+0.25,p.get_height()+1),ha='center')
           plt.xlabel(column, weight = "bold")
           plt.ylabel('Number of Occurances, weight='bold')
           plt.show()
getBarChart('Payment Method')
getBarChart('Shipping Type')
getBarChart('Item Purchased')
plt.figure(figsize=(16,8))
df['Item Purchased'].value_counts().sort_values().plot(kind='barh', color=sns.color_palette("tab10"),edgecolor='black')
plt.ylabel('Item Purchased', fontsize=16)
plt.xlabel('\nNumber of Occurrences', fontsize=16)
plt.title('Item Purchased\n', fontsize=16)
plt.show()
df["Location"].value_counts()
df["Size"].value_counts()
df["Category"].value_counts()
df["Color"].value_counts()
df["Season"].value_counts()
text = " ".join(title for title in df["Frequency of Purchases"])
word_cloud=WordCloud(collocations=False, background_color='white').generate(text)
plt.axis("off")
plt.imshow(word_cloud) I
plt.show()
plt.figure(figsize=(20, 6))
category_purchase_total=df.groupby ('Category') ['Purchase Amount (USD)'].sum()
category_purchase_total.plot(kind='area')
plt.title('Total Purchase Amount by Category')
plt.xlabel('Category')
plt.ylabel('Total Purchase Amount (USD)')
plt.xticks (rotation=45)
plt.show()
average_age=df['Age'].mean()
print("Average Age:",average_age)
df['Item Purchased'].mode()
df['Item Purchased'].mode()[0]
df[df['Gender']=='Male']['Item Purchased'].mode()
df [df['Gender']=='Female']['Item Purchased'].mode()
most_common_season=df ['Season'].mode()[0]
print("Most Common Season for Purchases:", most_common_season)
max_review_rating = df['Review Rating'].max() 
min_review_rating = df['Review Rating'].min() 
print("Maximum Review Rating:", max_review_rating)
print("Minimum Review Rating:", min_review_rating)
average_rating male=df[df ['Gender']=='Male']['Review Rating'].mean()
average_rating female=df[df['Gender']=='Female']['Review Rating'].mean()
print("Average Review Rating for Male Customers:", average_rating_male)
print("Average Review Rating for Female Customers:", average_rating_female)
common_category_low_rating_male_winter = df[(df['Gender'] == 'Male')& (df['Season'] == 'Winter') & (df['Review Rating'] <3)] ['Category'].mode()[0]
print("Most Common Category for Low-Rating Male Customers in Winter Season:", common_category_low_rating_male_winter)
subscription_promo_count = df[(df['Subscription Status'] == 'Yes') & (df['Promo Code Used'] == 'Yes')]['Customer ID'].count() 
print("Number of Customers with Subscription and Promo Code Used: ", subscription_promo_count)
​