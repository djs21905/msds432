#Greedy Algorithm - Approximation 

#24 hours to fill
guards = [1,2,3,4,5,6]
#Each guard can hold a maximum of 8 hours because we want to minimize 
#Any overtime which is considered > 8 hours

total_cost = 50000
number_of_guards = 0 
hours_each = 0
for guard in guards:
    hours_per_guard = 24/guard
    guard_wage = 0 
    print(hours_per_guard)
    print("# of guards " + str(guard))
    if hours_per_guard <= 8:
        guard_wage = (15 * hours_per_guard) * guard
    elif hours_per_guard > 8: 
        overtime = (hours_per_guard - 8) * (20)
        guard_wage = (overtime + (15 * 8)) * guard
    print("new cost "+ str(guard_wage) + " Vs old cost " + str(total_cost))
    if guard_wage < total_cost:
        number_of_guards = guard
        total_cost = guard_wage 
        hours_each = hours_per_guard
        print("The Number of Guards " + str(number_of_guards))
        print("Total cost $" + str(total_cost))
        print("Hours per guard " + str(hours_each))
        print()
        print()
        print()

print()
print()
print()
print("Optimum")
print(number_of_guards)
print(total_cost)
print(hours_each)

"""
Explain your algorithm in detail.  How is it greedy?
This is a greedy algorithm because it does not perform an exhaustive search to find the global optimum.
This would be very computationally expensive.  Instead we approximate the global optimum using a greedy algorithm.  
This algorithm iterates through different scenarios of guards i.e 1 through 6.   For each scenario is determins the cost
and if the cost is less than the previous cost we assign it as the optimal choice.  

What is the complexity of your solution?
The complexity of the solution above is O(n) because there is one for loop by which each item (n) in a list is iterated over.

Did the greedy algorithm provide the best solution or could there be an alternative/better solution to your problem?  Why or why not?
In this circumstance the greedy algorithm did provide the best solution.   However there are also several alternatives
that would lead to the same total cost.  For example 6 guards each working 4 hours each would result in the same
global optimum.

If the scenario had different values for the inputs would your algorithm still be successful?  Eg. more than 24 hours, higher overtime, shorter shifts, or values that don't factor so nicely.  Why or why not?  What things would change the optimal output?
If you were not constrained to a greedy algorithm, what approaches would you take to solve the problem?  

If the scenario was different and there were more hours being considered i.e 30 hours the answer would change. 
Also if you added another constraint on the maximum or minimum number of hours each guard must work the core of the problem
would change and the greedy algorithm would no longer work. 

If I was not constrained to a greedy algorithm you could iterate over every potential combination or guard # and hours for each guard.
For example you could consider 2 guards each working 12 hours or 2 guards one working 13 and one working 11 etc... 

"""