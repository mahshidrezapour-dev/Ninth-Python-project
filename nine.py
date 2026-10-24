#پروژه نهم
#سیستم مدیریت فروشگاه
from datetime import datetime

def store(product =None):
    if product is None:
        product= input("enter product name")
        cost =float(input("cost in toomans>>> "))
        box=int(input("how many boxes ? "))
        count_in_box=int(input("count of product in a box >>> "))
        count_in_box_shelf=int(input("count in shelf"))
        inventory=int(input("Inventory of an item  : "))#موجودی
        category=input("enter the category >>>")
        sale_times=0
        available=True
        information={
            "product": product ,
            "cost":cost,
            "box":box,
            "count_in_box" :count_in_box,
            "count_in_shelf":count_in_box_shelf,
            "inventory" : inventory ,
            "category":category,
            "sale_times":sale_times,
            "available":available
        }
        return information
def buy():
    date=datetime.now()
    name=input("enter name of shopper : ")
    phone=int(input("enter shopper's phone number : "))
    basket=0
    buyer={
        "date":date,
        "name":name,
        "phone":phone,
        "basket":basket
    }
    return buyer


def sale_history():
    for record in salehistory:
        print("date : ",record["date"])
        print("name : " , record["name"])
        print("phone : ", record["phone"])
        print("basket : ", record["basket"])

    


all_products={}
salehistory=[]
#      0        1       2          3          4      5        6
table=["add","delete","search","buy","sale history","restock","exit"]
i=int(input("enter what the store has : "))
for x in range (i):
    shelf=store()
    all_products[shelf["product"]]=shelf
while True:
    employee=input("enter what you need >>>")
    employee=employee.lower()
    if employee in table:
        if employee == table[0]:
            question1=input("enter what item is being added : ")
            shelf=store(question1)
            all_products[shelf["product"]]=shelf
            print("seuccessfully added")
            available=True
        elif employee==table[1]:
            found=False
            question2=input("what do you want to delete? ")
            for product in list(all_products):
                if all_products[product]["product"]==question2:
                    del all_products[product]
                    found=True
                    break
            if not found:
                print("not found")
        elif employee==table[2]:
            question3=input("based on what are you searching ? name/ category >>> ")
            found =False
            if question3.lower()=="name":
                question4=input("what product's name : ")
                for product in all_products:
                    if all_products[product]["product"]==question4:
                        print(all_products[product])
                        found=True
            if not found:
                print("not found")
            elif question3.lower()=="category":
                question5=input("what category : ")
                for product in all_products:
                    if all_products[product]["category"]==question5:
                        print(all_products[product])
                        found=True
                if not found:
                    print("NOT FOUND")
            else:
                print("not found")
        elif employee==table[3]:
            buying=buy()
            question6=input("what item do you want to buy : ").split(",")
            
            question7=input("the count of each item").split(",")
             
            question7=[int(x) for x in question7]
            totalprice=[]
            

            for product , count in zip(question6 , question7):
                found=False
                for item in all_products:
                    if all_products[item]["product"]==product:
                        found=True
                        print("FOUND...")
                        countinshelf=all_products[item]["count_in_shelf"]
                        if all_products[item]["count_in_shelf"]>=count:
                            print("available")
                            all_products[item]["count_in_shelf"]-=count
                            
                            totalprice.append(all_products[item]["cost"]*count)
                            total=all_products[item]["cost"]*count
                            buying["basket"]+=total
                            
                        else:    
                            question8=input(f"only {countinshelf} is available . do you want it? ")
                            if question8.lower() in ["yes","y","yeah","ok"]:
                                all_products[item]["count_in_shelf"]-=countinshelf
                                total=all_products[item]["cost"]*countinshelf
                                buying["basket"]+=total
                                
                                totalprice.append(all_products[item]["cost"]*countinshelf)
                            else:
                                pass
                    else:
                        pass
                if not found:
                    print(f"{product} not found")
            finalprice=sum(totalprice)
            print(f"final price = {finalprice}")
            salehistory.append(buying)

        elif employee==table[4]:
            history=sale_history()
            
        elif employee==table[5]:
            question9=input("which existing product do you want to add").split(",")
            amount=int(input("how many boxes? >> "))
            found=False    
            for product in question9:
                for item in all_products:
                    if all_products[item]["product"]==product:
                        all_products[item]["inventory"]+=amount
                        found=True
                        print("restocked successfully")
                        
            if not found:
                print(f"{product} is new... NOT ELIGIBLE")
                    
        elif employee==table[6]:
            print("GOOD BYE...EXITING >")
            break

                                

                            

                            

                                    
                    
                            
                    
                     



                        
                        






                


                
            






