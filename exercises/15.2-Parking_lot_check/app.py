parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot():
    state={
        "totalSlots":0,
        "availableSlots":0,
        "occupiedSlots":0
    }
    #print(state["availableSlots"]+1)
    for i in parking_state:
        for m in i:
            if m==2:
                state["availableSlots"]=state["availableSlots"]+1
                state["totalSlots"]=state["totalSlots"]+1
            elif m==1:
                state["occupiedSlots"]=state["occupiedSlots"]+1
                state["totalSlots"]=state["totalSlots"]+1
    return state
                
print(get_parking_lot())