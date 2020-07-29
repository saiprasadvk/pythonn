Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, a
nd if the salary is missing in function call it should show it as 9000.

Ans::
def showEmployee(name, salary=9000):
    print("Employee", name, "salary is:", salary)

print(showEmployee("ben",9000))
print(showEmployee("ben"))

O/P::
Employee ben salary is: 9000
Employee ben salary is: 9000

