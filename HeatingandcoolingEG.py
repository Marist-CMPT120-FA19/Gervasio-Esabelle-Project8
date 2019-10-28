#Esabelle Gervasio
#Heating and cooling days
#esabelle.gervasio1@marist.edu

def temp():
        avg= input("Enter the avg temp per day with a space between days: ")
        avg=avg.split(" ")
        cool=0
        heat=0

        for i in avg:
            if float(i)> 80 or float(i)<60:
                if float(i)> 80:
                    cool+=float(i)-80
                else:
                    heat+=60-float(i)

        print("there are", cool, "cooling degrees and", heat, "heating degrees")
temp()
