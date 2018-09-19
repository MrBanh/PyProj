#! python3
# PyProj.py - Creates a directory template for python projects
# Usage:    
#           PyProj.py save <project name> - creates project directory
#           PyProj.py remove <project name> - removes project directory
#           PyProj.py <project name> - Shows where project directory is located
#           PyProj.py - Displays how to use script & list all project directories

import os
import re
import sys
import shelve
import send2trash
import pyperclip

scriptPath = os.path.split(__file__)

# Stores the projects and project directories in a file for projects created with this script
PyProjShelfDir = os.path.join(scriptPath[0], scriptPath[1] + '_Shelf')

# Create a directory to store data on the project folders created with this script
if not os.path.isdir(PyProjShelfDir):
    os.mkdir(PyProjShelfDir)

PyProjShelf = shelve.open(os.path.join(PyProjShelfDir, 'PyProj'))


def makeProjectDir(folder, projectName):
    # :param: folder - absolute path, parent directory of where this script is located
    # :param: projectName - name of new python project directory
    try:
        # Check for valid folder name
        folderRegex = re.compile(r'(\w)+')
        if folderRegex.search(projectName) == None:
            print('Invalid folder name, please run again...')
            exit()
        
        projectDir = os.path.join(folder, projectName)

        # Create new project directory
        os.mkdir(projectDir)

        # licenseFile = open(os.path.join(projectDir, 'LICENSE.txt'), 'w')
        readmeFile = open(os.path.join(projectDir, 'README.md'), 'w')
        # TODO: write to README.md file

        pythonFile = open(os.path.join(projectDir, f'{projectName}.py'), 'w')
        # TODO: write to the new python file

        # Create a .bat file in the parent (of this script) directory
        batFile = open(os.path.join(folder, f'{projectName}.bat'), 'w')
        batFile.write(f'@py.exe {os.path.join(projectDir, projectName)}.py %* \n@pause')

        # licenseFile.close()
        readmeFile.close()
        pythonFile.close()
        batFile.close()

        print()

    except FileExistsError:
        print('Project folder already exists. Please run again...')
        exit()


# sys.argv - ['script.py', arg1, arg2, ...]
# sys.argv[0] - name of the script
# sys.argv[1] - first line argument
# sys.argv[2] - second line argument

# Creating project file via terminal
if len(sys.argv) == 3 and sys.argv[1].lower() == 'add':
    if sys.argv[2].lower() != 'list':

        # Change to this script's directory
        os.chdir(scriptPath[0])

        # Change current directory to the parent directory
        os.chdir('..')

        # Adds a new project directory
        makeProjectDir(os.getcwd(), sys.argv[2])

        # Saves project directory to a file
        PyProjShelf[sys.argv[2]] = os.path.join(os.getcwd(), sys.argv[2])
        
        print(f'Created project folder: {sys.argv[2]} \nLocation: {PyProjShelf[sys.argv[2]]}')

        # Copy the new project directory to clipboard
        pyperclip.copy(f'{PyProjShelf[sys.argv[2]]}')
        print('\nCopied location to clipboard.\n')

    else:
        print('"list" is an argument in this script. \nPlease try a different project name')
        exit()

# Removing project file via terminal
elif len(sys.argv) == 3 and sys.argv[1] == 'remove':
    # Check if the project name is in the shelf data
    if sys.argv[2] in PyProjShelf:
        while True:
            # Confirm removal
            doRemove = input(f'Remove {sys.argv[2]} at [{PyProjShelf[sys.argv[2]]}]? (y/n): ')
            if doRemove.lower() == 'y':
                # Delete the .bat file
                currDir = os.getcwd()
                os.chdir(scriptPath[0])
                os.chdir('..')
                send2trash.send2trash(f'{sys.argv[2]}.bat')
                os.chdir(currDir)

                # Removes the project directory
                send2trash.send2trash(PyProjShelf[sys.argv[2]])
                del PyProjShelf[sys.argv[2]]

                break
            elif doRemove.lower() == 'n':
                exit()
            else:
                print('Invalid input')
    else:
        print('Project created with this script does not exist')
        exit()


elif len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        # Show all projects and their directories
        print(f'\n{"Projects":<20}  Location')
        print(f'{"--------":<20}  --------')
        for proj in PyProjShelf:
            print(f'{proj:<20}- {PyProjShelf[proj]}')

    # Show and copy the location of a project directory created with this script
    elif PyProjShelf.__contains__(sys.argv[1]):
        print(f'\n{sys.argv[1]} Located at: {PyProjShelf[sys.argv[1]]}')
        pyperclip.copy(f'{PyProjShelf[sys.argv[1]]}')
        print('\nCopied location to clipboard.\n')

    # Otherwise, tell user that a project directory was never created
    else:
        print(f'{sys.argv[1]} was never created.')

# Show how to use the script
elif len(sys.argv) == 1:
    print()
    print(f"Add the directory of this file to the environment variable: {scriptPath[0]}")
    print('\tIn Terminal:')
    print('\t\tPyProj.py save <project name> - creates project directory')
    print('\t\tPyProj.py remove <project name> - removes project directory')
    print('\t\tPyProj.py list - Shows all projects and directories')
    print('\t\tPyProj.py <project name> - Shows where project directory is located')
    print('\t\tPyProj.py - Displays how to use script')
    print()

PyProjShelf.close()