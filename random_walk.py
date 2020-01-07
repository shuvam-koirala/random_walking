import random
#here we assume n no of steps for this function
def walk(n):

     # starting coordinate for the drunk person
     x,y=0,0
     #Generating random choice for 2d SQUARE rolling experiment
     #having faces n,s,e,w
     #sample space={n,s,e,w}
     for i in range(n):
         step=random.choice(["n","s","e","w"])
        #assuming that the drunk person wals only one step according to  an event
        #applying the condition that if event is "n" then drunk person walks forward
         if step == "n":
                 #increasing co-ordinate y by 1
             y=y+1
        #applying the condition that if event is "s" then drunk person walks backward
         elif step == "s":
                 #decreasing co-ordinate y by 1
            y=y-1
        #applying the condition that if event is "e" then drunk person walks leftward
         elif step == "e":
                 #decreasing co-ordinate x by 1
            x=x-1
        #applying the condition that if event is "w" then drunk person walks rightward
         elif step == "w":
                #increasing co-ordinate x by 1
             x=x+1
    #returning the final co-ordinate after n steps
     return (x,y)

def distance():
    pos=0 #setting the total travelled distance as 0
    for trail in range (100): # performing 100 trails
        dist= walk(1000) #assuming the steps be 1000
        #calculating the distance travelled by drunk person from starting position(x=0,y=0)
        pos=pos+(((dist[0]**2)+(dist[1]**2))**(1/2))
        #returning the average distance travelled by drunk person from starting position(x=0,y=0)
    return (round(pos/100))
print("Starting coordinate for the drunk person.")
print("x=0 ,y=0")
print("Let, 1 step of drunk person is regared as 2 feet.")
print("Assuming the number of steps randomly travelled by drunk person be: 1000 steps ")
print("On Performing 100 trails of experiment.")

print("The average steps that is covered by the drunk person is :{%d}").format(distance())
print("The average distance  that is covered by the drunk person is : {%d} feet").format(distance()*2)
