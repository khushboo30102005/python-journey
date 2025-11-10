# Python Code Execution Process

### The python execution process involves several key steps:

- ### **Source code Creation:**

A Programmer writes python code in a text editor and save it with `.py` extension. This is the human-readable set of instructions.

- ### **Compilation to ByteCode:**

When a python script is executed, the python interpreter first compiles source code into an intermediate formate called Bytecode. This bytecode is platform-independent and is stored in `.pyc` files.This step also includes lexical analysis and parsing, where the code is broken down into tokens and checked for syntax errors.

- ### **Execution by Python Virtual Machine (PVM):**

The bytecode is then fed to the PVM, Which is a component of the python interpreter. The PVM reads the Bytecode instruction one by one and translate them into machine executable instruction that the computer' CPU can understand and execute. This Process is known as interpretation.

- ### **Machine Code Execution:**
  The CPU then executes the machine code instruction Produces by the PVM, performing the operations specified in the original Python code.
- ### **Output & Termination:**
  The Program produces the intended output, and the execution process terminates when all instructions are executed and unhandled exception occurs.

# PYTHON VARIABLES:

#### in Python a variable is a symbolic name that refers to a value stored in computer's memory. It is acts as container for data, allowing you to store, access and manipulate information within your program.

### Key characteristics of Python Variables:

- ### **Dynamic typing:**
  Python is a dynamically typed language, meaning you do not need to explicitly declare the data type of a variable. The interpreter automatically infers the type based on the value assigned.

```python
    my_number = 10  # Python infers 'my_number' is an integer
    my_string = "Hello"  # Python infers 'my_string' is a string
```

- ### Assignment:
  Variables are created and assigned values using the assignment operator `=`

```python
variable_name = value
```

- ### Mutability:
  Python variable can be reassigned to different values, and even to value to different data type.

```python
x = 5
print(x)   # output => 5
x = 'five'
print(x)   # output => five
```

- ### Naming Conventions:
  It is common practice to use lowercase with underscores (snake_case) for variable names (e.g., my_variable_name)
- ### Scope:
  Variables have a defined scope, determining where they can be accessed in your code (e.g., local variables within functions, global variables accessible throughout the program).
- ### Deletion:
  Variables can be deleted from memory using the del keyword.

```python
del x
print(x)  # output => raise a nameError

```
