# Code Review

### The Code I've Been Given To Review

```py
def CompareSwapSizeInMb(self, swap1, swap2):
    if self.OSType == "Linux":
        if swap1 < swap2:
            return False
    return True
```

### My Review

#### Firstly
_What does this function do exactly?_

I see that we are comparing two swap sizes and returning a boolean that states if one swap is bigger than the other. However, if I were to only see the name of the function `CompareSwapSizeInMb()`, I would anticipate that the funcion would either return nothing, or maybe some sort of readable report based on the two swap sizes.

I suggest to **rename the function** to make it clear that a boolean will be returned.

My suggestion is something like `swap_is_smaller()`, but further clarification of what the returned boolean will be used for may alter my suggestion.

Also, note that my suggested name follows expected python naming conventions of **lowercase words separated by underscores**.

#### Condense The Logic

The logic of this function is clearly laid out, but it could easily be condensed.

Any time there is a `return True` or `return False` statement, it is important to check if that can be made simpler with some refactoring.

In this case, we can put everything into a singe `or` statement.

```py
return self.OSType != "Linux" or swap1 >= swap2
```
First, it automatically returns `True` if the OSType is not `"Linux"`, representing the first and last lines of the original.

If the type is indeed `"Linux"`, it checks now if `swap1` is greater than or equal to `swap2`. Since the original comparison had a return value of `False` if the comparison was true, I inverted the original logic to return `True` if the opposite condition is met, allowing me to condense it all into one line.

### My Final Adjustments

```py
def swap_is_smaller(self, swap1, swap2):
    return self.OSType != "Linux" or swap1 >= swap2
```