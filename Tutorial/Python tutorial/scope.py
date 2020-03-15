# Variable scope LEGB
# 1.Local
# 2.Enclosing
# 3.Global
# 4.Bulitin

# GLOBAL

name ='I am global Variable scope'

def greet():
    #Enclosing
    # name = 'I am Enclosing Variable scope'

    def hello():
        #local
        # name = 'I am local Variable scope'
        print('Hello '+name)

    hello()

greet()
