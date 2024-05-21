#Submitted by: Ryan Angelo Dela Cruz

import math

#car rental dictionary for size, capacity, and cost
rental_cost = { "S": {"seat":5, "cost":5000.0}, "M": {"seat":10, "cost":8000.0}, "L": {"seat":15, "cost":12000.0}}


def calculate(num_seat):
	#create a temporary list
	rec = []

	for keys in rental_cost.keys():
		#calculate no. of cars needed to accomodate required seats
		#returns round up value
		total_car = math.ceil(num_seat / rental_cost[keys]["seat"])

		#calculate total cost by total car times rental cost
		total_cost = total_car * rental_cost[keys]["cost"] 

		#append the total cost together with the size of the car
		rec.append([keys, total_car, total_cost])

	
	#check if temporary list has data
	if len(rec) > 0:

		#sort list by cost to identify the cheapest	
		cheapest = sorted(rec, key=lambda x: x[2], reverse=True)
		
		#initialize most optimized car size and cost
		text = "{} x {}".format(cheapest[-1][0], cheapest[-1][1])
		total = "Total = PHP {}".format(cheapest[-1][2])

		#clear temporary list
		rec.clear()
		return(str(text) + "\n" + str(total))
	else:
		#if no data
		return("Error: Please try again later.")

			
print("Car Rental Problem\nPress 0 to exit\nPress 1 to CALCULATE Rental Cost\nPress 2 to UPDATE Seat\nPress 3 to UPDATE Cost\nPress 4 to DISPLAY Rental Costs")
while True:
    try: 
        option = int(input("Choose option:"))
        
        if option == 0:
            print("Thank you! Please come again.")
            break
            
        elif option == 1:
            try:	
                num_seat = int(input("Please input number (seat):"))
                
                if num_seat <= 0:
                    print("Please enter valid number")
                else:
                    cal = calculate(num_seat)
                    print(cal)
        
            except (ValueError):
                print("Please enter valid number")
                
        elif option == 2:
            key = str(input("Enter size: ")).upper()
            if key in rental_cost.keys():
                try: 
                    seat = int(input("Enter updated seat: "))
                    rental_cost[key]["seat"] = seat
                    print("Seat for {} UPDATED successfully".format(key))
                    print(rental_cost)
                except (ValueError):
                    print("Please enter valid seat capacity")
            else:
                print("Please enter valid size")

        
        elif option == 3:
            key = str(input("Enter size: ")).upper()
            if key in rental_cost.keys():
                try:
                    cost = float(input("Enter updated cost: "))
                    rental_cost[key]["cost"] = cost
                    print("Cost for {} UPDATED successfully".format(key))
                    print(rental_cost)
                except (ValueError):
                    print("Please enter valid cost")
            else:
                print("Please enter valid size")
                
        elif option == 4:
            print("Rental Costs as follow:")
            print(rental_cost)
          
        else:
            print("Please enter valid option.")
       
    except(ValueError):
        print("Please enter valid option.")
    
    
