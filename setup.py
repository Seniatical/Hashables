from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='Hashize',
  version='0.0.1',
  description='Python Data Types Rewritten!',
    
  long_description=open('README.md', 'r', encoding='utf-8').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/Seniatical/Hashize/", 
    
  project_urls={
   "Homepage": "https://github.com/Seniatical/MechaK.py/",
   },
    
  author='Seniatical',
  license='MIT', 
  classifiers=classifiers,
  keywords='Data-Types', 
  packages=find_packages(),
  install_requires=[''] 
)
