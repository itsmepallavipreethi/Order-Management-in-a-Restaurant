from tabulate import tabulate
import sys
class Restaurant:

    def csv_list(self):
        csv = []
        with open("python.csv") as file:
            for items in file:
                sno,item,price = items.strip().split(", ")
                csv.append(int(sno))
                csv.append(item.strip())
                csv.append(int(price))
        return csv


    def breakfast(self):
        print("\n__________________________________________________________Start your day with Infinity Platter breakfast_____________________________________________________")
        breakfst = ([[1, "Dosa", 20], [2, "Idly", 20], [3, "Puri", 30], [4, "Bonda", 40]])
        table = tabulate(breakfst, headers = ["Id", "Item", "Price"], tablefmt = "grid")
        print(table)

    def meals(self):
        print("\n__________________________________________________________Have a good nap after eating Infinity Platter meals___________________________________________________")
        meal = ([[5, "Pulihora", 80],[6, "Full Meals", 120], [7, "Thali", 180],[8, "Veg Pulao", 100],[9, "Chicken Biryani", 250],[10, "Mutton Biryani", 550]])
        table = tabulate(meal, headers = ["Id", "Item", "Price"], tablefmt = "grid")
        print(table)

    def delicacy(self):
        print("\n_________________________________________________________________Eat our delicacies with no regrets______________________________________________________________")
        delicacies = ([[11, "Gulab Jamun", 30], [12, "Halwa", 30],[13, "Rasgulla", 50],[14,"Rasmalai", 50]])
        table = tabulate(delicacies, headers = ["Id", "Item", "Price"], tablefmt = "grid")
        print(table)

    def ice(self):
        print("\n_____________________________________________They say taste Infinity Platter icecream, to taste the essence of heaven____________________________________________")
        icecream = ([[15, "Vanilla", 50],[16, "Chocolate", 50], [17, "Butter Scotch", 50],[18, "Strawberry", 50],[19, "Dark Forest", 100]])
        table = tabulate(icecream, headers = ["Id", "Item", "Price"], tablefmt = "grid")
        print(table)

    def menu(self):
        print("\n1. Breakfast\n2. Meals\n3. Delicacies\n4. Ice Cream\n")
        cate = int(input("Enter the number corresponding to preferences(1, 2, 3, 4): "))
        if cate == 1:
           return self.breakfast()
        elif cate == 2:
           return self.meals()
        elif cate == 3:
           return self.delicacy()
        elif cate == 4:
           return self.ice()

    def order(self):
        print("__________________________________________________________Order here to taste Infinity Platter cuisine____________________________________________________________")
        try:
            cost = 0
            order = []
            check = self.csv_list()
            while True:
                confirm = int(input("\nEnter the number correponding to the item you want to order: "))
                if confirm in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]:
                    print(f"you are ordering {check[check.index(confirm)+1]}")
                    okay = input("Enter yes/no: ").strip()
                    if okay == "yes":
                        while True:
                            plates = int(input("\nEnter number of plates of the item: "))
                            if plates <= 0:
                                print("Enter valid number of plates")
                                pass
                            else:
                                break
                        cost = plates * (check[check.index(confirm)+2]) + cost
                        order.append(check[check.index(confirm)+1])
                        print("\n1.Add another item\n2.Menu\n3.Payment\n4.Exit\n")
                        choose = int(input("Choose your choice by entering the preceding number: "))
                        if choose == 1:
                            pass
                        elif choose == 2:
                            self.menu()
                        elif choose == 3:
                            break
                        elif choose == 4:
                            sys.exit("\n__________________________Please Visit again______________________________\n")
                    else:
                        print("\nChoose your item by entering the ID corresponding to it\n")
                        print("\n1.Add another item\n2.Menu\n3.Payment\n4.Exit")
                        choose = int(input("Choose your choice by entering the preceding number: "))
                        if choose == 1:
                            pass
                        elif choose == 2:
                            self.menu()
                        elif choose == 3:
                            break
                        elif choose == 4:
                            sys.exit("\n__________________________Please Visit again______________________________\n")
                else:
                    print("\nENTERED ID DOES NOT EXIST. PLEASE KINDLY CHOOSE THE ID CORRESPONDING TO THE ITEM YOU WANT TO ORDER")
            print(f"\nFor {', '.join(order)} pay {cost}/-")
            return self.payment(cost)
        except ValueError:
            print("Order\nMenu")
            hel = input("\nEnter your preference from the above list:").title()
            if hel == "Order":
                self.order(cost)
            elif hel == "Menu":
                self.menu()

    def payment(self, cost):
            print("\n______________________________________________________________You are one step away from your food_____________________________________________________\n")
            while True:
                amount = int(input("\nenter the denomination in numbers: "))
                balance =  abs(int(cost) - amount)
                if amount < int(cost):
                    print("\nInsufficient amount enter required amount")
                elif amount > int(cost):
                    print(f"\nAmount in change {balance}/-\n")
                    print("                                                                ****Please visit again****                                              ")
                    break
                elif amount == int(cost):
                    print(f"Amount in change {balance}/-\n")
                    print("                                                                ****Please visit again****                                              ")
                    break


def main():
    print("\n_______________________________________________________Welcome to The Infinity Platter Restaurant__________________________________________________________________\n")
    preferences = ["Menu","Help"]
    for category in range(len(preferences)):
        print(preferences[category])
    prefer = input("\nEnter your preference from the above list: ").lower()
    j1 = Restaurant()
    if prefer == "menu":
        j1.menu()
        j1.order()
    elif prefer == "help":
        print("\n_____PLEASE CHECK OUR MENU TO ORDER_____")
        j1.menu()
        j1.order()

if __name__ == "__main__":
    main()
