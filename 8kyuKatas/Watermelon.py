def divide(melons):
  """
  sharing melons with a friend
  
  if melons can be split into even addends return True else False
  """
    if melons == 2:
        return False
    elif melons%2 == 0:
        return True
    else:
        for jason in range(melons + 1):
            lou = melons - jason
            if jason%2 == 0 and lou%2 == 0:
                return True
            return False
