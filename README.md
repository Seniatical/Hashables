# Hashables

Rewriting basic python data types, allowing you to do many new things with them which will make your life easier!
An extension of python's dictionaries that allow you to do things such as: 

put shit here isa

# Installation

Right now, the best way to install is by using git to install it directly:
```bash
pip install -U git+https://github.com/Seniatical/Hashize.git
```

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

# License
This project is licensed under the: **isa license**
** More isa license conditions here **


