str1 = 'interior dEsign application\n'
str2 = str1.title() 
print('\033[0m' + str2)

menu_input = int(input("Select Menu option: "))

def menu_option1():
  pass
  print("option 1 selected.")

def menu_option2():
  pass
  print("option 2 selected.")

def menu_option3():
  pass
  print("option 3 selected.") 

def menu_optionUnknown():
  pass
  print("option selected is unknown.")

def switchCase_func(menu_input):
  my_switch = {
    1:menu_option1, 
    2:menu_option2, 
    3:menu_option3
    }

  my_switch.get(menu_input, menu_optionUnknown)()

switchCase_func(menu_input)
print(menu_option1)
