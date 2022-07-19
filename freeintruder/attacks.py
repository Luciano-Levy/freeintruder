from collections import OrderedDict
import re
import string
# inform total requests


def attack_starter(request,attack,payloads,marker):
    pattern = f"(?:{marker})(.*?)(?:{marker})"
    positions = positions_search(request,pattern)
    if(len(positions) == 0):
        raise Exception("You forgot the markers")
    tasks_request = []
    if(attack == "sniper"):
        
            tasks_request = sniper(request,payloads,positions,marker,pattern)
            
    elif(attack == "parallel"):
        
            tasks_request = parallel(request,positions,payloads)
    else:
        raise Exception("Attack not yet implemented")
    return tasks_request

def sniper(request,payloads,positions,marker,pattern):
    
    total_requests = []
    for key,value in positions.items():            
        for elem in payloads:
            with open(elem,"r") as file:
                for line in file:
                    
                    new_request = dict(request)
                    new_request = request_modifier(new_request,line,key,pattern,value[0])
                    new_request = marker_cleaner(new_request,marker)
                    
                    
                    total_requests.append({"req":new_request,"payload": line,"position":key})
           
    return total_requests         
           
           
def parallel(request,payloads,positions,pattern):
    
    total_requests = []
    for elem in payloads:
        with open(elem,"r") as file:
            for line in file:
                
                new_request = dict(request)
                for key,value in positions.items():
                
                    new_request = request_modifier(new_request,line,key,pattern,value[0])
                                            
                total_requests.append(new_request)                    

    return total_requests
         
    
def request_modifier(request,payload,key,pattern,level=None):
    # URL-ENCONDED
    
    payload = payload.strip()
    if(level is not None):       
        request[level][key] = re.sub(pattern,payload,request[level][key])
    else:    
        request[key] = re.sub(pattern,payload,request[key])
        
    return request

def marker_cleaner(request,marker):
    clean_request = dict(request)
    for key,value in request.items():
        if(value is not None):    
            if(isinstance(value,OrderedDict) and len(value) > 0):
                clean_request[key] = marker_cleaner(value,marker)
                continue

            if(isinstance(value,str)):
                clean_request[key] = value.replace(marker,"") 
    
    return clean_request       
        
def positions_search(request,pattern,level=None):
    
    positions = OrderedDict()
    
    for key,value in request.items():
         
        if(value is not None):    
            if(isinstance(value,OrderedDict) and len(value) > 0):
                positions.update(positions_search(value,pattern,key))
                continue

           
            search = re.search(pattern,str(value)) # First apareance or all, multiple parametres in one http field?
            if(search is not None):
                
                positions[key] = (level,search.span())
               
    return positions