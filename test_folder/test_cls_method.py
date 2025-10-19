
# Example 1
# Example demonstrating the use of class methods in Python
# A class method is a method that is bound to the class and not the instance of the class.
# It can access class variables and other class methods.

print("Example 1:\n")

class Point:
    # 1. Standard instance constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 2. Instance method (uses self)
    def display(self):
        print(f"Point({self.x}, {self.y})")

    # 3. Class method (uses cls)
    @classmethod
    def from_string(cls, data_string):
        """
        An alternative constructor to create a Point object 
        from a string like '10,20'.
        """
        # cls here refers to the Point class itself
        x_str, y_str = data_string.split(',')
        
        # We use cls(x, y) to call the __init__ constructor 
        # and create a new instance of the class (Point).
        return cls(int(x_str), int(y_str))

# --- Usage ---

# 1. Standard instantiation
p1 = Point(5, 10)

# 2. Class method instantiation (alternative constructor)
# We call it directly on the class (Point.from_string)
p2 = Point.from_string("100,200") 

p1.display() # Output: Point(5, 10)
p2.display() # Output: Point(100, 200)

print("-" * 20 + "\n" + "-" * 20 + "\n" + "Example 2:\n")

# Example 2
# Demonstrating how class methods can be used in inheritance
# to ensure that the correct class type is instantiated.

class Log:
    """Base class for all log entries."""
    def __init__(self, message, timestamp):
        self.message = message
        self.timestamp = timestamp

    def display(self):
        print(f"[{self.timestamp}] LOG: {self.message}")

    @classmethod
    def from_dict(cls, data):
        """
        Alternative constructor that takes a dictionary.
        'cls' ensures the correct type is returned.
        """
        # The crucial part: cls() calls the __init__ of the *actual* class 
        # it was called on (either Log or ErrorLog).
        return cls(data['msg'], data['time'])

class ErrorLog(Log):
    """Specific log for errors."""
    def __init__(self, message, timestamp, level='CRITICAL'):
        # Call the base class constructor
        super().__init__(message, timestamp)
        self.level = level

    def display(self):
        print(f"[{self.timestamp}] {self.level} ERROR: {self.message}")

# --- Usage ---

data = {'msg': 'Disk full', 'time': '2025-10-19 12:00'}

# 1. Calling the class method on the base class
log_entry = Log.from_dict(data) 
print(f"Object Type 1: {type(log_entry)}")
log_entry.display()
# Output: [2025-10-19 12:00] LOG: Disk full

print("-" * 20)

# 2. Calling the EXACT SAME class method on the subclass
error_entry = ErrorLog.from_dict(data) 
print(f"Object Type 2: {type(error_entry)}")
error_entry.display()
# Output: [2025-10-19 12:00] CRITICAL ERROR: Disk full