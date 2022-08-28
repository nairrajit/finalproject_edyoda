
admin_keys = {"rajit123": "rajit123"}

inven={1:{'Name':'Tandoori Chicken','Quantity':4,'Price':240,'Discount':10,'Stock':20},
           2:{'Name':'Vegan Burger','Quantity':1,'Price':320,'Discount':10,'Stock':20},
           3:{'Name':'Truffle Cake','Quantity':500,'Price':200,'Discount':10,'Stock':8},
           } 
# inven={}

a=4 #this is global var to assign automatic foodID,it will incremented after creating a 1 item

def add_new_item():
    global a
    itemid =   a                       
    itemname = input("Enter the Item name: ")
    item_quantity = int(input("Enter food item Quantity "))
    price = int(input("Enter the price of the item: "))
    discount=int(input("Enter the Discount"))
    stock = int(input("Enter the stock value of item: "))         
    inven[itemid] = {
        "ItemName": itemname,
        "item_quantity":item_quantity,
        "Price": price,
        "Discount":discount,
        "Stock": stock
    }
    a+=1
    print("The Item" +itemname+ "is successfully added")
    # return inven


def edit_from_item():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name")
    b = int(input("Enter the Quantity of item"))
    c = int(input("Enter the price of item"))
    d = int(input("Enter the Discount"))
    e = int(input("Enter the stock of the item"))
    inven[item]["ItemName"] = a
    inven[item]["Quantity"] = b
    inven[item]["Price"] = c
    inven[item]["Discount"] = d
    inven[item]["Stock"] = e
    print("*****Edited item successfully*****")
    return inven

def show_inven():
    print("*****HERE IS THE INVENTORY OF FOOD MART*****")
    i=1
    for values in inven.values():
      print("item Id",i, values)
      i+=1
    
    

def remove_item():
    d = int(input("Enter the Item id which you want to REMOVE"))
    inven.pop(d)
    print("Item removed successfully ")
    return inven
