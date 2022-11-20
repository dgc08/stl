# stl - Python and bash based Shell with module support

## TODO
- Readme
- Documentation

## Installation

### Download and start of the shell

Download the Source code from Github: <br>
`git clone https://github.com/dgc08/stl.git`

Make sure you have Python 3 installed.

The interactive Shell is started with <br>
`python3 stl`

### Creating a launcher script

You can put a launcher script into `/usr/bin`, which starts a interactive shell.

A simple Launcher can look like this:

<code>#!/bin/bash <br>
&nbsp;python3 /path/to/stl $@
</code> 

## Importing as Python Library

STL can also be used as Python Library to process  commands. See in the documentation for more.

<b>THE USE AS PYTHON LIBRARY DOES NOT WORK. I'M TRYING TO FIX IT SOON.
