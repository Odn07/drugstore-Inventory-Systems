<<<<<<< HEAD
import mod1 
=======
import mod1
>>>>>>> 4e1d81f15443ea57de4675d1380ba0398831e2f3

print("\n|INVENTRY MANAGEMENT SYSTEM\n")  
#Display sales record, create sales record, create expired product record, display sales summary
while True:
    try:
        count = int(input("\nPress 1 to sell, 2 to use menu tab, and zero to logout: "))
        print("\n")
    except BaseException as err:
        pass
    if count == 1:
        mod1.Sales.sell_product()
        #delete temporary file after printing the current sales details
<<<<<<< HEAD
        mod1.delete_file()
    elif count == 2:
        print("|MENU =>", "|Pcode", "|Stock", "|Sales")
        # menu
        while True:
            try:
                menu = input("|MENU =>: ").title().strip()
=======
        delete_file()
    elif count == 2:
        print("\n|MENU =>", "|Pcode", "|Stock", "|Sales")
        # menu
        while True:
            try:
                menu = input("\n|MENU =>: ").title().strip()
>>>>>>> 4e1d81f15443ea57de4675d1380ba0398831e2f3
                if menu == "Admin":
                    break        
            except BaseException as err:
                print(err)
            menu_list = ["Pcode", "Stock", "Sales"]
            if menu in menu_list:
<<<<<<< HEAD
                match menu: 
                    case "Pcode":
                        mod1.Stock.codeGenerator(cls)   
=======
                match menu:
                    case "Pcode":
                        mod1.Stock.codeGenerator()    
>>>>>>> 4e1d81f15443ea57de4675d1380ba0398831e2f3
                    case "Stock":       
                        #CREATE STOCK FILE
                        mod1.Stock.createStockFile()
                    case "Sales":
                        #DISPLAY A SUMMARY OF SALES DATA
                        mod1.Sales.display_sales_summary()
                    case _:
                        pass

    elif count == 0:
        break   

