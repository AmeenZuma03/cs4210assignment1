#-------------------------------------------------------------------------
# AUTHOR: Ameen Saleh
# FILENAME: title of the source file
# SPECIFICATION: This program is meant to make a decision tree from my contact lens.csv file
# i was unable to figure out how to complete this part of the task given the time constraint.
# FOR: CS 4210- Assignment #1
# TIME SPENT: Unable to be completed
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
#--> add your Python code here
# X =

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
#--> addd your Python code here
# Y =

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()