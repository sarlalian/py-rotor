from setuptools import setup, Extension

rotor = Extension('rotor',
	sources=['rotor/rotormodule.c'],
	depends=['rotor/rotormodule.c']
	)

setup(
	name = 'rotor',
	version = '1.0',
	description = 'The Rotor Module',
	ext_modules = [rotor],
  	packages = ['rotor'],
  	author = 'Lance Ellinghouse',
  	url = 'https://github.com/sarlalian/rotormodule',
  	keywords = ['encryption', 'logging', 'example'], # arbitrary keywords
	classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
