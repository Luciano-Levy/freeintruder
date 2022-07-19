import io
from unittest import result
from lxml import etree
from colorama import Back, Fore, Style
from prettytable import PrettyTable



    

def matcher(responses,matches):
    
    
    print(Style.BRIGHT)
    table = PrettyTable()
    fields = ["Request","Payload","Position","Status","Lenght"] + matches
    fields = setTextStyle(fields,"fields")
    table.field_names = fields
    
    i = 1
    for res in responses:
        html_doc = io.BytesIO(res["res"])
        parser = etree.HTMLParser()
        tree = etree.parse(html_doc, parser)
        
        results = []
        
        for text in matches:
            
            search_results = tree.xpath(f"//*[contains(.,'{text}')]")
            results.append(len(search_results) > 0)
        
        res =[i,res["payload"],res["position"],res["status"],len(res["res"])] + results
        res = setTextStyle(res)
        table.add_row(res)
            
            
        i +=1
    print(table)
    
 
def setTextStyle(texts,style=None):
    temp = []
    for elem in texts:
        
        if(elem is True):
            temp.append(Style.BRIGHT + Fore.GREEN + "x" + Fore.RESET + Style.RESET_ALL)
        elif(elem is False):
            temp.append(Style.BRIGHT + Fore.RED + "x" + Fore.RESET + Style.RESET_ALL)
        
        elif(style == None):
            temp.append(Style.NORMAL + Fore.WHITE + str(elem)+ Fore.RESET)
        elif(style=="fields"):
            temp.append(Style.BRIGHT + Fore.BLUE + elem + Fore.RESET)
    
    return temp    