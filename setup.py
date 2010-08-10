from setuptools import setup
setup(name='password', 
    version='0.1',
    description='Password Python Package', 
    author='@huy', 
    author_email='', 
    license='MIT', 
    packages=['password'],
    install_requires=
    [
        'PyMySQL'
    ],      
    zip_safe=False)