from distutils.core import setup

setup(name='crust1',
      version='1.0.1',
      description='A python package to retreive information from the LLNL Crust 1.0 model.',
      author='John Leeman, Juan Manuel Haedo',
      author_email='john@leemangeophysical.com, juanu@juanu.com.ar',
      url='https://github.com/jrleeman/Crust1.0/',
      packages=['crust1'], # Package name
      package_data={'crust1': ['data/*.*']}, # Include data files
      include_package_data=True
     )