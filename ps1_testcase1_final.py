# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# PartA: House Hunting Program - calculate how many months 
# to save up for initial down payment
############################################
# cost of dream home -> total_cost
# Initial Down payment needed to buy house -> portion_down_payment
# Assume portion_down_payment = 0.25*total_cost
# current savings in bank = 0
# annual salary -> annual_salary
# portion saved = portion_saved*10%*annual_salary
# percentage salary tobe saved -> percent_saved

#############################################

# Enter inputs

#annual_salary = float(input("enter annual salary:  "))
#portion_saved = float(input("portion salary to be saved:   "))
#total_cost = float(input("cost of dream home:   "))

annual_salary = 120000
portion_saved = 0.1
total_cost = 1000000

#checkpoint1
print (annual_salary,",  ", portion_saved, ",  ",total_cost)
print ("/n")
# calculat value of no_months
# no_months is the number of months required to save up for required deposit

portion_down_payment = total_cost*0.25
current_savings = 0
r = 0.04

print("target deposit required:  ", portion_down_payment)

for no_months in range (1,1000):
    current_savings = current_savings + (annual_salary*portion_saved)/12
    current_savings = (1+r/12)*current_savings # add interest
    no_months = no_months+1
    print(current_savings, ",   ", no_months)
    if current_savings >=portion_down_payment:
        break
    
print ("number of months :  ", no_months)
    

    
    
    
    


  