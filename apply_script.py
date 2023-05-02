#! python3

import csv
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction

# Load the CSV file with Room Ids and predicted values
csv_file_path = "predictions.csv"

# Read the CSV file and store the Room Ids and predicted values in a dictionary
room_data = {}
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        room_id = int(row['Room_ID'])
        predicted_value = row['Prediction']
        room_data[room_id] = predicted_value

# Get the current Revit document
doc = __revit__.ActiveUIDocument.Document

# Get all rooms in the Revit model
rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()

# Ask the user for the parameter name they want to update
parameter_name = input("Enter the parameter name you want to update: ")

# Start a new transaction
t = Transaction(doc, "Update Rooms with Predicted Values")
t.Start()

# Update the rooms with the predicted values from the CSV file
for room in rooms:
    room_id = room.Id.IntegerValue

    if room_id in room_data:
        predicted_value = room_data[room_id]

        # Update the room's parameter with the predicted value (replace 'Parameter_Name' with the actual parameter name)
        room_parameter = room.LookupParameter(parameter_name)
        if room_parameter:
            room_parameter.Set(predicted_value)
        else:
            print(f"No parameter found for room {room_id}")

# Commit the transaction
t.Commit()