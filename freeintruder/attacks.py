from collections import OrderedDict
import re


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
                
                positions[key] = search.span(1)
               
    return positions