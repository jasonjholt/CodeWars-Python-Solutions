def update_light(current):
    """updating a traffic light
    
    goes green -> yellow -> red -> green
    """
    choose = {"green":"yellow", "yellow":"red","red":"green"}
    return choose[current]
