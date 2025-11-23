# Expanse Tracker 

expanses = []
print("Welcome to Expanse Tracker : Your Personal Finance APP.")
while True:
  print("\n=========MENU=========")
  print("1. Add Expanse")
  print("2. View All Expanse")
  print("3. View Total Spending")
  print("4. Exit")
  print("=====================")
  choice = int(input("Enter Your Choice: "))
  if choice==1:
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    description = input("Enter short description: ")
    amount = float(input("Enter amount (₹):"))
    expanse = {
      "date": date, 
      "category": category, 
      "description": description, 
      "amount": amount
      }
    expanses.append(expanse)
    print("\n✅ Expense added successfully!")
  elif choice==2:
    if len(expanses)==0:
      print("\n⚠️  No expenses recorded yet.")  
    else:
      print("\n--- All Expenses ---")
      count = 1
      for e in expanses:
          print(f"{count}. {e["date"]}  |  {e["category"]}  |  {e["description"]}  |  {e["amount"]}")
          count+=1
  elif choice==3: 
    total = 0
    for e in expanses:
      total = total+ e["amount"]        
    print(f"\n💰 Total Spending = ₹{total}") 
  elif choice==4:  
    print("\n👋 Thanks for using Expense Tracker! Bye!")
    break
  else:
    print("\n❌ Invalid choice. Please try again.")