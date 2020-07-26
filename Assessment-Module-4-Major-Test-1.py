#!/usr/bin/env python
# coding: utf-8

# # <center> 195227 - VICEDO, Rafael Enrique G.

# ### Major Test 1
# 
# #### Coverage: Modules 2-4

# ### A Intern Payroll
# 
# **(75 Points)**
# 
# #### Problem
# 
# A tech startup hiring interns on a work-from-home basis asked you to automate the generation of a Payroll Slip Spoolfile based on a time-and-attendance log file. You are given the file named `interns-july2020.csv` for the current month for testing and immediate deployment. The first few lines of the log file look something like this:
# 
# ```
# id,base_monthly_pay,hours_rendered
# 2020001,4500,15
# 2020002,4500,20
# 2020003,4500,15
# 2020004,4500,20
# 2020005,4500,16
# 2020006,4500,18
# ```
# 
# There are 20 interns in total.
# 
# 
# To compute for Takehome Pay, first you need to compute for utilization.
# 
# To get the full amount of base pay as takehome pay, the intern must have 100% utilization.  
# 
# Assume that 100% Utilization for the month means 20 hours. So, 15 hours means 15/20 = .75 (or 75% Utilization).
# 
# **Takehome Pay = base monthly pay x utilization. **
# 
# Example:
# 
# Base Monthly Pay: 5000.00
# Hours Rendered  : 15
# 
# Utilization = base monthly pay x hours rendered / 20 = 5000.00 x 15 / 20 = 3750.00  
# 
# ### Instructions
# 
# #### 1
# 
# #### 1.a.
# 
# Write a function `get_utilization` with an argument `hours_rendered` and returns utilization (not percentage).
# 
# 

# In[1]:


# write code here. add more cells as needed.

def get_utilization(hours_rendered):
    utilization = int(hours_rendered)/20
    return utilization


# #### 1.b.
# 
# Write a function `get_takehome_pay` with two arguments `base_monthly_pay` and `hours_rendered` and returns the computed takehome pay as float. This function will presumably call `get_utilization`.
# 
# 
# 

# In[2]:


# write code here. add more cells as needed.

def get_takehome_pay(base_monthly_pay,hours_rendered):
    takehome = int(base_monthly_pay) * get_utilization(hours_rendered)
    return float(takehome)


# #### 2
# 
# #### 2.a.
# 
# Create a **list** variable named `raw_log` that contains **dictionaries** (or **ordered dictionaries** if you use the DictReader method of the Python csv module) for each entry in the time-and-attendance log file `interns-july2020.csv`.

# In[3]:


import csv


raw_log = []
# write code here. add more cells as needed.

with open("interns-july2020.csv","r") as csvfile:
    import_interndata = csv.DictReader(csvfile)
    for i in import_interndata:
        raw_log.append(i)
    
# sample dump of raw_log in interactive mode
raw_log


# #### 2.b.
# 
# Create a new list variable `payroll` based on `raw_logs` but with an additional key `takehome_pay` for each dictionary entry.

# In[4]:


payroll = []

# write code here. add more cells as needed.
payroll = raw_log
counter=0
for employee_dict in payroll:
    payroll[counter]["takehome_pay"] = get_takehome_pay(employee_dict["base_monthly_pay"],employee_dict["hours_rendered"])
    counter+=1
                 
# sample dump of payroll in interactive mode
payroll 


# #### 2.c.
# 
# Looping through the new list variable `payroll`, write a simple payroll spool file named `payslip-july2020.txt` containing Payslips for interns.
# 
# Each record in the Payroll Spool File will look something like this:
# ```
# Payroll Date   : July 25, 2020
# ID             : 2020001
# Base Pay       : 4500
# ------------------------------
# Hours Rendered : 15
# Takehome Pay   : 3375.0
# 
# ______________________________
# 
# ```
# 
# The first few entries of the sample spoolfile provided look something like this:
# ```
# Payroll Date   : July 25, 2020
# ID             : 2020001
# Base Pay       : 4500
# ------------------------------
# Hours Rendered : 15
# Takehome Pay   : 3375.0
# 
# ______________________________
# Payroll Date   : July 25, 2020
# ID             : 2020002
# Base Pay       : 4500
# ------------------------------
# Hours Rendered : 20
# Takehome Pay   : 4500.0
# 
# ______________________________
# Payroll Date   : July 25, 2020
# ID             : 2020003
# Base Pay       : 4500
# ------------------------------
# Hours Rendered : 15
# Takehome Pay   : 3375.0
# 
# ______________________________
# 
# ```
# 
# A sample file `payslip-july2020_test_output.txt` has been provided for your reference. Use this to test your output. Note that both your `payslip-july2020.txt` AND `payslip-july2020_test_output.txt` must match character by character!
# 
# To test this using operating system commands:
# 
# Windows:  `fc payslip-july2020.txt payslip-july2020_test_output.txt`
# Mac:  `diff payslip-july2020.txt payslip-july2020_test_output.txt`
# 

# In[5]:


import csv

# write code here. add more cells as needed.

#                                  An important lesson: 
#
#  .csv files will add quotation marks with strings added that have
#  commas, '\n', or other string attributes. This is so the file knows that the comma
#  does not signify another value. If you want to print specific formatted text files
#  and strings, this might get in the way of how it looks on the file itself...

# Using the built in Python writing method for the .txt file:

# The built in .write also take only one argument, so use the '%s' method for 
# inserting values from iterables:

with open("payslip-july2020.txt","w") as file:

    for employee_dict in payroll:
        file.write("Payroll Date   : July 25, 2020\n")
        file.write("ID             : %s\nBase Pay       : %s\n" 
                   %((employee_dict["id"]),(employee_dict["base_monthly_pay"])))
        file.write('------------------------------\n')
        file.write("Hours Rendered : %s\nTakehome Pay   : %s\n"
                   %((employee_dict["hours_rendered"]),(employee_dict["takehome_pay"])))
        file.write("\n______________________________\n")


# #### 3
# 
# #### 3.a.
# 
# Load the file `interns-masterlist.csv` to a dictionary variable named `intern_master`. The dictionary keys are the ids of the interns.
# 

# In[6]:


intern_master = dict()

# write code here. add more cells as needed.

with open("interns-masterlist.csv","r") as csvfile:
    import_dict = csv.DictReader(csvfile)
    
    for dictionary in import_dict:
        idkey = dictionary["id"]
        accountnum = dictionary["account_number"]
        intern_master[idkey] = accountnum


# The sample output can be seen below
print(intern_master)


# #### 3.b.
# 
# As you can see from the previous question, each intern already has a bank account. All the company needs to do is to tell the bank to pay each intern via a **credit advise** file following a certain format.
# 
# Generate a bank credit advise CSV file `credit-advise-july-2020.csv` for your payroll run.
# 
# The credit advise file should contain the following information:
# * account number (`account_number`)
# * amount to be credited (`amount`), which is the takehome pay
# 
# Account numbers **must not contain spaces**.
# 
# Hint: you will need information from `intern_master` and `payroll` to make this work.
# 
# The first few lines of `credit-advise-july-2020.csv` will look like this:
# 
# ```
# account_number,amount
# 109350005001,4500.0
# 109350005002,3825.0
# 109350005003,3600.0
# 109350005004,3375.0
# 109350005005,3600.0
# 109350005006,4050.0
# 109350005007,3825.0
# ```
# 
# A sample file `credit-advise-july-2020_test_output.csv` has been provided for your reference. Use this to test your output. Note that both your `credit-advise-july-2020.csv` AND `credit-advise-july-2020_test_output.csv` must match character by character!
# 
# To test this using operating system commands:
# 
# Windows:  `fc credit-advise-july-2020.csv credit-advise-july-2020_test_output.csv`
# Mac:  `diff credit-advise-july-2020.csv credit-advise-july-2020_test_output.csv`

# In[7]:


# write code here. add more cells as needed.

with open("credit-advise-july-2020.csv","w") as csvfile:
    field_names = ["account_number","amount"]
    creditwriter = csv.DictWriter(csvfile,fieldnames=field_names)
    
    creditdict = dict()
    space = " "
    i=0
    creditwriter.writeheader()
    for account in intern_master:
        accountnum = intern_master[account]
        if space in accountnum:
            accountnum = accountnum.replace(space,"")
        creditdict["account_number"] = accountnum
        creditdict["amount"] = payroll[i]["takehome_pay"]
        i+=1
        creditwriter.writerow(creditdict)
    


# ### B Spotify and JSON
# 
# **(75 Points)**
# 
# Spotify has a [Developers' Portal](https://developer.spotify.com/) which allows you to write programs to access information about tracks, albums, playlists, recommendations, audio features, and others.
# 
# A dump of new releases as of July 23, 2020 is found in the `spotify-new-releases.json`.
# 
# 

# #### 1.
# 
# #### 1.a. 
# 
# Load the contents of `spotify-new-releases.json` into a **dictionary** variable named `new_releases` resembling the JSON structure.

# In[8]:


import json

# write code here. add more cells as needed.

with open("spotify-new-releases.json","r") as jsonfile:
    spotifyrelease = json.loads(jsonfile.read())
    new_releases=dict(spotifyrelease)


# verify that new_releases is a dictionary
print(type(new_releases))


# #### 1.b.
# 
# Dump contents of new_releases (in script mode)

# In[9]:


# write code here. add more cells as needed.
print(new_releases)


# #### 1.c.
# 
# Define a new **list** variable `albums` and assign the list of albums in new_releases as pointed to by the key `items`. Note that this item is embedded so you need to know how to access it accordingly.
# 
# Dump the contents of `albums` via script mode.
# 

# In[10]:


# write code here. add more cells as needed.
albums = []
albums = new_releases["albums"]["items"]


# dump here
print(albums)


# #### 2.
# 
# #### 2.a.
# 
# Using **one line** of code, generate a list of names of artists for each album in `albums`. Save this list to a new variable named `artist_names`. If there are multiple artists, get the first one only.
# 
# Dump this new list

# In[13]:


# write code here. add more cells as needed.

# This is the string of code that gets each first artist in each artist list:
#     
#        1) albums[i]["artists"] - we need to get counts of i for changing lists in
#           the dictionary key "artists"
#        2) [0]["name"] - gets only the first artist
#        3) for i in range(20) - a conditional that gets the 20 artists in 
#           the list range 'i'
#
# (albums[0]["artists"][0]["name"])

artist_names = [ albums[i]["artists"][0]["name"] for i in range(20)]

# sample output
print(artist_names)


# In[ ]:




