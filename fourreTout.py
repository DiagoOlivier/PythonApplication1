def trace(func):
    def decorateur():
        print("Début d'appel à", func)
        func()
        print("Fin d'appel à", func)
    return decorateur

def do_something():
    print("doing something")