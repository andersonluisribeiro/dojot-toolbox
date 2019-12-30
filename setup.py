import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='dojot-cli',  
     version='0.0.8',
     scripts=['dojot'],
     author="Anderson Luis Ribeiro",
     author_email="anderson.luis.rib@gmail.com",
     description="A CLI for dojot",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/andersonluisribeiro/dojot-cli",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=[
        'pyfiglet==0.8.post1',
        'PyYAML==5.1.2',
        'gitpython==3.0.5',
        'termcolor==1.1.0',
        'progress==1.5',
        'ansible==2.9.2'
    ]
 )