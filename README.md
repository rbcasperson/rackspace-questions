# Rackspace Questions

## Ryan Casperson - @rbcasperson

### My Answers

- [Class Model Solution](https://github.com/rbcasperson/rackspace-questions/tree/master/class-model)

- [Code Review](https://github.com/rbcasperson/rackspace-questions/tree/master/code-review)

### The Questions

#### 1. Class Model

Using Python, please define a class model to implement the following specification:  
 
A company has a staffing model which includes Employees, Contractors, and Temporaries.  We want an object model which implements this structure.  The expected behavior for the classes is documented below:

```
Employee:
Constructor: accepts First Name, Last Name, Pay Rate, Yearly Vacation (num days)
Public Methods: get_name - returns the employee’s name in the format “Last Name, First Name"
                get_pay_rate - returns hourly pay rate (dollars / hour)
                get_yearly_vacation - returns the amount of yearly vacation for the employee
 
Contractor:
Constructor: accepts First Name, Last Name, Pay Rate, Agency Name (Note: By policy, all contractors have 0 days of vacation)
Public Methods: get_name - returns the contractor's name in the format “Last Name, First Name [ C ]"
                get_pay_rate - returns hourly pay rate (dollars / hour)
                get_yearly_vacation - returns the amount of yearly vacation for the contractor
                get_agency - returns the name of the contracting agency that represents the contractor
 
 
Temporary:
Constructor: accepts First Name, Last Name, Pay Rate, Agency Name (Note: By policy, all temporaries have 0 days of vacation)
Public Methods: get_name - returns the contractor's name in the format “Last Name, First Name [ T ]"
                get_pay_rate - returns hourly pay rate (dollars / hour)
                get_yearly_vacation - returns the amount of yearly vacation for the temporary
                get_agency - returns the name of the temp agency that represents the temporary
```

#### 2. Code Review

If you were a code reviewer, what feedback would you provide on the below function.  Provide as much feedback as you can:
 
```py
def CompareSwapSizeInMb(self, swap1, swap2):
    if self.OSType == "Linux":
        if swap1 < swap2:
            return False
    return True
```