#! python3

import csv
import os.path
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, StorageType
import string

def remove_non_printable_chars(s):
    return "".join([c for c in s if c in string.printable])


def extract_data(input_parameter_names, output_parameter_names):
    doc = __revit__.ActiveUIDocument.Document
    collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()

    data = []

    for room in collector:
        inputs = []
        outputs = []

        for input_name in input_parameter_names:
            input_parameter = room.LookupParameter(input_name)
            if input_parameter:
                if input_parameter.StorageType == StorageType.String:
                    inputs.append(input_parameter.AsString())
                elif input_parameter.StorageType == StorageType.Double:
                    inputs.append(input_parameter.AsDouble())
            else:
                print(f"No input parameter found with name {input_name} for room {room.Id}")
            print(inputs)
        for output_name in output_parameter_names:
            output_parameter = room.LookupParameter(output_name)
            if output_parameter:
                if output_parameter.StorageType == StorageType.String:
                    outputs.append(output_parameter.AsString())
                elif output_parameter.StorageType == StorageType.Double:
                    outputs.append(output_parameter.AsDouble())

            else:
                print(f"No output parameter found with name {output_name} for room {room.Id}")
            print(outputs)
        if inputs and outputs:
            data.append(inputs + outputs)

    return data


def main():
    input_parameter_names = input("Enter the names of the input parameters, separated by commas:")
    output_parameter_names = input("Enter the names of the output parameters, separated by commas:")


    input_parameter_names = input_parameter_names.split(",")

    output_parameter_names = output_parameter_names.split(",")



    data = extract_data(input_parameter_names, output_parameter_names)

    file_path = os.path.join(os.path.expanduser("~"), "Desktop", "data.csv")

    with open(file_path, 'w', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        header_row = [remove_non_printable_chars(name).strip() for name in input_parameter_names] + [remove_non_printable_chars(name).strip() for name in output_parameter_names]
        writer.writerow(header_row)
        for row in data:
            writer.writerow(row)

    print("Data extraction completed. File saved at: " + file_path)


if __name__ == "__main__":
    main()
