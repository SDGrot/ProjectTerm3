# define class called Item , it has 4 parameters (name, amount, price, owner)
class Item:
    def __init__(self, name, amount, price, owner):
        self.name = name
        self.amount = amount
        self.price = price
        self.owner = owner

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def get_price(self):
        return self.price

    def get_owner(self):
        return self.owner

    def show_all(self):
        print(f" Name = {self.name} "
              f" Amount = {self.amount} "
              f" Price = {self.price} "
              f" Owner = {self.owner} ")

    def show_name(self):
        print(f" Name = {self.name} ")

    def show_amount(self):
        print(f" Amount = {self.amount} ")

    def show_price(self):
        print(f" Price {self.price} ")

    def show_owner(self):
        print(f" Owner {self.owner} ")


list_of_items = []  # list for items  needed for new_item_terminal


# append new items to the list_of_items
def new_item_terminal():
    for i in range(len(list_of_items), 99, ):
        x = "item_" + str(i)
        print(x)  # test to see name of item should be item_0 , _1,_2 and so on
        list_of_items.append(x)
        list_of_items[-1] = Item(name=str(input("Name ")),
                                 amount=int(input("Amount ")),
                                 price=float(input("Price ")),
                                 owner=str(input("Owner ")))

        return list_of_items


# similar to new_item_terminal , takes values in func(name,...)
def new_item_for_ui(name, amount, price, owner):
    for i in range(len(list_of_items), 99, ):
        x = "item_" + str(i)
        print(x)  # test to see name of item should be item_0 , _1,_2 and so on
        list_of_items.append(x)
        list_of_items[-1] = Item(name=name,
                                 amount=amount,
                                 price=price,
                                 owner=owner)

        return list_of_items


# func to show all item in item list
def show_all_in_the_list():
    decor_new_window()
    for x in list_of_items:
        x.show_all()
    print("=" * 70)


# some decor for new window
def decor_new_window():
    print("\n" * 15)
    print("=" * 70)


# text in the main menu
def main_menu_text():
    print("Chose option ")
    print("1. Show all items in the list ")  # calls  show_all_in_the_list()
    print("2. Add new item to the list ")  # calls new_item_terminal()
    print("3. Change item  ")  # don't have func
    print("4. Later ( sort func)")  # don't have func
    print("5. Exit") # don't have func
    print("=" * 70)


# algorithm of main menu
def menu_default():
    decor_new_window()
    main_menu_text()
    res = int(input("Enter option "))
    if res == 1:
        show_all_in_the_list()

    elif res == 2:
        new_item_terminal()

    elif res == 3:
        pass
    elif res == 4:
        pass

    elif res == 5:
        pass
    else:
        pass


# some items for tests
# new_item_for_ui(name,amount,owner)
new_item_for_ui("Apple", 24, 4.3, "Den")
new_item_for_ui("Cola", 14, 5.3, "Den")
new_item_for_ui("Beer", 74, 10.3, "Den")
new_item_for_ui("Apple", 8, 9.3, "Sviatoslav")

menu_default()  # calls menu
