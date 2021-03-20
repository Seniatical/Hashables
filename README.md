# Hashables

Rewriting basic python data types, allowing you to do many new things with them which will make your life easier!
An extension of python's dictionaries that allow you to do things such as: 

> Accessing values with a index
> Adding things from keys

# Examples

```py
>>> new
<Hashable Dict [{'name': 'John', 'gender': 'Male'}]>
>>> new + {'age': 20}
{'name': 'John', 'gender': 'Male', 'age': 20}
>>> new['age']
20
>>> new[1:]
{'gender': 'Male', 'age': 20}
>>> new[1]
'Male'
>>> new.fromkeys(['job', 'salary'], values=['Employee', 25000])
>>> new
<Hashable Dict [{'name': 'John', 'gender': 'Male', 'age': 20, 'job': 'Employee', 'salary': 25000}]>
>>> 
```
