from collections import OrderedDict
import re
import string
# inform total requests


def attack_starter(request,attack,payloads,marker):
    pattern = f"(?:{marker})(.*?)(?:{marker})"
    positions = positions_search(request,pattern)
    print(positions)
    if(attack == "sniper"):
        for elem in payloads:
            with open(elem,"r") as file:
                tasks_request = sniper(request,positions,file,marker)
    if(attack == "parallel"):
        for elem in payloads:
            with open(elem,"r") as file:
                tasks_request = parallel(request,positions,file)



def sniper(request,positions,file,marker,pattern):
    
    total_requests = []
    for key,value in positions.items():            
        for line in file:
                
            new_request = dict(request)
            new_request = request_modifier(new_request,line,key,pattern,value[0])
            new_request = marker_cleaner(new_request,marker)
            
            
            total_requests.append(new_request)
                    
    return total_requests         
           
           
def parallel(request,positions,file,pattern):
    
    total_requests = []
    for line in file:
        
        new_request = dict(request)
        for key,value in positions.items():
           
            new_request = request_modifier(new_request,line,key,pattern,value[0])
                                       
        total_requests.append(new_request)                    

    return total_requests

# len(payloads) == len(positions)
# all individual patloads must have same len                            
# pass open files
"""
def pitchfork(files):
    
    for j in range(len(files[0])):
        for i in range(len(positions)):
            new_request = dict(request)
            #files[i] line j in position replace
        #REQUEST        
        
def cluster(files):
    for j in range(len(files[0])):
        for i in range(len(positions)):
            for k in files[i]:
"""            

    
def request_modifier(request,payload,key,pattern,level=None):
    # URL-ENCONDED
    print(request)
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