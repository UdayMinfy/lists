### Easy Questions

###  1. **Function Basics**

def calculate_average(list1):
    if len(list1)==0:
        return 0 
    else:
        return sum(list1)/len(list1) 
print(calculate_average([5, 10, 15, 20]))  # Should return 12.5
print(calculate_average([]))  # Should return 0


### 2. Default Parameters

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Example usage:
print(greet_user("Alice"))         # Should return "Hello, Alice!"
print(greet_user("Bob", "Hi"))     # Should return "Hi, Bob!"

### Medium Questions

###  1. **Variable Arguments**
def calculate_total(*costs, discount=0):
    total = sum(costs)
    if discount:
        total -= (total * discount / 100)
    return total

# Example usage:
print(calculate_total(10, 20, 30))  # Should return 60
print(calculate_total(10, 20, 30, discount=10))  # Should return 54.0


### 2. Closures

def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# Example usage:
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Should return 10
print(triple(5))  # Should return 15


### Hard Questions 

###  1. Recursion

def power(x, n):
    if n == 0:
        return 1
    
    if n < 0:
        return 1 / power(x, -n)
    
    half = power(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

print(power(2, 10))  # Should return 1024
print(power(3, 4))   # Should return 81 

### 2. Higher Order Functions 

def compose(*funcs):
    def composed(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return composed

# Example usage:
def add_one(x): return x + 1
def double(x): return x * 2
def square(x): return x ** 2

f = compose(square, double, add_one)
print(f(3))  # Should print 64

