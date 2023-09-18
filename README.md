# Revit-Autofiller: from Schematic Design to Design Development

Architecture design has several phases, starting from schematic design, design development, construction documents, to bidding and construction administration. Basicly, it is an idea evolving through different phases into a product. With the help of machine learning, it is possible to auto-complete parts of the project so that designers can focus more on the individual cases and the creative work.

![Revit autofillor](https://user-images.githubusercontent.com/17108049/235349767-752b5057-082a-476c-b942-370006c26971.png)

In this project, we used Random Forest Classifier to predict door parameters from the rooms names in a hospital project. 


The idea is to use the information from previous projects to speed up the design development phase of the project. The data source are 40 revit projects. With 15000 door element, we trained different models to use the room name that the door opens to to predict the door parameters for cost estimation.   

After trying out different input parameters, we find out that using the room names and the dimension of the door openings could capture the most information for prediction. 

Currently we have a general accuracy of 90% on the prediction so the value still has to be verified by human case by case to be applied on an architectural project. This work process has a lot of potential and can be applied on different type of elements.

 ![heatmap_new_tb_material](https://github.com/shicongcao/ML-Revit-Optimization/assets/17108049/b4f4734d-a099-4f75-922b-f979456ecbb0)
