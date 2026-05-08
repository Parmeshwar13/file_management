import os
from datetime import datetime
data=[]
with open('text.txt',"r") as f:
    
    for i in f:
        parts=i.strip().split(':')
        if len(parts)==2:
            data.append({"line_number":parts[0].strip(),"content":parts[1].strip(),'created_at':datetime.now().isoformat(),
                         'updated_at':datetime.now().isoformat()})


        

print(data)
with open('structured_data.json',"w") as f:
    import json
    json.dump(data,f,indent=4)
    