# PyProj

Add the directory of this file to the PATH environment variable.

In terminal, you can type:

    PyProj.py save <project name> - creates project directory
    PyProj.py remove <project name> - removes project directory
    PyProj.py list - Shows all projects and directories
    PyProj.py <project name> - Shows where project directory is located
    PyProj.py - Displays how to use script
    
Alternatively, you can create a .bat file in a directory that is already on your "Path" environment variable
  - For example, in the .bat file you can have

        @py.exe C:\Folder\to\the\PyProj.py %*
        @pause
    
  - Save as "PyProj.bat"
  
  - With this, you can just type in the terminal:
  
        PyProj save <project name>
        PyProj remove <project name>
        PyProj list
        PyProj <project name>
        PyProj

This script creates

    - A new project folder with a few template files (such as a README.md, LICENSE.txt, and the <project name>.py)
    - A <project name>.bat file in the parent directory of where the script is locate, with the included: @py.exe \...\<project name>.py  inside the .bat file
    - A folder (PyProj_Shelf) that holds a record of all projects created with this script, and where they are stored. It does not create multiple folders everytime you create a new project.
  
You can then add the parent directory to the PATH environment variable, and easily run all of your project scripts in terminal with:

    <project name> arg1 arg2 ...

