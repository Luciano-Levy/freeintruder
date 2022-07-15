from collections import OrderedDict
import re

from requests import request


def positions_search(request,marker):
    
    positions = OrderedDict()
    
    for key,value in request.items():
         
        if(value is not None):    
            if(isinstance(value,OrderedDict) and len(value) > 0):
                positions[key] = positions_search(value,marker)
                continue

            pattern = f"(?:{marker})(.*?)(?:{marker})"
            search = re.search(pattern,str(value)) # First apareance or all, multiple parametres in one http field?
            if(search is not None):
                
                positions[key] = search.span()
               
    return positions

def sniper(request,positions,payloads,marker,level=None):
    pattern = f"(?:{marker})(.*?)(?:{marker})"
    
    for key,value in positions.items():
        for elem in payloads:
            with open(elem,"r",encoding="latin1") as file:
                for line in file:
                    new_request = dict(request)
                    

                    request_modifier(new_request,value,key,line,pattern,level)
                    
                    # Clear the other positions markers
                    # Make Asyncounus requests
                        
            file.close()
           
           
def parallel(request,positions,payloads,marker,level=None):
    pattern = f"(?:{marker})(.*?)(?:{marker})"
    
    for elem in payloads:
        with open(elem,"r",encoding="latin1") as file:
            for line in file:
                new_request = dict(request)
                for key,value in positions.items():
                    
                    request_modifier(new_request,value,key,line,pattern,level)     
                                       
            #REQUEST                    
                            
        file.close()
           
 
           
def request_modifier(request,value,key,line,pattern,level=None):
    
    if(isinstance(value,OrderedDict)):
        #sniper(request,value,payloads,marker,key)
        # Without recursion , it may be opening multiple file
        continue

    if level is None:
        og_string = request[key]
        request[key] = re.sub(pattern,line,og_string,1)

    else:        
        og_string = request[level][key]
        request[level][key] = re.sub(pattern,line,og_string,1) 
        
    return request