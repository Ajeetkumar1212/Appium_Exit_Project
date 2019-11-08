from pathlib import Path
import json
import os
##JSON File Reader Function
def Call_fun(filename,key):
    path = Path(__file__).parent.parent
    path=os.path.join(path,"test_Module")
    os.chdir(path)
    with open("Locators.json") as file:
        f=json.load(file)
    return(f[key])

