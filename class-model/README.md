# Employee Class Model

Please find my full solution [here](./employees.py). A complete description of my logic and organization is below.

### Employee

The `Employee` class represents a typical full time employee.

Each `Employee` has the following attributes and methods:
- `get_name` - returns the employee’s name in the format “Last Name, First Name"
- `get_pay_rate` - returns hourly pay rate (dollars / hour)
- `get_yearly_vacation` - returns the amount of yearly vacation for the employee

### IndependentWorker

The `IndependentWorker` class outlines the shared differences Contractors and Temporaries have with Employees.

The key differences are:
- They don't have any yearly vacation time
- The `get_name` method adds a label tag after "Last, First"
- They have a `get_agency` method, which returns the name of the agency that represents the worker

This class calls the `Employee` contructor with `0` as the `yearly_vacation`. It also overrides the `get_name` method to include the appropriate label tag in the return string.

### Contractor & Temporary

The `Contractor` and `Temporary` classes each extend `IndependentWorker`. They simply call the constructor of `IndependentWorker` with the appropriate label passed in as a parameter.

## Example

These class instances and method calls:
```
a = Employee("Aaron", "Adams", 40, 14)
b = Contractor("Bill", "Bowen", 30, "Company B")
c = Temporary("Charlie", "Clown", 25, "Company C")

print "-" * 20
print a.get_name()
print a.get_pay_rate()
print a.get_yearly_vacation()

print "-" * 20
print b.get_name()
print b.get_pay_rate()
print b.get_yearly_vacation()
print b.get_agency()

print "-" * 20
print c.get_name()
print c.get_pay_rate()
print c.get_yearly_vacation()
print c.get_agency()

print "-" * 20
```

would print this to output:
```
--------------------
Adams, Aaron
40
14
--------------------
Bowen, Bill [ C ]
30
0
Company B
--------------------
Clown, Charlie [ T ]
25
0
Company C
--------------------
```