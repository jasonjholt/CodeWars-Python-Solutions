def validate_hello(greetings):
    d = {"hello","ciao","salut","hallo","hola","ahoj","czesc"}
    greetings = greetings.split()
    for g in greetings:
        if g.lower().strip("!,:;?") in d: return True
    return False
