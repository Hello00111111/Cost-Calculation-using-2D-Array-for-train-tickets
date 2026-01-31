
#the program uses 2D Array to calculate the cost of train ticket(s)

stations = {"City Hall": 0,
            "Central Station": 1,
            "Stadium": 2, 
             "Park": 3}
cost = []
fare_array = [[0, 1, 2, 3], 
              [1 ,0, 1, 2], 
              [2 ,1 ,0, 1], 
              [3, 2, 1, 0]] 

while True:
 departure = input("Departure Station: ")
 destination = input("Destination: ")
 price = fare_array[stations[departure]][stations[destination]]
 cost.append(price)
 continue_or_not = input("Press c to continue. Press s to proceed to the payment.")
 if continue_or_not == "s":
  break
 elif continue_or_not == "c":
  continue
print("Your ticket(s) cost is $",sum(cost))

        
        






