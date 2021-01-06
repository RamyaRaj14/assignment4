#menu based app
menu={}
menu['1']="Add Task" 
menu['2']="View All Tasks"
menu['0']="To Exit"
while True: 
  options=menu.keys()
 
  for entry in options: 
    print (entry, menu[entry])
    selection=int(input("Please Select:"))
    if selection =='1': 
      print("Enter Task Name:")
      print("Enter Date:")
    elif selection == '2': 
      print("Enter Task Name:")
      print("Enter Date:") 
    elif selection == '4': 
      print("Bye")
      break
    else:
        print("Please choose correct operation")
    x=input("Do you want to continue yes or no")
    if x!='yes':
        print("exit")
        break