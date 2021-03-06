from distutils.core import setup
setup(name='LabJackPython',
      version='10-22-2012',
      description='The LabJack python module.',
      url='http://www.labjack.com/support/labjackpython',
      author='The LabJack crew',
      package_dir = {'': 'src'},
      py_modules=['LabJackException', 'LabJackPython', 'Modbus', 'u3', 'u6', 'ue9', 'u12', 'skymote']
      )
