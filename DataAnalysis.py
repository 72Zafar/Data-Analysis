import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt


df = pd.read_csv(r"D:\projectis\Data\Diwali Sales Data.csv", encoding='latin1')

print (df.shape)
print ("\n")

print (df.isnull().sum())
print ("\n")

print (df.info())
print ("\n")

df.drop(["Status", "unnamed1"], axis=1, inplace=True)
print ("\n")

print (df.head())
print ("\n")

print (df.isnull().sum())
print ("\n")

print(df.shape)
print ("\n")

print (df.dropna(inplace=True))

print (df.isnull().sum())
print ("\n")

print(df.shape)
print ("\n")

df["Amount"] = df["Amount"].astype ('int')

print (df["Amount"].dtypes)

print(df.columns)
print ("\n")

print (df.describe())
print ("\n")

ax = sns.countplot(x = "Gender" , data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()    


sales_gendr = df.groupby(["Gender"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.barplot(x = "Gender" , y = "Amount" , data=sales_gendr)
plt.show()
# From above graphs we can see the most of the buyers are females and even the purchasing power of females are greater than men

ax = sns.countplot(data=df , x = "Age Group" , hue = "Gender",palette='BuPu')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()    


# Total Amount  vs Age group
sales_age = df.groupby(["Age Group"],as_index=False)["Amount"].sum().sort_values(by = "Amount",ascending=False)
sns.barplot(x= "Age Group",y="Amount",data=sales_age)
plt.show()
# from above graphs we can see that most of the buyers are of age group between 26-35 yer female


print(df.columns)
print ("\n")

sales_stats = df.groupby(["State"],as_index = False)["Orders"].sum().sort_values(by="Orders",ascending=False).head(8)
sns.set_theme(rc={'figure.figsize':(15,5)})
sns.barplot(x="State" , y = "Orders",data = sales_stats)
plt.show()


sales_stats = df.groupby(["State"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False).head(8)
sns.set_theme(rc={'figure.figsize':(15,5)})
sns.barplot(data= sales_stats, x="State",y="Amount")
plt.show()
# from above graphs we can see that most of the order and total sales/amount are from utter pradesh ,maharashtra and karnataka respectively

sns.set_theme(rc={'figure.figsize':(5,5)})
sns.countplot(data=df,x="Marital_Status")
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()    


sales_stats = df.groupby(["Marital_Status","Gender"],as_index =False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.barplot(data=sales_stats, x = "Marital_Status" , y = "Amount", hue = "Gender",palette='plasma')
plt.show()
# from above graphs we can see tat most of the buyers are married(Women)and they have hige purchasing

sns.set_theme(rc={'figure.figsize':(20,5)})
sns.countplot(data=df,x="Occupation")
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()    



sales_stats = df.groupby(["Occupation"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.set_theme(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_stats,x="Occupation",y="Amount")
plt.show()
# from above graphs we can see tat most of the buyers are working in IT Healthcare and Aviation   sector


top_product_categories = df['Product_Category'].value_counts().head(7).index
filtered_df = df[df['Product_Category'].isin(top_product_categories)]


sns.set_theme(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data=filtered_df, x="Product_Category", order=top_product_categories)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()    

sales_stats = df.groupby(["Product_Category"],as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False).head(7)
sns.set_theme(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_stats,x="Product_Category",y="Amount")
plt.show()
# from above graphs we can see tat most of the sold products are from Food , Clothing and Electronics category


sales_stats = df.groupby(["Product_ID"],as_index=False)["Orders"].sum().sort_values(by="Orders",ascending=False).head(8)
sns.barplot(data=sales_stats,x="Product_ID",y="Orders")
plt.show()



