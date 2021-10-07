# BneiAkivaTuckShop
Repo for the Tuck shop Software for Bnei Akiva

tuch5774 contains old software, requires java version 8 update 281 to run on a pc clean of any other java versions.

TuckShop5781 contains an executable file for distribution which contains all the dependencies required.

    It uses .json files to store tuck shop data, and will export .xlsx files for generating tuck lists and calculating change.
    Any files created by the executable will be saved to whichever folder it is run from.
    Can import from .xlsx files, but requires specific formatting. No column headers, with columns in order being [firstname, lastname, funds] for chanichim and [name,price] for       tuck
    
TuckShop5781 also contains a folder called Code which includes the python files which were bundled for the executable, as well as some other files that were used during development. 
    
    TuckShopUI.ui was edited using qtdesigner, and converted to TuckShopUI.py with pyuic5.
    Running TuckShop.py with python should execute the program. Requires python 3.8 or later.

Library Dependencies for running the python distribution:
    
    PyQt5
    json
    pandas
    xlrd <--Might not be needed, there's a possibility pandas might throw an error without it though
