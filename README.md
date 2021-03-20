# Hashize

Rewriting basic python data types, allowing you to do many new things with them which will make your life easier!
An extension of python's data types which makes more flexible and nicer to work with;

# Installation

Right now, the best way to install is by using git to install it directly:
```bash
pip install -U git+https://github.com/Seniatical/Hashize.git
```

# Examples

```py
>>> from hashize import Dict
>>> new = Dict({'name': 'John', 'age': 20})
>>> new + {'job': 'Builder'}
{'name': 'John', 'age': 20, 'job': 'Builder'}
>>> new['job'] = 'Employer'
>>> new
HashizeDict([{'name': 'John', 'age': 20, 'job': 'Employer'}])
>>> new.index(20)
{'index': 1, 'value': 'age'}
>>> new[1]
20
>>> new[1:]
{'age': 20, 'job': 'Employer'}
>>> for key, value in new.items():
	print(key, ' = ', value)

	
name  =  John
age  =  20
job  =  Employer
>>> 
```

# License
Using the MIT License


