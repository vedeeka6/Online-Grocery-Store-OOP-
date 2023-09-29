from abc import ABCMeta,abstractmethod
class User(metaclass=ABCMeta):               #defining abstract class
    def set_username(self):
        self.__username = input('USERNAME : ')
    def set_password(self):
        self.__password = input('PASSWORD : ')
    def get_username(self):
        return self.__username
    def get_password(self):
        return self.__password
    @abstractmethod                           #defining abstract method
    def login(self):
        pass


class Admin(User):   #admin class inherited from user class
    def __init__(self):                       #admin's information made private
        self.__admin_username = 'oop-adm4679'
        self.__admin_password = 'admin5678'
        self.__admin_email = 'admin987@gmail.com'
        self.__admin_captcha = 'R e N a J i x 2 0 8'


    def login(self):                     #method overriding
        while True:
            super().set_username()
            super().set_password()
            self.username = super().get_username()
            self.password = super().get_password()
            if self.username == self.__admin_username and self.password == self.__admin_password:
                while True:
                    self.email = input('EMAIL : ')
                    if self.email == self.__admin_email:
                        while True:
                            print('ARE YOU HUMAN?')
                            captcha = input('COPY THE GIVEN CODE\nR e N a J i x 2 0 8 : ')
                            if captcha == self.__admin_captcha:
                                BOLD = '\033[1m'
                                END = '\033[0m'
                                YELLOW = '\033[93m'
                                print(BOLD+YELLOW+'YOU HAVE SUCCESSFULLY LOGGED IN'+END)
                                while True:
                                    option = input('\n1. DISPLAY PRODUCTS \n2. MANAGE STOCK\n3. VIEW CUSTOMER SHOPPING HISTORY\n4. EXIT')
                                    if option == '1':
                                        admin.products_display()
                                    elif option == '2':
                                        admin.stock_manage()
                                    elif option == '3':
                                        admin.history_display()
                                    else:
                                        BOLD = '\033[1m'
                                        END = '\033[0m'
                                        YELLOW = '\033[93m'
                                        print(BOLD+YELLOW+'      EXITED\n     ThankYou\n----MyShop.com----'+END)

                                        break

                                break
                            else:
                                BOLD = '\033[1m'
                                RED = '\033[91m'
                                END = '\033[0m'

                                print(BOLD+RED+'INCORRECT'+END)
                        break
                    else:
                        BOLD = '\033[1m'
                        RED = '\033[91m'
                        END = '\033[0m'
                        print(RED+BOLD+'INVALID EMAIL'+END)
                        continue
                break
            else:
                BOLD = '\033[1m'
                RED = '\033[91m'
                END = '\033[0m'
                print(BOLD+RED+'INVALID USERNAME OR PASSWORD'+END)
                continue

    def products_display(self):           #this function displays the stock to admin
        from tabulate import tabulate
        self.product_list = []
        with open('products', 'r') as f:
            for lines in f:
                product = lines.rstrip()
                product = product.split(',')
                self.product_list.append(product)
        BOLD = '\033[1m'
        YELLOW = '\033[93m'
        END = '\033[0m'
        print(BOLD+YELLOW+'AVAILABLE PRODUCTS------------MyShop.com'+END)
        print(tabulate(self.product_list, headers=['PRODUCTS', 'PRICE(RS)', 'QUANTITY'], tablefmt='fancy_grid'))

    def history_display(self):          #this function let the admin view all customer's history
        with open('users', 'a+') as f:
            f.seek(0)
            l = []
            for line in f:
                lst = line.strip()
                lst = lst.split('/')
                l.append(lst)
            final = []
            for i in l:
                new = i[2]
                final.append(new)
        for name in range(len(final)):
            print('\n' + '-' * 30)
            print('CUSTOMER NAME : ', (l[name][0]).upper(), (l[name][1]).upper())
            print('-' * 30)
            shopping_history = open(final[name], 'r')
            file = []
            for lines in shopping_history:
                history = lines.split(',')
                file.append(history)
            for i in range(len(file)):
                print('DATE : ', file[i][0], '\nTIME : ', file[i][1])
                file[i].pop(0)
                file[i].pop(0)
                from tabulate import tabulate
                from prettytable import PrettyTable
                order = []
                for j in range(0, len(file[i]), 3):
                    lst = []
                    lst.append(file[i][j])
                    lst.append(file[i][j + 1])
                    lst.append(file[i][j + 2])
                    order.append(lst)
                BOLD = '\033[1m'
                YELLOW = '\033[93m'
                END = '\033[0m'
                print(BOLD + YELLOW + 'SHOPPING HISTROY----------MyShop.com' + END)
                print(tabulate(order, headers=['PRODUCTS', 'PRICE', 'QUANTITY'], tablefmt='fancy_grid'))
                self.display_table = PrettyTable(['Item Name', 'Item Price', 'Item Quantity'])

    def stock_manage(self):           #this function allows admin to make changes to the stock
        def admin_add():              #this function allows admin to add desired products from stock
            while True:
                name = input('ENTER THE NAME OF YOUR ITEM:').upper()
                price = int(input('ENTER THE PRICE OF YOUR ITEM:'))
                quantity = int(input('ENTER THE QUANTITY OF YOUR ITEM:'))
                BOLD = '\033[1m'
                END = '\033[0m'
                YELLOW = '\033[93m'
                print(BOLD+YELLOW+name, ' HAS BEEN ADDED TO THE STOCK SUCCESSFULLY!!'+END)
                with open('products', 'a') as f:
                    f.write(name + ',' + str(price) + ',' + str(quantity)+'\n')
                    f.flush()
                option = (input('WANT TO ADD MORE? [Y/N] : ')).upper()
                if option == 'N':
                    break


        def admin_remove():            #this function allows admin to remove desired products from stock
            class ItemNotFound(Exception):
                pass
            with open('products', 'a+') as f:
                f.seek(0)
                l = []
                products=[]
                for line in f:
                    lst = line.strip()
                    lst = lst.split(',')
                    l.append(lst)
                for product in l:
                    products.append(product[0])
                while True:
                    try:                    #exception handling
                        name = input('NAME THE ITEM YOU WOULD LIKE TO REMOVE:').upper()
                        if name not in products:
                            raise ItemNotFound
                        else:
                            l = [i for i in l if name != i[0]]
                            BOLD = '\033[1m'
                            END = '\033[0m'
                            YELLOW = '\033[93m'
                            print(BOLD+YELLOW+name, 'HAS BEEN REMOVED FROM THE STOCK!!'+END)
                            option = (input('WANT TO REMOVE MORE? [Y/N] : ')).upper()
                            if option == 'N':
                                break


                    except ItemNotFound:
                        BOLD = '\033[1m'
                        RED = '\033[91m'
                        END = '\033[0m'
                        print(BOLD+RED+'THIS ITEM IS NOT IN YOUR PRODUCT LIST..'+END)

                f.truncate(0)
                for i in l:
                    if i != -1:
                        f.write(i[0] + ',' + i[1] + ',' + i[2])
                        f.write('\n')
                    else:
                        f.write(i[0] + ',' + i[1] + ',' + i[2])


        def update_price():               #this function allows admin to change price of desired products existing in stock
            with open('products', 'a+') as f:
                f.seek(0)
                l = []
                for line in f:
                    lst = line.strip()
                    lst = lst.split(',')
                    l.append(lst)
                while True:
                    name = input('ENTER NAME OF THE PRODUCT YOU WANT TO CHANGE PRICE OF : ').upper()
                    final = []
                    for i in l:
                        new = i[0]
                        final.append(new)
                    if name not in final:
                        BOLD = '\033[1m'
                        RED = '\033[91m'
                        END = '\033[0m'
                        print(BOLD+RED+'THIS ITEM DOESNT EXIST!!'+END)
                    else:
                        for i in l:
                            if name == i[0]:
                                new_price = int(input('ENTER THE UPDATED PRICE:'))
                                i[1] = new_price
                                BOLD = '\033[1m'
                                END = '\033[0m'
                                YELLOW = '\033[93m'
                                print(BOLD+YELLOW+'THE PRICE OF', name, 'HAS BEEN UPDATED!!'+END)
                    option = (input('DO YOU WANT TO UPDATE PRICE OF MORE PRODUCTS? [Y/N]: ')).upper()
                    if option == 'N':
                        break
                f.truncate(0)
                for i in l:
                    f.write(str(i[0]) + ',' + str(i[1]) + ',' + str(i[2]))
                    f.write('\n')


        def update_quantity():             #this function allows admin to change quantity of desired products existing in stock
            with open('products', 'a+') as f:
                f.seek(0)
                l = []
                for line in f:
                    lst = line.strip()
                    lst = lst.split(',')
                    l.append(lst)
                while True:
                    name = input('ENTER THE NAME OF THE PRODUCT:').upper()
                    final = []
                    for i in l:
                        new = i[0]
                        final.append(new)
                    if name not in final:
                        BOLD = '\033[1m'
                        RED = '\033[91m'
                        END = '\033[0m'
                        print(BOLD+RED+'THIS ITEM DOESNT EXIST!!'+END)
                    else:
                        for i in l:
                            if name == i[0]:
                                new_quantity = int(input('ENTER THE UPDATED QUANTITY:'))
                                i[2] = new_quantity
                                BOLD = '\033[1m'
                                END = '\033[0m'
                                YELLOW = '\033[93m'
                                print(BOLD+YELLOW+'THE QUANTITY OF', name, 'HAS BEEN UPDATED!!'+END)
                    option = (input('DO YOU WANT TO UPDATE QUANTITY OF MORE PRODUCTS? [Y/N]: ')).upper()
                    if option == 'N':
                        break
                f.truncate(0)
                for i in l:
                    f.write(str(i[0]) + ',' + str(i[1]) + ',' + str(i[2]))
                    f.write('\n')

        BOLD = '\033[1m'
        END = '\033[0m'
        YELLOW = '\033[93m'

        print(BOLD+YELLOW+'WELCOME TO STOCK MANAGER of MyShop.com!!'+END)
        while True:
            select = int(input('PRESS 1 FOR ADDING ITEMS IN THE STOCK\nPRESS 2 FOR REMOVING ITEMS FROM THE STOCK\nPRESS 3 TO UPDATE THE PRICE OF EXISTING ITEMS\nPRESS 4 TO UPDATE THE QUANTITY OF EXISTING ITEMS:\nPRESS 5 TO GO BACK'))

            if select == 1:
                admin_add()
            elif select == 2:
                admin_remove()
            elif select == 3:
                update_price()
            elif select == 4:
                update_quantity()
            elif select==5:
                break

class Customer(User):       #customer class inherited from user class
    def __init__(self):
        self.file = open('users', 'r')
        self.file = self.file.read().split('/')

    def login(self):             #method overriding
        while True:
            super().set_username()
            super().set_password()
            self.username = super().get_username()
            self.password = super().get_password()
            if self.username in self.file and self.password in self.file:
                BOLD = '\033[1m'
                END = '\033[0m'
                YELLOW = '\033[93m'
                print(BOLD+YELLOW+'YOU HAVE LOGGED IN SUCCESSFULLY'+END)
                break
            else:
                BOLD = '\033[1m'
                RED = '\033[91m'
                END = '\033[0m'
                print(BOLD+RED+'INVALID USERNAME OR PASSWORD'+END)
                continue


    def signup(self):
        self.first_name = input('FIRST NAME : ')
        self.last_name = input('LAST NAME : ')
        self.address = input('ADDRESS: ')
        self.shipping_info = input('SHIPPING INFORMATION\nENTER CITY AND REGION SEPARATED BY COMMAS :')
        self.user_file = open('users', 'a+')
        while True:
            super().set_username()
            self.username = super().get_username()
            if self.username in self.file:
                BOLD = '\033[1m'
                RED = '\033[91m'
                print(RED+BOLD+'USERNAME ALREADY EXISTS')
            else:
                break
        while True:
            super().set_password()
            self.password = super().get_password()
            if self.password in self.file:
                BOLD = '\033[1m'
                RED = '\033[91m'
                print(BOLD+RED+'PASSWORD ALREADY EXISTS')
            else:
                BOLD = '\033[1m'
                END = '\033[0m'
                YELLOW = '\033[93m'
                print(BOLD+YELLOW+'YOU HAVE SIGNED UP SUCCESSFULLY'+END)
                break

    def shopping(self):        #a function that contains the code of whole shopping process
        while True:
            print('1.ADD ITEM\n2.VIEW SHOPPING HISTORY\n3.VIEW EXISTING CART\n4.EXIT')
            choice = input('PRESS [1 OR 2 OR 3 OR 4] : ')
            if choice == '1':
                products_available = Product()
                products_available.display_products()
                products_available.cart_items.add_item()
                usershopping = products_available.cart_items
                while True:
                    print('1.VIEW CART\n2.REMOVE ITEMS\n3.ORDER\n4.BACK')
                    choice2 = input('PRESS [1,2,3 OR 4] : ')
                    if choice2 == '1':

                        usershopping.display_current_cart()
                    elif choice2 == '2':
                        products_available.cart_items.remove_item()
                    elif choice2 == '3':
                        usershopping.updated_cart.place_order()
                        usershopping.updated_cart.checkout()
                        while True:
                            choice3 = input('1.VIEW ORDER\n2.CHECKOUT\n3.BACK\n[PRESS 1,2 OR 3] : ')
                            user_order = usershopping.updated_cart
                            if choice3 == '1':
                                user_order.display_orders()
                            elif choice3 == '2':
                                choice4 = (input('ARE YOU SURE YOU WANT TO CHECKOUT? [Y/N] : ')).upper()
                                if choice4 == 'Y':
                                    user_order.bill_calculation.calculate_bill()
                                    user_order.bill_calculation.display_total_bill()
                                    user_order.save_to_file()
                                    break
                                break
                            else:
                                break
                    elif choice2 == '4':
                        break
            elif choice == '2':
                customer.view_shopping_history()
            elif choice == '3':
                products_available = Product()
                usershopping = products_available.cart_items
                usershopping.updated_cart.display_cart()
            else:
                BOLD = '\033[1m'
                END = '\033[0m'
                YELLOW = '\033[93m'
                print(BOLD+YELLOW+'      EXITED\n     ThankYou\n----MyShop.com----'+END)
                break


    def update_details(self):          #this function saves a new customer's information to the users file
        self.user_file = self.user_file.write('\n' + self.first_name + '/' + self.last_name + '/' + self.username + '/'+ self.password+'/'+self.address+'/'+self.shipping_info)

        self.history_file = open(self.username, 'w')
        self.cart_file = open(self.password, 'w')

    def view_shopping_history(self):         #a function that displays the customer's history
        shopping_history = open(self.username, 'r')
        file = []
        for lines in shopping_history:
            history = lines.split(',')
            file.append(history)
        if file != []:
            for i in range(len(file)):
                print('DATE : ', file[i][0], '\nTIME : ', file[i][1])
                file[i].pop(0)
                file[i].pop(0)
                from tabulate import tabulate
                from prettytable import PrettyTable
                order = []
                for j in range(0, len(file[i]), 3):
                    lst = []
                    lst.append(file[i][j])
                    lst.append(file[i][j + 1])
                    lst.append(file[i][j + 2])
                    order.append(lst)
                BOLD = '\033[1m'
                YELLOW = '\033[93m'
                END = '\033[0m'
                print(BOLD + YELLOW + 'SHOPPING HISTORY-----------MyShop.com' + END)

                print(tabulate(order, headers=['PRODUCTS', 'PRICE', 'QUANTITY'], tablefmt='fancy_grid'))
                self.display_table = PrettyTable(['Item Name', 'Item Price', 'Item Quantity'])
        else:
            BOLD = '\033[1m'
            YELLOW = '\033[93m'
            END = '\033[0m'
            print(BOLD + YELLOW + "YOUR HISTORY DOESN'T EXIST YET" + END)

class Product:
    def __init__(self):
        self.list_of_products = []
        self.cart_items = ShoppingCart(self.list_of_products)        #composition of product and shopping cart class
    def display_products(self):         #displays available products to the customer
        from tabulate import tabulate
        from prettytable import PrettyTable
        with open('products', 'r') as f:
            for line in f:
                lst = line.rstrip()
                lst = lst.split(',')
                self.list_of_products.append(lst)
        BOLD = '\033[1m'
        YELLOW = '\033[93m'
        END = '\033[0m'
        print(BOLD + YELLOW + 'AVAILABLE PRODUCTS-------------MyShop.com' + END)
        print(tabulate(self.list_of_products, headers=['PRODUCTS', 'PRICE', 'QUANTITY'], tablefmt='fancy_grid'))
        self.display_table = PrettyTable(['Item Name', 'Item Price', 'Item Quantity'])
        # self.cart_items.add_item()

class ShoppingCart:
    def __init__(self, product_list):
        self.product_list = product_list
        self.current_cart = []
        self.updated_cart = Order(self.current_cart)              #composition of shopping cart and order class
        self.pwd=Admin.get_password(customer)
    def add_item(self):               #allows customer to add items to his cart
        class ItemNotFound(Exception):
            pass
        with open(self.pwd,'r') as file:
            previous_list=[]
            for line in file:
                lst = line.strip()
                lst=lst.split(',')
                previous_list.append(lst)
        while True:
            try:                        #exception handling
                self.add_to_cart = (input('ENTER PRODUCT NAME: ')).upper()
                check_list = []
                for i in self.product_list:
                    new = i[0]
                    check_list.append(new)
                if self.add_to_cart not in check_list:
                    raise ItemNotFound
                else:
                    for product in range(len(self.product_list)):
                        if self.add_to_cart == self.product_list[product][0]:
                            self.total_quantity = int(input('ENTER QUANTITY OF PRODUCT: '))
                            if self.total_quantity <= int(self.product_list[product][2]):
                                for i in previous_list:
                                    if self.add_to_cart==i[0]:
                                        self.total_quantity+=int(i[2])
                                        previous_list.remove(i)
                                self.current_cart.append([self.add_to_cart, int(self.product_list[product][1]), self.total_quantity])
                            else:
                                BOLD = '\033[1m'
                                RED = '\033[91m'
                                END = '\033[0m'
                                print(BOLD+RED+'SORRY:( WE HAVE ONLY', BOLD+RED+str(self.product_list[product][2])+END)
                option = (input('WANT TO ADD MORE PRODUCTS(Y/N): ')).upper()
                if option == 'N':
                    break
            except ItemNotFound:
                BOLD = '\033[1m'
                RED = '\033[91m'
                END = '\033[0m'
                print(RED+BOLD+'ITEM NOT FOUND'+END)

        self.current_cart += previous_list
        with open(self.pwd, 'w') as file:
            for item in self.current_cart:
                file.write(item[0] + ',' + str(item[1]) + ',' + str(item[2]) + '\n')
                file.flush()



    def remove_item(self):             #allows customer to add items to his cart
        class ItemNotFound(Exception):
            pass
        with open(self.pwd, 'r') as f:
            self.current_cart = []
            for line in f:
                lst = line.rstrip()
                lst = lst.split(',')
                self.current_cart.append(lst)
        while True:
            try:                       #exception handling
                check_list=[]
                remove_item = (input('ENTER PRODUCT NAME YOU WANT TO REMOVE:')).upper()
                for i in self.current_cart:
                    new = i[0]
                    check_list.append(new)
                if remove_item not in check_list:
                    raise ItemNotFound
                self.current_cart = [order for order in self.current_cart if remove_item != order[0]]
                option = (input('DO YOU WANT TO REMOVE MORE PRODUCTS? [Y/N]: ')).upper()
                if option == 'N':
                    break
            except ItemNotFound:
                BOLD = '\033[1m'
                RED = '\033[91m'
                END = '\033[0m'
                print(BOLD+RED+'OOPS! THIS ITEM IS NOT IN YOUR CART..'+END)
        with open(self.pwd,'w') as f:
            for item in self.current_cart:
                f.write(item[0] + ',' + str(item[1]) + ',' + str(item[2]) + '\n')
                f.flush()
    def display_current_cart(self):                 #display the current cart of customer
        from tabulate import tabulate
        with open(self.pwd, 'r') as f:
            table_data = []
            for line in f:
                lst = line.rstrip()
                lst = lst.split(',')
                if lst[2] != '0':
                    table_data.append(lst)

        BOLD = '\033[1m'
        YELLOW = '\033[93m'
        END = '\033[0m'
        print(BOLD + YELLOW + 'CURRENT CART----------------MyShop.com' + END)

        print(tabulate(table_data, headers=['PRODUCT', 'PRICE', 'QUANTITY'], tablefmt='fancy_grid'))


class Order:
    def __init__(self,obj):
        self.current_cart = obj
        self.order_list = []
        self.user_password = User.get_password(customer)
        self.bill_calculation = Bill(self.order_list)          #composition of bill and order class

    def display_cart(self):           #displays the existing cart from the last log in
        from tabulate import tabulate

        with open(self.user_password, 'r') as f:
            table_data = []
            for line in f:
                lst = line.rstrip()
                lst = lst.split(',')
                if lst[2] != '0':
                    table_data.append(lst)
        BOLD = '\033[1m'
        YELLOW = '\033[93m'
        END = '\033[0m'
        print(BOLD + YELLOW + 'EXISTING CART--------------MyShop.com' + END)
        print(tabulate(table_data, headers=['PRODUCTS', 'PRICE', 'QUANTITY'], tablefmt='fancy_grid'))

    def place_order(self):           #allows customer to order items he placed in his cart
        while True:
            self.order_place = (input('ENTER THE NAME OF THE PRODUCT YOU WANT TO ORDER: ')).upper()

            check_list = []
            for i in self.current_cart:
                check_list.append(i[0])
            if self.order_place not in check_list:
                BOLD = '\033[1m'
                RED = '\033[91m'
                END = '\033[0m'
                print(BOLD+RED+'SORRY ! THIS ITEM IS NOT AVAILABLE IN YOUR CART\nPLACE ORDER AGAIN'+END)
            else:
                for product in range(len(self.current_cart)):
                    if self.order_place == self.current_cart[product][0]:
                        self.quantity = int(input('HOW MUCH QUANTITY: '))
                        if self.quantity <= int(self.current_cart[product][2]):
                            self.order_list.append([self.order_place,self.current_cart[product][1], self.quantity])
                        else:
                            BOLD = '\033[1m'
                            RED = '\033[91m'
                            END = '\033[0m'
                            print(BOLD+RED+'SORRY:( YOU HAVE ONLY', BOLD+RED+str(self.current_cart[product][2]), BOLD+RED+'IN YOUR CART\nPLACE ORDER AGAIN'+END)


            more = (input('WANT TO PLACE MORE(Y/N): ')).upper()
            if more == 'N':
                break
    def display_orders(self):           #displays table of items customer ordered from his cart
        from tabulate import tabulate
        BOLD = '\033[1m'
        YELLOW = '\033[93m'
        END = '\033[0m'
        print(BOLD + YELLOW + 'ORDERS----------MyShop.com' + END)
        print(tabulate(self.order_list, headers=['PRODUCTS','PRICE', 'QUANTITY']))
        print('-'*35)
    def manage_cart(self):        #removes the ordered items from the cart
        for order in range(len(self.order_list)):
            if self.order_list[order] in self.current_cart:
                self.current_cart.remove(self.order_list[order])
            for items in range(len(self.current_cart)):
                if self.order_list[order][0] == self.current_cart[items][0]:
                    self.current_cart[items][2]=int(self.current_cart[items][2])
                    self.current_cart[items][2] -= self.order_list[order][2]

    def save_to_file(self):        #records customers cart and history into respective files
        name = User.get_username(customer)
        pwd = User.get_password(customer)
        from datetime import date
        from datetime import datetime
        date = date.today()
        time = datetime.now()
        time = time.strftime('%H:%M:%S')
        if self.order_list != []:
            with open(name, 'a+') as user_history:
                user_history.write(str(date) + ',' + str(time) + ',')
                for i in range(len(self.order_list)):
                    for j in range(len(self.order_list[i])):
                        if "'" not in str(self.order_list[i][j]):
                            if self.order_list[i][j] == self.order_list[-1][-1]:
                                user_history.write(str(self.order_list[i][j])+'\n')
                            else:
                                user_history.write(str(self.order_list[i][j]) + ',')


        with open(pwd,'w') as user_cart:
            for i in range(len(self.current_cart)):
                for j in range(len(self.current_cart[i])):
                    if j==2:
                        user_cart.write(str(self.current_cart[i][j]) + '\n')
                    else:
                        user_cart.write(str(self.current_cart[i][j]) + ',')

    def update_stock(self):         #updates the stock after order has been placed
        self.product_list = []
        with open('products', 'r') as f:
            for lines in f:
                product = lines.rstrip()
                product = product.split(',')
                self.product_list.append(product)
        for order in self.order_list:
            for product in self.product_list:
                if order[0] == product[0]:
                    product[2] = int(product[2])
                    product[2] -= order[2]
        with open('products', 'w+') as f:
            for i in self.product_list:
                f.write(i[0] + ',' + str(i[1]) + ',' + str(i[2]) + '\n')
                f.flush()

    def checkout(self):
        self.manage_cart()
        self.update_stock()

class Bill:
    def __init__(self, order_list):
        self.order_list = order_list
        self.username = User.get_username(customer)

    def calculate_bill(self):
        self.bill = 0
        for order in range(len(self.order_list)):
            self.bill += (int(self.order_list[order][1]) * int(self.order_list[order][2]))

    def display_total_bill(self):
        END = '\033[0m'
        BOLD = '\033[1m'
        CYAN='\033[96m'
        if self.bill>0:
            print(BOLD + CYAN + '*----------------MyShop------------------*')
            print('*--------------Bill Receipt--------------*')
            print('Invoice to:')
            with open('users', 'r') as f:
                user_info = []
                for line in f:
                    lst = line.rstrip()
                    lst = lst.split('/')
                    user_info.append(lst)
            info = []
            for item in user_info:
                if self.username in item:
                    print('CUSTOMER NAME : ', item[0], item[1])
                    print('CUSTOMER ADDRESS : ', item[4],' ',item[5])
            from datetime import datetime
            print()
            from datetime import date
            date = date.today()
            print('DATE:', date.strftime('%B-%d-%Y'))
            time = datetime.now()
            print('TIME:', time.strftime('%H:%M:%S'))
            from tabulate import tabulate
            print(tabulate(self.order_list, headers=['Item Name', 'Item Price', 'Item Quantity'], tablefmt='fancy_grid'))
            print('+-----------+------------+---------------+')
            print('            Payment method: COD')
            print('            SUBTOTAL = ', self.bill, '/-Rs')
            print('            DELIVERY CHARGES = ', '150/-Rs')
            print('            TOTAL = ', self.bill + 150, '/-Rs')
            if self.bill >= 5000:
                discount = 0.05
                newtotal = self.bill - (self.bill * discount)
                print('            DISCOUNT = ', '5%')
                print('            TOTAL =', newtotal + 150, '/-Rs')


        print('\n*******THANKYOU! for visiting us :)*******')
        print('********Hope you will shop again**********')
        print('-----------', 'www.MyShop/pk.com', '------------', sep=' '+END)


END = '\033[0m'
BOLD = '\033[1m'
CYAN='\033[96m'
UNDERLINE='\033[4m'
print(BOLD+CYAN+UNDERLINE+'---------------------\nWELCOME TO MyShop.com\n---------------------'+END+'\n\nENTER YOUR IDENTITY')
identity = input('1.ADMIN\n2.CUSTOMER\nPRESS 1 0R 2 : ')
if identity == '1':
    admin = Admin()
    admin.login()
elif identity == '2':
    customer = Customer()
    print('1.LOGIN\n2.SIGNUP')
    choice = input('PRESS 1 OR 2: ')
    if choice == '1':
        customer.login()
        customer.shopping()
    elif choice == '2':
        customer.signup()
        customer.update_details()
        customer.shopping()

else:
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'
    print(BOLD + RED + 'ERROR\nINVALID SELECTION' + END)