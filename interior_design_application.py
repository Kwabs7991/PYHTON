import warnings

str1 = 'interior design application\n'
str2 = str1.title() 
print('\033[0m' + str2)
###################################################
'''
# Autumn term 2017 – Programming Project 1: #

Design, write and test a C program to be used by an interior decorator to estimate the cost of painting a room. 

The decorator needs to enter the height of the room (between 2.1 and 4.25 metres), the length and the width of the room (minimum 1.8 metre; maximum 7.5 metres). 
Assuming the room is box shape the program should calculate the ceiling area and the total area of the four walls.
If any plastering is required the ceiling will cost £31 per square metre and walls will cost £22.55 per square metre.

The program should allow a choice of three paints types:
- Luxury quality which costs £3 per square metre
- Standard quality which cost £1.45 per square metre
- Economy quality which costs £0.75 per square metre

The decorator should also be able to choose to use undercoat paint if required, which costs an additional £0.50 per square metre.
An estimate of hours needed for the job should be entered at the keyboard by the decorator. Then the labour cost should be calculated using the estimated hours and an hourly rate of
£17.50 per hour, with a minimum labour charge of £120.
Once all the data has been entered the program should display an itemised estimate including customer name, materials, labour, VAT and a total.
'''
###################################################
class HLW:
    length_input = int(input("Enter Length of Room: "))
    height_input = int(input("Enter Height of Room: "))
    width_input = int(input("Enter Width of Room: "))
    width_input = int(input("Enter Width of Room: "))
    width_input = int(input("Enter Width of Room: "))
        
    def __init__(self, height_input, length_input, width_input, fourwall_Area, ceiling_Area ):
            self.length_input = HLW.length_input
            self.height_input = HLW.height_input
            self.width_input = HLW.width_input
            self.fourwall_Area = fourwall_Area
            self.ceiling_Area = ceiling_Area
        
    def h_l_w_measurements(self):
        print(f"LENGTH MEASURED: {HLW.length_input}")
        print(f"WIDTH MEASURED: {HLW.width_input}")
        print(f"HEIGHT MEASURED: {HLW.height_input}")
        fourwall_Area = 2 * (HLW.length_input + HLW.width_input) * HLW.height_input
        ceiling_Area = HLW.length_input + HLW.width_input
        return f"Area of Four walls: {fourwall_Area} and Area of Ceiling: {ceiling_Area}."
       
        
    def plastering_cost(self, ceiling_Area, fourwall_Area):
        isNeeded = str(input("Are requiring any Plastering? \n Y/N: "))
        if isNeeded == "Y" or "y":
            ceiling_plastering = ceiling_Area * 31
            wall_plastering = fourwall_Area * 22.55
            print(f"Total for plastering job comes to {wall_plastering} for the wall, and {ceiling_plastering} for the ceiling.")
        elif isNeeded == "N" or "n":
            print("No extra plastering job is needed for this purchase. Will continue to next step.")
        else:
            warnings.warn("Warning...........Message")

            
    def display_reciept(self):
        print(f"Height: {self.height}, Length: {self.height}, Ceiling Area: {self.height}")
              
        return "Invoice/Reciept Process Complete."

room1 = HLW(HLW.length_input, HLW.height_input, HLW.width_input)

print(room1.h_l_w_measurements())
print(room1.plastering_cost( ceiling_Area, fourwall_Area))
