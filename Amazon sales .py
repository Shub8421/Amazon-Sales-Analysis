#!/usr/bin/env python
# coding: utf-8

# #                                   Amazon Sales - Analysis                          

# # INTRODUCTION
# 
# 
# This dataset consists more than 1000 of real products with their identification number listed in the Amazon marketplace specifically from the region India. I noticed the region due to the currency used in the dataset is Rupee India. My objective is to clean and prepare the data due to the raw data being very unorganized. I will then move on to finding insights about the data and try to elaborate in the form of visualization.

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Importing files
df=pd.read_csv('amazon.csv')
df


# In[3]:


#Checking the columns names
df.columns


# In[4]:


#checking First Few Rows
df.head()


# In[5]:


#checking the datatype
df.dtypes


# In[6]:


#Changeing the data type of Discounted_price and actual_price
df['discounted_price']=df['discounted_price'].str.replace("₹",'')
df['discounted_price']=df['discounted_price'].str.replace(",",'')
df['discounted_price']=df['discounted_price'].astype('float64')

df['actual_price']=df['actual_price'].str.replace("₹",'')
df['actual_price']=df['actual_price'].str.replace(",",'')
df['actual_price']=df['actual_price'].astype('float64')



# In[7]:


#Changeing data type values in Discount Percentange
df['discount_percentage']=df['discount_percentage'].str.replace('%','').astype('float64')
df['discount_percentage']=df['discount_percentage']/100
df['discount_percentage']


# In[8]:


#Finding unsual string in the rating column
df['rating'].value_counts()


# In[9]:


#Insecting the row
df.query('rating == "|"')


# i went to the amazon website and found the similar product id with the same product having the rating of 4 .
# so i am going to give the item rating of 4.0
# Providing the website link:https://www.amazon.in/Eureka-Forbes-Vacuum-Cleaner-Washable/dp/B08L12N5H1

# In[10]:


#changing rating column datatype
df['rating']=df['rating'].str.replace("|",'4.0').astype('float64')


# In[12]:


#changing the rating_count data type
df['rating_count']=df['rating_count'].str.replace(",",'').astype('float64')


# In[13]:


#checking duplicates
duplicates=df.duplicated()
df[duplicates]


# In[14]:


#Rechecking missing values
df.isnull().sum()


# In[15]:


#filing null value with the mode
df['rating_count'].fillna(df['rating_count'].mode()[0],inplace=True)


# In[16]:


#Recheching the missing values
df.isnull().sum()


# In[17]:


#Creating New data Frame with selected columns
df1=df[['product_id','product_name','category','discounted_price','actual_price','discount_percentage','rating','rating_count']].copy()


# In[18]:


#Splitting the strings into category column
catsplit=df['category'].str.split('|',expand=True)
catsplit


# In[19]:


catsplit=catsplit.rename(columns={0:'category_1',1:'category_2',2:'category_3'})



# In[20]:


#Adding column into New Dataframe
df1['category_1']=catsplit['category_1']
df1['category_2']=catsplit['category_2']
df1.drop(columns='category',inplace=True)
df1


# In[21]:


#Counting Values in Category_1 column
df1['category_1'].value_counts()


# In[22]:


#Arranging Srtings in category_1 column
df1['category_1']=df1['category_1'].str.replace('&',' & ')
df1['category_1']=df1['category_1'].str.replace('OfficeProducts','Office Products')
df1['category_1']=df1['category_1'].str.replace('MusicalInstruments','Musical Instruments')   
df1['category_1']=df1['category_1'].str.replace('HomeImprovement','Home Improvement')


# In[23]:


#Counting values in category_2 column
df1['category_2'].value_counts()


# In[24]:


#Arranging strings in category_2 columns
df1['category_1']=df1['category_1'].str.replace('&',' & ')
df1['category_1']=df1['category_1'].str.replace(',',', ')
df1['category_1']=df1['category_1'].str.replace('HomeAppliances','Home Appliances')
df1['category_1']=df1['category_1'].str.replace('HomeTheater','Home Theater')
df1['category_1']=df1['category_1'].str.replace('WearableTechnology','Wearable Technology')
df1['category_1']=df1['category_1'].str.replace('NetworkingDevices','Networking Devices')
df1['category_1']=df1['category_1'].str.replace('OfficePaperProducts','Office Paper Products')
df1['category_1']=df1['category_1'].str.replace('ExternalDevices','External Devices')
df1['category_1']=df1['category_1'].str.replace('DataStorage','Data Storage')
df1['category_1']=df1['category_1'].str.replace('HomeStorage','Home Storage')
df1['category_1']=df1['category_1'].str.replace('HomeAudio ','Home Audio')
df1['category_1']=df1['category_1'].str.replace('GeneralPurposeBatteries','General Purpose Batteries')
df1['category_1']=df1['category_1'].str.replace('BatteryChargers','Battery Chargers')
df1['category_1']=df1['category_1'].str.replace('CraftMaterials','Craft Materials')
df1['category_1']=df1['category_1'].str.replace('OfficeElectronics','Office Electronics')
df1['category_1']=df1['category_1'].str.replace('PowerAccessories','Power Accessories')
df1['category_1']=df1['category_1'].str.replace('CarAccessories','Car Accessories')
df1['category_1']=df1['category_1'].str.replace('HomeMedicalSupplies','Home Medical Supplies')




# In[25]:


#Removing wide space from Product_id
df1['product_id'].str.strip()


# In[29]:


#Creating Categories for Rankings
rating_score=[]
for score in df1['rating']:
    if score <2.0 : rating_score.append('Poor')
    elif score < 3.0 : rating_score.append('Below Average')
    elif score < 4.0 : rating_score.append('Average')
    elif score < 5.0 : rating_score.append('Above Average')
    elif score ==5.0 : rating_score.append('Excellent')


# Created a a Rating Category that consists of:
# 
# 1. Score below 2.0 = Poor
# 
# 2. Score range of 2.0 - 2.9 = Below Average
# 
# 3. Score range of 3.0 - 3.9 = Average
# 
# 4. Score Range of 4.0 - 4.9 = Above Average
# 
# 5. Score of 5.0 = Excellent

# In[30]:


#Creating the new column changing the datatype
df1['rating_score'] =rating_score
df1['rating_score'] =df1['rating_score'].astype('category')


# In[31]:


#Reordering Categories
df1['rating_score']=df1['rating_score'].cat.reorder_categories(['Below Average','Average','Above Average',
                                                                'Excellent'],ordered=True)


# In[32]:


#Creating Difference of price column
df1['difference_price']=df1['actual_price']-df1['discounted_price']


# In[33]:


#Result After Cleaning
df1.head()


# In[34]:


#Subsetting Reviewing Identification
reviewers=df[['user_id','user_name']]
reviewers


# In[35]:


#Splitting user_id
splitting_user_id=reviewers['user_id'].str.split(',',expand=False)
splitting_user_id


# In[36]:


#Making user_id Display 1 per Row
reviewer_exp_id=splitting_user_id.explode()
reviewer_clean_id=reviewer_exp_id.reset_index(drop=True)
reviewer_clean_id


# In[37]:


#Splitting user_name
splitting_user_name=reviewers['user_name'].str.split(',',expand=False)
splitting_user_name


# In[38]:


#Making user_name Display 1 per Row
reviewer_exp_name=splitting_user_name.explode()
reviewer_clean_name=reviewer_exp_name.reset_index(drop=True)
reviewer_clean_name


# In[39]:


#Coverting 2 dataframes to merge
df21=pd.DataFrame(data=reviewer_clean_id)
df22=pd.DataFrame(data=reviewer_clean_name)


# In[40]:


#Merging 2 DataFramea
df2=pd.merge(df21,df22,left_index=True,right_index=True)


# In[41]:


df2.head()


# # DATA EXPLORATION

# In this stage I will try to elaborate my insights through Visualizations, Pivot Tables, and short explanations.

# In[43]:


#Setting Visualization Styles
sns.set_style(style='darkgrid')
sns.set_palette(palette='icefire')


# # Observation 1: Product Category

# Below are the list of Main Category and Sub-Category to help determine which sub-category belongs to which main category:

# In[44]:


#Main category and sub_category
main_sub=df1[['category_1','category_2','product_id']]
main_sub=main_sub.rename(columns={'category_1':'Main Category','category_2':'Sub-Category','product_id':'Producd ID'})
main_sub_piv=pd.pivot_table(main_sub, index=['Main Category', 'Sub-Category'], aggfunc='count')
main_sub_piv


# In[57]:


#Most Amountof Product by category
most_main_items = df1['category_1'].value_counts().head(5).rename_axis('category_1').reset_index(name='counts')

most_sub_items = df1['category_2'].value_counts().head(10).rename_axis('category_2').reset_index(name='counts')

fig, ax = plt.subplots(2, 1, figsize=(8, 10))
fig.suptitle('Most Amount of Products by Category', fontweight='heavy', size='x-large')

sns.barplot(ax=ax[0], data=most_main_items, x='counts', y='category_1')
sns.barplot(ax=ax[1], data=most_sub_items, x='counts', y='category_2')

plt.subplots_adjust(hspace = 0.3)

ax[0].set_xlabel('Count', fontweight='bold')
ax[0].set_ylabel('Product Main Category', fontweight='bold')

ax[1].set_xlabel('Count', fontweight='bold')
ax[1].set_ylabel('Product Sub-Category', fontweight='bold')

ax[0].set_title('Most Products by Main Category', fontweight='bold')
ax[1].set_title('Most Products by Sub-Category', fontweight='bold')


ax[0].bar_label(ax[0].containers[0])
ax[1].bar_label(ax[1].containers[0])

plt.show()


# Electronics especially accessories & pripherals and Kitchen & homeappliance contain most of the products in this data set .
# In general most products are related to the electric devices in this dataset.

# In[90]:


#Top 5 Most Expensive Products After Discount
disc_exp=sns.barplot(data=df1.sort_values('discounted_price',ascending=False).head(5),x='discounted_price',y='product_name')
disc_exp.set_title('Top 5 Expensive Product After Discount',fontweight='bold')
disc_exp.set_xlabel('Discounted Price (Indian Rupee)',fontweight='bold')
disc_exp.set_ylabel('Product Name',fontweight='bold')
plt.show()



# Sony Bravia 164 cm (65 inches) is the most expensive product after discount

# In[91]:


#Top 5 cheapest Products After Discount
disc_cheap=sns.barplot(data=df1.sort_values('discounted_price').head(5),x='discounted_price',y='product_name')
disc_cheap.set_title('Top 5 Cheapest Product After Discount',fontweight='bold')
disc_cheap.set_xlabel('Discounted Price(Indian Rupee)',fontweight='bold')
disc_cheap.set_ylabel('Product Name',fontweight='bold')
plt.show()


# E-cosmos 5V 1.2W Portale Flexible is the cheapest product after discount

# In[73]:


#Top 5 Largest price difference due to the discount in products
price_diff=sns.barplot(data=df1.sort_values('difference_price',ascending=False).head(5),x='difference_price',y='product_name')
price_diff.set_title('Top 5 Largest price difference due to discount',fontweight='bold')
price_diff.set_xlabel('Price difference(Indian Rupee)',fontweight='bold')
price_diff.set_ylabel('Product Name',fontweight='bold')
plt.show()


# Sony Bravia 164cm  having the largest price difference due to discount

# # Observation 2 : Correlation Between Features
# 

# In[92]:


#heatmap and Correlation Between Features
fig, ax = plt.subplots(2, 1, figsize=(8, 10))
fig.suptitle('Correlation between Features',fontweight='heavy',size='xx-large')
sns.heatmap(ax=ax[0],data=df1.corr())
sns.scatterplot(ax=ax[1],data=df1,y='discounted_price',x='actual_price',color='brown')
plt.subplots_adjust(hspace=0.8) 
ax[1].set_xlabel('Actual Price(India Rupee)',fontweight='bold')
ax[1].set_ylabel('Discounted Price(India Rupee)',fontweight='bold')
ax[0].set_title('Heatmap',fontweight='bold')   
ax[1].set_title('Correlation between actual price and discounted price',fontweight='bold')
plt.show()


# There are almost no correlation between the dataset but there  is positive correlation between the discounted price  of product and actual price of product.

# # Observation 3 : Product Rating
# 

# In[98]:


# Rating and Amount of rating distribution
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle('Rating and Amount of Rating Distribution',fontweight='heavy',size='xx-large')
fig.tight_layout(pad=3.0)
sns.histplot(ax=ax[0],data=df1,x='rating',bins=15,kde=True,color='blue')
sns.histplot(ax=ax[1],data=df1,x='rating_count',bins=10,kde=True,color='purple')
ax[0].set_xlabel('Rating',fontweight='bold')
ax[1].set_xlabel('Amount of Rating',fontweight='bold')
ax[0].set_ylabel('Count',fontweight='bold')
ax[1].set_ylabel('Count',fontweight='bold')
ax[0].set_title('Rating Distribution',fontweight='bold')   
ax[1].set_title('Amount of Rating Distribution',fontweight='bold')
plt.show()


# Most of the product range around 4.0 to 4.37 with  no products under the score of 2.0. The Raating Distribution is Slightly left-Skewed.
# The amount of ratings given to a product is very widespread. Most of the products that have been rated, have around 0 - 5000 amount of rating for each product. Interestingly there are products that have more than 40,000 ratings. The amount of ratings distribution is highly right skewed.

# In[47]:


#Rating Distribution by Product Main category
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(ax=ax, data=df1,x='rating',y='category_1')
ax.set_title('Rating Distribution by Product Main Category',fontweight='heavy',size='xx-large',y=1.03)
ax.set_xlabel('Rating',fontweight='bold')
ax.set_ylabel('Product Main Category',fontweight='bold')
plt.show()


# Toys&Games,Car&Motorbike and health&PersonalCare product rating around 3.7 to 4.6. All homeImpprovement and officeProduct have the minimal rating of 4.0.
# Many of the Computer & Accessories, and Electronics products have ratings in the range of 3.6 - 4.6. Though these categories do have products that have a high rating such as 5.0 and low rating, going down to 2.75.
# 
# Noticeably, the Home & Kitchen products have a really widespread rating going to as high as 4.75 and going as low as 2.0 rating, which is the lowest rating out of all the products in this dataset. However, most of the products in this category fall in the range of around 3.8 - 4.6.
# 

# In[70]:


#Rating of Products Based on Rating category
rating_main_cat=df1.groupby(['category_1','rating_score']).agg('count').iloc[:,1].rename_axis().reset_index(name='Amount')
rating_main_cat=rating_main_cat.rename(columns={'category_1':'Main category','rating_score':'Rating Category'})
rating_main_cat



# This list mention about the product and product Main category and amount of rating 

# In[71]:


#Rating Distribution by Product Sub-Category
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(ax=ax, data=df1,x='rating',y='category_2')
ax.set_title('Rating Distribution by Product Sub Category',fontweight='heavy',size='xx-large',y=1.03)
ax.set_xlabel('Rating',fontweight='bold')
ax.set_ylabel('Product Sub Category',fontweight='bold')
plt.show()


# What i observed in this Graph of Rating Distribution by Product Sub Category is that Accessories & Peripherals is highly rated product 
# .The Lowest rated product came from the sub category of heating,cooling & air quality.

# In[46]:


#The Rating of all Product in Percentage
rating_ordered=['Below','Average','Above Average','Excellent']
rating_count=df1['rating_score'].value_counts(normalize=True).rename_axis('rating').reset_index(name='counts')
rating_count['counts']=rating_count['counts'].round(3)
rating_count_plot=sns.barplot(data=rating_count ,x='rating',y='counts',order=rating_order)
rating_count_plot.set_xlabel('Rating category',fontweight='bold')
rating_count_plot.set_ylabel('Percentage',fontweight='bold')
rating_count_plot.set_title('The Rating of all  Product in Percentage',fontweight='heavy',size='xx-large',y=1.03)
rating_count_plot.bar_label(rating_count_plot.containers[0])

plt.show()


# Most of the product in the dataset have been rated Above average.There are extremely few products are rated below Average and Excellent.No Products are rated poor in this dataset

# In[47]:


#Pivoting the Rating table
def p25(g):
    return np.percentile(g,25)
def p75(g):
    return np.percentile(g,75)
rating_pivot=df1.pivot_table(values=['rating','rating_count'],index=['category_1','category_2'],
                             aggfunc=([p25,np.median,np.mean,p75]))
rating_pivot=rating_pivot.rename(columns={'rating':'Rating','rating_count':'Rating_count','median':'Median','mean':'Mean'},
                                index={'category_1':'Main_category','category_2':'Sub_category'})
rating_pivot                                       


# This is the specific data on Rating and Amount of the rating for each main and sub-category of Product from the dataset.
# 

# # Observation 3 : Reviewers

# In[69]:


#Reviewers who gave rating and reviews for more than one product
top_reviewer=data=df2['user_name'].value_counts().head(10).rename_axis('username').reset_index(name='counts')
top_review_plot=sns.barplot(data=top_reviewer,x='counts',y='username')
top_review_plot.bar_label(top_review_plot.containers[0])

top_review_plot.set_xlabel('Amount of Rating Reviews Given',fontweight='bold')
top_review_plot.set_ylabel('Reviewers name',fontweight='bold')
top_review_plot.set_title('Top 10 Active Reviewers',fontweight='heavy',size='x-large',y=1.03)
plt.show()


# There are more than 500 active reviewers who review the product ananomously under the alias of Amazon customer,Placeholder,
# kindle customer
# There are more than 8 people who have given ratings and reviews to more than 10 products on this dataset.

# # Observation 3 : Product Pricing

# In[72]:


#Actual price and discounted Price distribution
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
fig.suptitle('Actual Price and Distcounted Distribution',fontweight='heavy',size='xx-large')
fig.tight_layout(pad=3.0)
sns.histplot(ax=ax[0],data=df1,x='actual_price',bins=15,kde=True,color='orange')
sns.histplot(ax=ax[1],data=df1,x='discounted_price',bins=10,kde=True,color='red')
ax[0].set_xlabel('Actual Price (Indian Rupee)',fontweight='bold')
ax[1].set_xlabel('Discounted Price (Indian Rupee)',fontweight='bold')
ax[0].set_ylabel('Count',fontweight='bold')
ax[1].set_ylabel('Count',fontweight='bold')
ax[0].set_title('Actual Price Distribution',fontweight='bold')   
ax[1].set_title('Discounted Price Distribution',fontweight='bold')
plt.show()


# Both of the Graph shows the same results which is positive Skewed to right.

# In[75]:


#Discount Percentage distribution

Disc_per=sns.histplot(data=df1 ,x='discount_percentage',bins=8,kde=True,color='purple')
Disc_per.set_xlabel('Discount Percentage',fontweight='bold')
Disc_per.set_ylabel('count',fontweight='bold')
Disc_per.set_title('Discount Percentage distibution',fontweight='heavy',size='xx-large',y=1.03)


plt.show()


# Most of the Product have the discount of more than 50% to 80%.

# In[76]:


#Specfic details of discount percentage
df1['discount_percentage'].describe()


# In[84]:


#The Discount range by Product Main Category
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df1,x='discount_percentage',y='category_1')
ax.set_title('Discount Range by Product Main Category',fontweight='heavy',size='xx-large',y=1.03)
ax.set_xlabel('Discount Percentage',fontweight='bold')
ax.set_ylabel('Product Main Category',fontweight='bold')
plt.show()


# Computers & Accessoies,Electronics,Home & Kitchen have a large widely spread discount ranging from  mininal 10% to 90%.
# Toys & game,Car &  Motorbike,Health & PersonalCare,Home Improvement are the least spread discount.
# office product does not give a large amount of discount as compared to product main category.

# In[85]:


#The Discount range by Product Sub Category
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df1,x='discount_percentage',y='category_2')
ax.set_title('Discount Range by Product Sub Category',fontweight='heavy',size='xx-large',y=1.03)
ax.set_xlabel('Discount Percentage',fontweight='bold')
ax.set_ylabel('Product Sub Category',fontweight='bold')
plt.show()


# In[93]:


#Actual Price range and discounted Price range  by product Main Category
fig, ax = plt.subplots(2,1,figsize=(13, 15))
fig.suptitle('Price Range by Product Main category',fontweight='heavy',size='xx-large')
sns.scatterplot(ax=ax[0],data=df1,x='actual_price',y='category_1',alpha=0.3,color='blue')
sns.scatterplot(ax=ax[1],data=df1,x='discounted_price',y='category_1',alpha=0.3,color='Green')

ax[0].set_title('Actual Price Range by Product Main Category',fontweight='heavy',size='xx-large',y=1.03)
ax[0].set_xlabel('Actual Price (Indian Rupee)',fontweight='bold')
ax[0].set_ylabel('Product Main Category',fontweight='bold')

ax[1].set_title('Discounted Price Range by Product Main Category',fontweight='heavy',size='xx-large',y=1.03)
ax[1].set_xlabel('Discounted Price (Indian Rupee)',fontweight='bold')
ax[1].set_ylabel('Product Main Category',fontweight='bold')
plt.show()


# There is the decrease in the product category of electronic after applying Discount .
# Most of the product's actual price falls below 20,000 Rupee. For the discounted price, most of the products fall under 10,000 Rupee.

# In[94]:


#Actual Price range and discounted Price range  by product Sub Category
fig, ax = plt.subplots(2,1,figsize=(13, 15))
fig.suptitle('Price Range by Product Sub category',fontweight='heavy',size='xx-large')
sns.scatterplot(ax=ax[0],data=df1,x='actual_price',y='category_2',alpha=0.3,color='red')
sns.scatterplot(ax=ax[1],data=df1,x='discounted_price',y='category_2',alpha=0.3,color='orange')

ax[0].set_title('Actual Price Range by Product Sub Category',fontweight='heavy',size='xx-large',y=1.03)
ax[0].set_xlabel('Actual Price (Indian Rupee)',fontweight='bold')
ax[0].set_ylabel('Product Sub Category',fontweight='bold')

ax[1].set_title('Discounted Price Range by Product Sub Category',fontweight='heavy',size='xx-large',y=1.03)
ax[1].set_xlabel('Discounted Price (Indian Rupee)',fontweight='bold')
ax[1].set_ylabel('Product Sub Category',fontweight='bold')
plt.show()


# In[95]:


#Pivoting the Price
def p25(g):
    return np.percentile(g,25)
def p75(g):
    return np.percentile(g,75)
Price_pivot=df1.pivot_table(values=['actual_price','discounted_price'],index=['category_1','category_2'],
                             aggfunc=([p25,np.median,np.mean,p75]))

Price_pivot  

