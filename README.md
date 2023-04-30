# Revit-Autofiller: from Schematic Design to Design Development

Architecture design has several phases, starting from schematic design, design development, construction documents, to bidding and construction administration. Basicly, it is an idea evolving through different phases into a product. With the help of machine learning, it is possible to auto-complete parts of the project so that designers can focus more on the individual cases and the creative work.

![Revit autofillor](https://user-images.githubusercontent.com/17108049/235349767-752b5057-082a-476c-b942-370006c26971.png)

In this project, we used Naive Bayes Classifier to predict door parameters from the rooms names in a hospital project. 


The idea is to use the information from previous projects to speed up the design development phase of the project. The data source are the past revit projects. Many DD (design development) parameters can be predicted from the a simple room name or department name from SD (schematic design) phase. 

We extracted with data from Revit using Pyrevit and Revit API. Then train a Naive Bayes classifier based on the data extracted. Next, we use the model to predict on new project data and load it back in the Revit model. 

Currently we have a general accuracy of 90% on the prediction so the value still has to be verified by human case by case to be applied on an architectural project. This work process has a lot of potential and can be applied on different type of elements. 



