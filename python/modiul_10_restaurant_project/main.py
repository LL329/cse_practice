from menu import Pizza, Burger,  Drinks, Menu
from restaurant import Restaurant
from user import Chef, Customer, Server, Employee, Manager
from order import Order
def main():
   menu = Menu()
   Pizza_1 = Pizza('shutki',600,'large', ['shutki','onion'])
   menu.add_menu_item('pizza',Pizza_1)
   Pizza_2 = Pizza('Alu', 400,'large', ['potato', 'onion', 'oil'])
   menu.add_menu_item('pizza', Pizza_2)
   Pizza_3 = Pizza('Dal', 500, 'small', ['dal', 'oil','meat'])
   menu.add_menu_item('pizza', Pizza_3)

    # add burger to the menu
   burger_1 = Burger('nana burger', 1000, 'chili', ['bread', 'chili'])
   menu.add_menu_item('burger', burger_1)
   burger_2 = Burger('Nani burger', 800, 'red chilli', ['bread', 'haddi'])
   menu.add_menu_item('burger', burger_2)
   burger_3 =Burger ('DAda burger', 1200, 'onion', ['break', 'gorur vuri'])
   menu.add_menu_item('burger',burger_3)


   # add drinks to the menu
   coke = Drinks('coke', 50, True)
   menu.add_menu_item('drinks', coke)
   speeds = Drinks('speeds', 30, True)
   menu.add_menu_item('drinks', speeds)
   cane = Drinks('cane', 70, True)
   menu.add_menu_item('drinks', cane)

   # show Menu
   menu.show_menu()

   restaurant = Restaurant('Ali baba Restaurant', 2000, menu)

   # add employees
   manager = Manager('Kalachan manager', 189129, 'kala@gmail.com', 'kalipur', 1500, 'jan 1 2020', 'core')
   restaurant.add_employee('manager', manager)
   chef = Chef('Liton chef', 689988, 'liton@gmailcom', 'dhanbandhi', 3500, 'Feb 28 2020', 'Chef', 'everything')
   restaurant.add_employee('chef', chef)
   server = Server('Choto server', 688888, 'server@gmail.com', 'restaurant', 200, 'March 1 2020', 'server')
   restaurant.add_employee('server', server)
   
   #show employee
   restaurant.show_employees()

   # customer 1 placing an order
   customer_1 = Customer('Tusi', 8151650, 'tusi@gmail.com', 'sirajganj', 5000)
   order_1 = Order(customer_1,[Pizza_3, burger_1, speeds, cane])
   customer_1.pay_for_order(order_1)
   restaurant.add_order(order_1)


   # customer 2 placing an order
   customer_2 = Customer('Mh shanto', 8151650, 'sausi@gmail.com', 'sirajganj', 5000)
   order_2 = Order(customer_2,[Pizza_3,Pizza_2, Pizza_3, cane])
   customer_2.pay_for_order(order_2)
   restaurant.add_order(order_2)


   # customer one paying for order
   restaurant.receive_payment(order_1, 20500, customer_1)
   # customer two paying for order
   restaurant.receive_payment(order_2, 20000, customer_2)


   print('revenue and balance after first customer ', restaurant.revenue, restaurant.balance)
    
   #pay rent
   restaurant.pay_expense(restaurant.rent, 'Rent')
   print('after rent', restaurant.revenue, restaurant.balance, restaurant.expense)

   #pay salary
   restaurant.pay_salary(chef)
   print('after salary', restaurant.revenue, restaurant.balance, restaurant.expense)


#call the main method

# main()
if __name__ == '__main__':
    main()