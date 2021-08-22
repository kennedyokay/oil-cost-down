#This is the oil cost-down program, prototype(version.1). 
"""
If l >= 25liter, run this program.
final cost = (current cost - 2) * current liter -25
"""
# Current_cost_92 = float(input("Please enter current 92 cost:"))
# Current_cost_95 = float(input("Please enter current 95 cost:"))
# Current_cost_98 = float(input("Please enter current 98 cost:"))
Current_cost_92 = 28
Current_cost_95 = 29.4
Current_cost_98 = 31.5
Current_cost_list = [Current_cost_92, Current_cost_95, Current_cost_98]

for Current_cost in Current_cost_list:
    for Current_liter in range(25, 51, 5):
        while Current_cost == Current_cost_92:
            Final_cost_92 = (Current_cost - 2) * Current_liter - 25
            print("oil=92, liter={}, cost={}".format(Current_liter, Final_cost_92))
            break
        while Current_cost == Current_cost_95:
            Final_cost_95 = (Current_cost - 2) * Current_liter - 25
            print("oil=95, liter={}, cost={}".format(Current_liter, Final_cost_95))
            break
        while Current_cost == Current_cost_98:
            Final_cost_98 = (Current_cost - 2) * Current_liter - 25
            print("oil=98, liter={}, cost={}".format(Current_liter, Final_cost_98))
            break