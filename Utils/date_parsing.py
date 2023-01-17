import re


date_matching = r"^\d{4}[\-\/\s]?((((0[13578])|(1[02]))[\-\/\s]?(([0-2][0-9])|(3[01])))|(((0[469])|(11))[\-\/\s]?(([0-2][0-9])|(30)))|(02[\-\/\s]?[0-2][0-9]))$"


def search(year : str, month : str, day : str):
    
    complied_date = f"{year}-{month}-{day}"

    regex = re.search(pattern=date_matching, string=complied_date)
    if regex == None:
        print("False")
        return False 
    print("Not False")
    return True