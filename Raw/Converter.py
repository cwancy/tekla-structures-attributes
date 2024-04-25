"""
Excel properties file to C# converter
Author: Clancy Lewis
Date: 27/04/2024

Copyright (c) 2024 Clancy Lewis

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import pandas as pd

excel = pd.read_excel("Attributes_2023.xlsx")

def convert_type(type):
    if type == "FLOAT":
        return "float"
    elif type == "INTEGER":
        return "int"
    elif type == "CHARACTER":
        return "string"
    else:
        return "object"

c = ""
for index, row in excel.iterrows():
    c += f"/// <summary> \n"
    c += f"/// NIL_DESCR \n"
    c += f"/// </summary> \n"
    c += f"/// <returns>{convert_type(row['type'])}</returns> \n"
    c += f"public const string {row['property']} = '{row['property']}'; \n"

with open("output.cs", "w") as file:
    file.write(c)

print("Done")
