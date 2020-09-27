#!/usr/bin/env python
# coding: utf-8

# # Programming Exercise 2: Constraint Satisfaction Problem

# <div class="alert alert-info">
#     <h3>Please read the following important information before starting with the programming exercise: </h3>
#     <p>In order to avoid problems with the relative file path we recommend to place the provided notebook and csp_programming_exercise.py file in the rootfolder of your <b>aima repository</b>.</p> 
#     <p>Do not use/install any additional packages, which are not provided in the requirements.txt of the  <b>aima repository</b>. </p>
#     <p>For modelling the constraint satisfaction problem you will have to define some variables. Do not change the names of variables that we provided you! Since we use these variables for an automatic evaluation, changing  variable names will result in failing the programming exercise. </p>
#     <p>Do not modify the example with the TWO + TWO = FOUR problem!</p>
#     <p>Do not modify the csp_programming_exercise.py!</p>
#     <p>After completing the exercise, download this jupyter notebook as *.py file (File &rarr; Download as 	&rarr; Python (.py)) </p>
#     <p>Before uploading this file together with your jupyter notebook to moodle, check if you can run <i>'python AI_Assignment2.py'</i> inside your anaconda environment in the root folder of your <b>aima repository</b>. If we are not able to run your submitted files in an environment with the packages provided by the requirements.txt of the <b>aima repository</b>, you will fail the programming exercise.</p>
#     
# </div>

# ## Initialization

# In[1]:


# Do not change this part.
from csp_programming_exercise import *
import sys, os
sys.path.append(os.path.realpath("aima"))


# ## Example for Solving a Constraint Satisfaction Problem

# In this exercise we are going to construct the Science Fair problem as a constraint satisfaction problem in Python using the csp library. The "TWO + TWO = FOUR" problem from the exercise (see Problem 3.4) will help us to understand how to model a constraint satisfaction problem with this library.
# 

# ### Constructing the Domains: TWO + TWO = FOUR

# We start with constructing the domains for our problem. As an example the domains for the TWO + TWO = FOUR- problem from the csp library are given. 

# In[2]:


# Do not change this part
# Here we form the domains for the variables: T, F, W, O, U, R, C1, C2 and C3
# Domains are formed using key-value pairs,
# where the key stands for the variable and the value is for the possible values
# set(range(1, 4)) is a short way of creating an array with numbers from 1 to 4
# set (range(1, 4)) == [1, 2, 3]
# Tip: Remember that you can construct arrays with any variable types

domains_TF = {'T': set(range(1, 10)),
           'F': set(range(1, 10)),
           'W': set(range(0, 10)),
           'O': set(range(0, 10)),
           'U': set(range(0, 10)),
           'R': set(range(0, 10)),
           'C1': set(range(0, 2)), 
           'C2': set(range(0, 2)), 
           'C3': set(range(0, 2))
}


# ### Constructing the Constraints: TWO + TWO = FOUR

# We continue with defining the constraints for our problem, the most important part of any constraint satisfaction problem. Let's take a look at the constraints for our "TWO + TWO = FOUR" problem to give you some insight about how to construct constraints with the csp library.

# In[3]:


# Do not change this part
# Here we define our constraints
# The constraint constructor of csp takes two arguments:
# 1. The variables that take part in the constraint
# 2. The constraint itself which is a function that takes the variables as arguments and returns true or false
# all_diff and eq are functions defined in csp 
# Like their name suggest all_diff returns true if every value is different
# and eq returns true if the two values are equal
# Tip: Take a look at the lambda operator in python https://www.w3schools.com/python/python_lambda.asp


constraint1_TF = Constraint(('T', 'F', 'W', 'O', 'U', 'R'), all_diff)
constraint2_TF = Constraint(('O', 'R', 'C1'), lambda o, r, c1: o + o == r + 10 * c1)
constraint3_TF = Constraint(('W', 'U', 'C1', 'C2'), lambda w, u, c1, c2: c1 + w + w == u + 10 * c2)
constraint4_TF = Constraint(('T', 'O', 'C2', 'C3'), lambda t, o, c2, c3: c2 + t + t == o + 10 * c3)
constraint5_TF = Constraint(('F', 'C3'), eq)


# ### Combine the constraints and set up the TWO + TWO = FOUR Problem

# In[4]:


# Do not change this part
# TWO + TWO = FOUR Problem
two_four_constraints = [constraint1_TF, constraint2_TF, constraint3_TF, constraint4_TF, constraint5_TF]
two_four = NaryCSP(domains_TF, two_four_constraints)


# ### Solve the TWO + TWO = FOUR Problem

# In[5]:


# Do not change this part
ac_search_solver(two_four)


# ## Programming Exercise Science Fair 

# ### Constructing the Domains: Science Fair

# In[6]:


# Define your domains here
# Four projects which are done by the students
# each student can select out of four projects
domains = {'Bella': set(range(1, 5)), 
           'Bethany': set(range(1, 5)),
           'Brian': set(range(1, 5)),
           'Brianna': set(range(1, 5)),
           'Ben': set(range(1, 5)),
           'Bill': set(range(1, 5)),
           'Bart':set(range(1, 5)),
           'Solar Powered Car': set(range(1, 2)),
           'Potato Battery': set(range(2, 3)),
           'Baking Powder Volcano': set(range(3, 4)),
           'Our Solar System': set(range(4, 5))
}


# ### Constructing the Constraints: Science Fair

# In[7]:


# Define your constraints here
# Everybody has a project
constraint1 = Constraint(('Bella', 'Bethany', 'Brian', 'Brianna', 'Ben', 'Bill', 'Bart'), 
                         lambda bella, beth, brian, brianna, ben, bill, bart: 
                         bella*beth*brian*brianna*ben*bill*bart > 0)
# No one presents alone
constraint2 = Constraint(('Bella', 'Bethany', 'Brian', 'Brianna', 'Ben', 'Bill', 'Bart', 'Solar Powered Car', 'Potato Battery', 'Baking Powder Volcano', 'Our Solar System'), 
                         lambda bella, beth, brian, brianna, ben, bill, bart, car, battery, volcano, solar: 
                         [bella, beth, brian, brianna, ben, bill, bart].count(car) != 1 and
                         [bella, beth, brian, brianna, ben, bill, bart].count(battery) != 1 and
                         [bella, beth, brian, brianna, ben, bill, bart].count(volcano) != 1 and
                         [bella, beth, brian, brianna, ben, bill, bart].count(solar) != 1)

# Every project is presented by someone
constraint3 = Constraint(('Bella', 'Bethany', 'Brian', 'Brianna', 'Ben', 'Bill', 'Bart', 'Solar Powered Car', 'Potato Battery', 'Baking Powder Volcano', 'Our Solar System'), 
                         lambda bella, beth, brian, brianna, ben, bill, bart, car, battery, volcano, solar: 
                         [bella, beth, brian, brianna, ben, bill, bart].count(car) > 0 and
                         [bella, beth, brian, brianna, ben, bill, bart].count(battery) > 0 and
                         [bella, beth, brian, brianna, ben, bill, bart].count(volcano) > 0 and
                         [bella, beth, brian, brianna, ben, bill, bart].count(solar) > 0)
# up to 4 people at solar car
constraint4 = Constraint(('Bella', 'Bethany', 'Brian', 'Brianna', 'Ben', 'Bill', 'Bart', 'Solar Powered Car'), 
                         lambda bella, beth, brian, brianna, ben, bill, bart, car: 
                         [bella, beth, brian, brianna, ben, bill, bart].count(car) < 5)
# up to 3 people at potato battery
constraint5 = Constraint(('Bella', 'Bethany', 'Brian', 'Brianna', 'Ben', 'Bill', 'Bart', 'Potato Battery'), 
                         lambda bella, beth, brian, brianna, ben, bill, bart, battery: 
                         [bella, beth, brian, brianna, ben, bill, bart].count(battery) < 4)
# 3 to 5 people on volcano
constraint6 = Constraint(('Bella', 'Bethany', 'Brian', 'Brianna', 'Ben', 'Bill', 'Bart', 'Baking Powder Volcano'), 
                         lambda bella, beth, brian, brianna, ben, bill, bart, volcano: 
                         ([bella, beth, brian, brianna, ben, bill, bart].count(volcano) < 6 and
                         [bella, beth, brian, brianna, ben, bill, bart].count(volcano) > 2) or
                         [bella, beth, brian, brianna, ben, bill, bart].count(volcano) == 0)
# solar system is for 2 people
constraint7 = Constraint(('Bella', 'Bethany', 'Brian', 'Brianna', 'Ben', 'Bill', 'Bart', 'Our Solar System'), 
                         lambda bella, beth, brian, brianna, ben, bill, bart, solar: 
                         [bella, beth, brian, brianna, ben, bill, bart].count(solar) == 2 or
                         [bella, beth, brian, brianna, ben, bill, bart].count(solar) == 0)   
# Bart presents with Bethany
constraint8 = Constraint(('Bart', 'Bethany'), eq)
# Brian, Bill and Ben don't present together
constraint9 = Constraint(('Brian', 'Bill', 'Ben'), all_diff)
# Bill and Brianna don't want to present volcano project
constraint10 = Constraint(('Bill', 'Brianna', 'Baking Powder Volcano'), lambda bill, brianna, volcano: 
                          bill != volcano and brianna != volcano)
# Bella and Bill present potato battery
constraint11 = Constraint(('Bella', 'Bill', 'Potato Battery'), lambda bella, bill, battery:
                         bella == battery and
                         bill == battery)
# Bella presents with at least one girl
constraint12 = Constraint(('Bella', 'Bethany', 'Brianna'), 
                         lambda bella, beth, brianna: 
                         beth == bella or brianna == bella)
# No one presents solar system
constraint13 = Constraint(('Bella', 'Bethany', 'Brian', 'Brianna', 'Ben', 'Bill', 'Bart', 'Our Solar System'), 
                         lambda bella, beth, brian, brianna, ben, bill, bart, solar: 
                         (bella | beth | brian | brianna | ben | bill | bart) & solar != solar)
# Brian and Brianna present together
constraint14 = Constraint(('Brian', 'Brianna'), eq)


# ### Combine the constraints and set up the CSPs for the different problems

# <div class="alert alert-info">
#     <p>The variables csp_21, csp_22, .. are defined for setting up the CSPs for the corresponding problems. You have to use these variable names otherwise this will result in failing the programming exercise. For setting up the CSPs, you have to use the NaryCSP class (without any modifications) from the module csp_programming_exercise which was imported before. </p> 
# </div>

# In[8]:


# Construct the Science Fair Problems

# Combine Constraints and set up the csp for Problem 2.1
# TODO: csp_21 = 
csp_21_constraint = [constraint1, constraint2, constraint4, constraint5, constraint6, constraint7, 
                     constraint8, constraint9, constraint10, constraint11, constraint12]
csp_21 = NaryCSP(domains, csp_21_constraint)

# Combine Constraints and set up the csp for Problem 2.2 
# TODO: csp_22 =
csp_22_constraint = [constraint1, constraint3, constraint4, constraint5, constraint6, constraint7, 
                     constraint8, constraint9, constraint10, constraint12]
csp_22 = NaryCSP(domains, csp_22_constraint)

# Combine Constraints and set up the csp for Problem 2.3
# TODO: csp_23 = 
csp_23_constraint = [constraint1, constraint3, constraint4, constraint5, constraint6, constraint7, 
                     constraint10, constraint11, constraint12]
csp_23 = NaryCSP(domains, csp_23_constraint)

# Combine Constraints and set up the csp for Problem 2.4
# TODO: csp_24 =
csp_24_constraint = [constraint1, constraint2, constraint4, constraint5, constraint6, constraint7, 
                     constraint10, constraint11, constraint12, constraint13]
csp_24 = NaryCSP(domains, csp_24_constraint)

# Combine Constraints and set up the csp for Problem 2.5
# TODO: csp_25 =
csp_25_constraint = [constraint1, constraint2, constraint4, constraint5, constraint6, constraint7, 
                     constraint8, constraint9, constraint10, constraint11, constraint13]
csp_25 = NaryCSP(domains, csp_25_constraint)

# Combine Constraints and set up the csp for Problem 2.6
# TODO: csp_26 =
csp_26_constraint = [constraint1, constraint2, constraint4, constraint5, constraint6, constraint7, 
                     constraint10, constraint11, constraint12, constraint14]
csp_26 = NaryCSP(domains, csp_26_constraint)


# ### Solving the CSP

# <div class="alert alert-info">
#     <p>Do not change the following cell. If you can't execute the following cell, you may have renamed the variables defined by us.</p> 
# </div>

# In[9]:


print(ac_search_solver(csp_21))
print(ac_search_solver(csp_22))
print(ac_search_solver(csp_23))
print(ac_search_solver(csp_24))
print(ac_search_solver(csp_25))
print(ac_search_solver(csp_26))

