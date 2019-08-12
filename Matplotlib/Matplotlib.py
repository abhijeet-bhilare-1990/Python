#!/usr/bin/env python
# coding: utf-8

# ## MatPlotlib Tutorial
# **Author - Abhijeet Bhilare** \
# **github link - https://github.com/abhijeet-bhilare-1990/Python**\
# **references - https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html**\
# **youtube reference - code basics matplotlib tutorial**
#                 
# ### Basics of matplotlib
# matplotlib library is used for data visualization in 2-D and 3-D plotting. Most common plots are\
# **1. Bar Chart**\
# **2. Histogram**\
# **3. Pie Chart**\
# **3. Pie Chart**\
# **3. Surface 3d**\
# **reference link - https://matplotlib.org/3.1.1/tutorials/introductory/sample_plots.html**
# 
# 
# In python3 you can install matplotlib using below command \
# **pip3 install matplotlib** \
# make sure you dont have any proxy, if proxy is there please penetrate proxy using following command \
# **pip3 --proxy https://username:password@proxyname:portnumber install matplotlib** 
# 
# ### Limitations
# 1. This tutorial is very basic and covers only basic and commonly use charts. 
# 
# ### Future Learnings
# 1. Explore more on 3-D charts.
# 2. Explore Log, Maths, related plots.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import numpy as np


# ### Basics

# In[2]:


x = [1,2,3,4,5,6,7]
y = [50,30,56,52,48,34,42]
plt.title('Weather') # Title 
plt.xlabel('day') # x-axis label
plt.ylabel('temperature') # y-axis label
plt.plot(x,y, color='green', linewidth=5, linestyle='dotted') # check reference link for more args


# ### Format Strings in Plot

# In[3]:


plt.plot(x, y, "g+") # plots +


# In[4]:


plt.plot(x, y, "g+--")  #you can join + with --
# there are multiple other options like . , v o * p # check reference link for more options in Marker section


# In[5]:


plt.plot(x, y, "g+-.", linewidth=0.5)


# In[ ]:





# In[6]:


plt.plot(x, y, "--r*") #-- line style, r(red) color, * marker


# In[7]:


plt.plot(x, y, marker='x', color='cyan', linestyle='', markersize=10) # explicit args can be provided


# In[8]:


plt.plot(x, y, color='red', marker='+', markersize='20', alpha=0.2) # alpha is opaquness/transparency


# ### Legend and Grids
# 
# #### Legend reference - https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html
# #### grid reference - https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.grid.html

# In[9]:


days = [1,2,3,4,5,6,7]
maxt = [41,40,38,34,36,41,39]
mint = [31,28,26,22,28,29,27]
avgt = [36,34,32,28,32,35,33]


# In[10]:


plt.title('Weather') # Title 
plt.xlabel('day') # x-axis label
plt.ylabel('temperature') # y-axis label
plt.plot(days, maxt, label='Max')
plt.plot(days, mint, label='Min')
plt.plot(days, avgt, label='Avg')
# labels set above are not visible to make them visible we have to call legend function
plt.legend() #we can set different properties to this like location, size, etc. 
plt.grid() # background grid


# ### Bar Chart

# In[11]:


company = ["Google", "Amazon", "Microsoft", "Facebook"]
revenue = [70, 124, 76, 67]
profit = [40, 25, 34, 24]


# In[12]:


nparray = np.arange(len(company))
nparray


# In[13]:


plt.title("US Company Stat")
plt.xlabel("Company Names")
plt.ylabel("Revenue in USD(bln)")
plt.xticks(nparray, company) # Replace numbers to names of companies
plt.bar(nparray, revenue, label='revenue') # Plot Bar chart
plt.legend()
#plt.grid()


# In[14]:


plt.bar(nparray, revenue, label='revenue') # Plot Bar chart
plt.bar(nparray, profit, label='Profit')  # another bar is plotted on same bar
plt.legend()


# In[15]:


plt.bar(nparray-0.6, revenue, label='revenue') # Plot Bar chart side by side
plt.bar(nparray-0.4, profit, label='Profit')  # another bar is plotted side by side
plt.legend()


# In[16]:


plt.xticks(nparray, company)
plt.bar(nparray-0.2, revenue, width=0.6, label='revenue') # Plot Bar chart side by side
plt.bar(nparray-0.2, profit, width=0.4, label='Profit')  # set width of bars
plt.legend()


# In[17]:


#Horizontal bar
plt.yticks(nparray, company)
plt.barh(nparray-0.2, revenue, label='revenue') 
plt.barh(nparray-0.2, profit, label='Profit')  
plt.legend()


# ### Histogram

# In[18]:


# For grouping or catogorizing data
blood_sugar = [70, 80, 85, 76, 121, 134, 143, 90, 95, 101, 91, 98, 73, 103, 132]
plt.hist(blood_sugar)


# In[19]:


plt.hist(blood_sugar, bins=[70,90,120,150], rwidth = 0.95, color = 'g') # change the bin and seperate it 


# In[20]:


#For seperating it with male and female catogory
blood_sugar_Male = [70, 80, 85, 76, 121, 134, 143, 90, 95, 101, 91, 98, 73, 103, 132]
blood_sugar_Female = [63, 76, 78, 76, 101, 121, 114, 69, 72, 85, 91, 98, 73, 103, 131]


# In[21]:


plt.hist([blood_sugar_Male, blood_sugar_Female],  bins=[70,90,120,150], rwidth = 0.95, color = ['g', 'red'], label=['Male', 'Female'])
plt.legend()


# ### Pie Chart

# In[22]:


expenses = [95, 60, 25, 20, 10, 20]
lbls = ["Rent", "Food", "Travel", "Education", "Phone", "Medical"]
plt.pie(expenses, labels=lbls) # Show basic pie chart with labels


# In[23]:


plt.axis("equal")
plt.pie(expenses, labels=lbls, radius=2) #double the size - raduis arg
plt.show()


# In[24]:


plt.pie(expenses, labels=lbls, radius=2, autopct="%0.1f%%") # Show percentage
plt.show()


# In[25]:


plt.pie(expenses, labels=lbls, radius=2, autopct="%0.1f%%", explode=[0, 0, 0, 0.2, 0, 0]) # Show take it out or seperate
plt.show()


# ### Save chart to file

# In[26]:


plt.savefig("Pie_Chart.png", bbox_inches='tight', transparent=True) # Save file, Transparent means background none


# ### 3-D Basics

# In[27]:


from mpl_toolkits import mplot3d # for 3-D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # for 3-D projection in 3 axes

x =[1,2,3,4,5,6,7,8,9,10]
y =[5,6,2,3,13,4,1,2,4,8]
z =[2,3,3,3,5,7,9,11,9,10]



ax.scatter(x, y, z, c='r', marker='x') #scatter data around 3 axes 

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

