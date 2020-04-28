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
            