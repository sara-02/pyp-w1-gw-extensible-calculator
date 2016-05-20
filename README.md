# [pyp-w1] Extensible calculator

Today you will be coding to build a calculator. Even though that sounds simple,
this won't be a regular calculator. You must implement it in a way that users
of the calculator are able to "extend" its functionally by adding as many
custom operations as they want. For that to be doable, we will make usage of
the high-order functions concept we've covered in class.

Operations will be defined as regular functions. There's just one important thing
you must have in mind. All operations need to keep the same interface, meaning
they all must be executable sending the same parameters. To have extra
flexibility, we will assume that all operations receives a variable number
or arguments (`*args`), like the following code:

```python
def add(*args):
    """
    Returns a number representing the sum of all given arguments.
    """
    # your implementation here
    pass
```

In many cases, operations are simple enough to be implemented just using a `lambda`:

```python
subtract = lambda *args: pass  # your code here
```

Operations are independent entities. You should be able to use them outside
any other code, even outside of the calculator you are supposed to build.
To use an operator follow this logic:

```python
>>> subtract(100, 20, 10, 20)
50
>>> subtract(100, 20)  # must accept variable number of arguments
80
```

If you reached this point, you should now be ready to start coding your calculator.
To create a new calculator you must follow this interface:

```python
>>> calc = create_new_calculator(operations=(add, subtract, divide, multiply))
{
    'operations': {
        'add': add,
        'subtract': subtract,
        ...
    },
    'history': [
        ('add', (1, 2, 3, 4), '2016-05-18 12:00:00'),
        ('multiply', (1, 2, 3, 4), '2016-05-18 12:10:00'),
        ...
    ]
}
```

As it's shown in the sample code, a `calculator` is just a data structure
(dict in this case) holding the collection of operations the calculator supports
and keeping track of the operation execution history.

Once you have the calculator created, you can start using it:

```python
>>> perform_operation(calc, 'add', params=(1, 2, 3, 4))
10
```

You must consider possible errors that might occur while using the calculator:

```python
>>> perform_operation(calc, 'something-weird', params=(1, 2, 3, 4))
InvalidOperation: "something-weird" operation not supported.
>>> perform_operation(calc, 'something-weird', params=False)
InvalidParams: Given params are invalid.
>>> perform_operation(calc, 'something-weird')  # params not sent
InvalidParams: Given params are invalid.
```

As the title of this group work says, the calculator must be extensible. That
means, after a calculator is created, new operations can be dynamically added to it.
To do that, you must implement the following method:

```python
>>> square_root = lambda ...
>>> add_new_operation(calc, operation=square_root)
```

>>> get_operations(calc)
['add', 'subtract', 'divide', 'multiply']

>>> get_history(calc)
>>> reset_history(calc)

>>> perform_operation(calc, 'subtract', params=(10, 2, 3, 4))
1
>>> repeat_last_operation(calc)
1

# extra points: Implement a `plot` operation
>>> plot = lambda ...
>>> add_new_operation(calc, operation=plot)

>>> perform_operation(calc, 'plot', params=('-x**2', -2, 2))
*hint: Investigate `sympy` library*

-0 |             ... ...
   |           ..       ..
   |          /           \
   |         /             \
   |        /               \
   |       /                 \
   |      .                   .
-2 | ------------------------------
   |     .                     .
   |    .                       .
   |
   |   .                         .
   |
   |  .                           .
-4 | /
     -2         0              2
