#پروژه نهم
#سیستم مدیریت فروشگاه
from datetime import datetime

def store(product =None):
    if product is None:
        product= input("enter product name")
    product=product.strip().casefold()
    while not product:
        print("product name cannot be empty")
        product=input("enter product name").strip().casefold()
    while True:
        try:
            cost =float(input("cost in toomans>>> "))
            if cost<=0:
                print("cost must be positive")
                continue
            break
        except ValueError:
            print("please enter a valid number")
    while True:
        try:
            box=int(input("how many boxes ? "))
            if box<0:
                print("count of box cnnot be negative")
                continue
            break
        except ValueError:
            print("please enter a valid integer")
    while True:
        try:
            count_in_box=int(input("count of product in a box >>> "))
            if count_in_box <=0:
                print("count of product in a box  cannot be zero or less")
                continue
            break
        except ValueError:
            print("please enter a valid integer")
    while True:
        try:
            count_in_shelf=int(input("count in shelf"))
            inventory=int(input("Inventory of an item  : "))#موجودی
            if count_in_shelf < 0 or inventory < 0:
                print("inventory cannot be negative")
                continue
            if  inventory < count_in_shelf:
                print("inventory cannot be less than she;f stock")
                continue
            break
        except ValueError:
            print("please enter a valid integer")
            continue
    while True:
        try:
            category=input("enter the category >>>").strip().casefold()
            if not category:
                print("category cannot be empty")
                continue
            break
        except ValueError:
            print("please enter a valid category")
            continue
    information={
        "product": product ,
        "cost":cost,
        "box":box,
        "count_in_box" :count_in_box,
        "count_in_shelf":count_in_shelf,
        "inventory" : inventory ,
        "category":category,
        "sale_times":0,
        "available":count_in_shelf>0
    }
    return information
def buy():
    date=datetime.now()
    name=input("enter name of shopper : ")
    phone=input("enter shopper's phone number : ").strip()
    basket=0
    buyer={
        "date":date,
        "name":name,
        "phone":phone,
        "basket":basket
    }
    return buyer


def sale_history():
    if not salehistory:
        print("no sale history")
        return
    for record in salehistory:
        print("date : ",record["date"])
        print("name : " , record["name"])
        print("phone : ", record["phone"])
        print("basket : ", record["basket"])

    


all_products={}
salehistory=[]
#      0        1       2          3          4      5        6         7
table=["add","delete","search","buy","sale history","restock","shelf","exit"]
while True:
    try:
        i=int(input("enter what the store has : "))
        if i <0:
            print("number cannot be negative")
            continue
        break
    except ValueError:
        print("please enter a valid integer")
for x in range (i):
    shelf=store()
    if shelf["produst"]in all_products:
        print("this product already exists")
    else:
        all_products[shelf["product"]]=shelf
while True:
    employee=input("enter what you need >>>")
    employee=employee.strip().casefold()
    if employee in table:
        if employee == table[0]:
            question1=input("enter what item is being added : ").strip().casefold()
            if question1 in all_products:
                print("this product already exists")
            else:
                shelf=store(question1)
                all_products[shelf["product"]]=shelf
                print("seuccessfully added")
        elif employee==table[1]:
            found=False
            question2=input("what do you want to delete? ").strip().casefold()
            for product in list(all_products):
                if all_products[product]["product"]==question2:
                    del all_products[product]
                    found=True
                    break
            if not found:
                print("not found")
        elif employee==table[2]:
            question3=input("based on what are you searching ? name/ category >>> ").strip().casefold()
            found =False
            if question3=="name":
                question4=input("what product's name : ").strip().casefold()
                if question4 in all_products:
                    print(all_products[question4])
                    found=True
            elif question3=="category":
                question5=input("what category : ").strip().casefold()
                for product in all_products.values():
                    if product["category"]==question5:
                        print(product)
                        found=True
            else:
                print("invalid search option")
                continue
            if not found:
                print("NOT FOUND")
        elif employee==table[3]:
            buying=buy()
            question6=input("what item do you want to buy : ").split(",")
            question7=input("the count of each item").split(",")
            for x in range (len(question6)):
                question6[x]=question6[x].strip().casefold()
            if "" in question6:
                print("product name cannot be empty")
                continue
            for x in range (len(question7)):
                question7[x]=question7[x].strip().lower()
            try:
                for x in range(len(question7)):
                    question7[x] = int(question7[x])
            except ValueError:
                print("please enter valid numbers")
                continue
            if len(question6) != len(question7):
                print("the number of products and quantities must match")
                continue

            if any(x <= 0 for x in question7):
                print("quantities must be positive")
                continue
            
            totalprice=[]
            sold_anything=False

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
                            all_products[item]["inventory"]-=count
                            all_products[item]["available"] = (all_products[item]["count_in_shelf"] > 0)
                            totalprice.append(all_products[item]["cost"]*count)
                            total=all_products[item]["cost"]*count
                            buying["basket"]+=total
                            all_products[item]["sale_times"]+=1
                            sold_anything=True
                            
                        else: 
                            if countinshelf == 0:
                                print("this product is out of stock")
                                continue
                            question8=input(f"only {countinshelf} is available . do you want it? ")
                            if question8.strip().casefold() in ["yes","y","yeah","ok"]:
                                all_products[item]["count_in_shelf"]-=countinshelf
                                all_products[item]["inventory"]-=countinshelf
                                all_products[item]["available"] = (all_products[item]["count_in_shelf"] > 0)
                                total=all_products[item]["cost"]*countinshelf
                                buying["basket"]+=total
                                totalprice.append(all_products[item]["cost"]*countinshelf)
                                all_products[item]["sale_times"]+=1
                                sold_anything=True
                            else:
                                pass
                    else:
                        pass
                if not found:
                    print(f"{product} not found")
            finalprice=sum(totalprice)
            print(f"final price = {finalprice}")
            if sold_anything:
                salehistory.append(buying)
            else:
                print("no product were sild")

        elif employee==table[4]:
            history=sale_history()
            
        elif employee==table[5]:
            question9=input("which existing product do you want to add").split(",")
            try:
                amount=int(input("how many boxes? >> "))
                if amount <=0:
                    print("amount must be positive")
                    continue
            except ValueError:
                print("please enter a valid integer")
                continue 
            for product in question9:
                product=product.strip().casefold()
                if not product:
                    print("product cannot be emoty")
                    continue
                if product not in all_products:    
                    print("product name cannot found")
                    continue
                    
                item=all_products[product]
                added_item=amount*item["count_in_box"]
                item["box"]+=amount
                item["inventory"]+=added_item
                print(f"{product}restocked successfully")
        elif employee==table[6]:
            product=input("which product : ").strip().casefold()
            if product not in all_products:
                print("product not found")
                continue
            item=all_products[product]
            try:
                amount=int(input("how many items put in shelf? : "))
                if amount <=0:
                    print("amount must be positive")
                    continue 
                if amount > item["inventory"]-item["count_in_shelf"]:
                    print("not enough item to storage")
                    continue
            except ValueError:
                print("please enter a valid integer")
                continue
            item["count_in_shelf"]+=amount
            item["available"]=item["count_in_shelf"]>0
            print("items moved to shelf successfully")

            
        elif employee ==table[7]:
            print("GOOD BYE...EXITING >")
            break
    else:
        print("invalid command")
