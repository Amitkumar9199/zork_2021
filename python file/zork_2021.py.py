from sys import exit

def _insidehouse():
    print"""
    you can see a large bunglow infront of you.
    there are large fields which have very long grasses (up to 7 feet long).
    you can either "1.go into long grasses" or "2.go inside the bunglow"
    """
    next=raw_input(">>")
    
    if next=="1":
        dead("you found a beautiful lady ghost,you moved forward and she killed you!")
    elif next=="2":
        _insidebunglow()
    
    else :
        print"this is not valid move"
        print"in the mean while an old man wandering on the door of bunglow saw you "
        print"he gave you suggestion to move out of this hell\n you don't listen to sufggestions"
        _insidehouse()
    
def dead(reason):
    print reason
    print "you made a wrong decision"
    print"bye-bye"
    exit(0) 
    
def _start():
    print"""
    you are outside a haunted bunglow                   
    you are not scared of ghosts 
    you have decided to explore this bunglow 
    you can "1.move inside" or "2.take more time to decide"
    """
    next=raw_input(">>")
    if "1" in next:
        _insidehouse()
    elif "2" in next:
        dead("the vampire living inside can't wait anymore for sucking your blood.on the 5th minute ,vampire killed you and sucked your blood")
    else:
        print"this is not a valid choice"
        print"try again"
        _start()
        
def _insidebunglow():
    print"""
    you are inside bunglow now
    this is very neat and clean
    looks like a human lives in here
    ***
    you can "1.move to room following staircase"
    you can "2.wander and find a suspicious kitchen"
    you can "3.move inside the cave "which opening is just beside the door,seems impossible but it is
    """
    
    next=raw_input(">>")
    if next=="1":
        _insideroom()
    elif next=="2":
        _insidekitchen()
    elif next=="3":
        _insidecave()
    else :
        dead("you took a lot  time time to think\nat the 5th minute vampire kills you and sucks blood.\n good day for vampire")
        
        
def _insideroom():
    print"""
    there are two dead bodies inside the room
    at a corner there is a girl crying,with a sweet voice
    you never heard such a beautiful voice in your life
    you can "1.shout hey girl"
    you can "2.move towards another corner and cry along with her"
    you can "3.go out of room"
    """
    next=raw_input(">>")
    if next=="1":
        print"she turns her head by 180 degrres \n her face is full of blood\n she smiles at you \nnow you join the membership of 2 dead bodies and make it 3\n that cute girl first cuts your neck and drink blood from the fountain"
        dead("")
    elif next=="2":
        dead("she loves you now\n you cried in a much better tone\nshe wants to marry you and have some vampire kids which will eat the whole village\n you have 1 night to live now ,although with that vampire girl ,xD ")
        
    elif next=="3":
        _insidebunglow()
    else:
        print"okay!since she has a cute voice.\n you fall in love ,although there are two dead bodies inside room\nyou move forward ,she also turns around and moved towards you\nshe is very beautiful\n you start kissing her\nafter a minute of enjoyment ,she put your head inside her mouth \n now you are no more to kiss anyone else"
        dead("")
        
        
def _insidekitchen():
    print"""
    here you find bad smell of rotten food
    as you go inside smell grows harder
    now you actually see a vampire sucking blood of a goat
    you can "1.advice vampire to stop doing this"
    you can "2.ran out"
    you can "3.join the party with vampire"
    
    """
    
    next=raw_input(">>")
    if next=="1":
        dead("he is more powerful than you ,you are now his meal.\nfool,you are dead")
    elif next=="2":
        _insidebunglow()
    elif next=="3":
        dead("vampire says:\ni have not seen such a foolish creature in my whole life,\ni will complain to my mom that you are taking my meal\nyou are dead\nher mom takes you as a meal") 
    else :
        dead("even after seeing this you didnt chose to ran out of bunglow\nyou should die now")
         
    
def _insidecave():
    print"""
    you make it long way inside
    finally you see that that the end is blocked with wall on which hanuman chalisa is written\n
    there is poison and holy liquid on other side
    now you hear scary noises,may be of vampire
    now you can "1.fight with vampire"
    you can "2.read hanuman chalisa"
    you can give up"3.eat poison"
    """
    next=raw_input(">>")
    if next=="1":
        dead("you are dead,you are not in bollywood so you lost your life")
    elif next=="2":
        print"vampire stops due to holy chant"
        print"""
        you can either "1.eat poison now"
        or "2.throw holy liquid on vampire"
        """   
        next1=raw_input(">>")
        if next1=="2":
            print"""
            you saved all villagers ,vamnpire is dead.
            the wall breaks ,leading a path to village .
            you are a true hero.
            well done
            """
            exit(0)
        elif next1=="1":
            print"coward,its easier for vampire to suck your blood now"
            dead("")
        else:
            dead("you are dead,vampire sucks your blood")
    elif  next=="3":
        dead("coward,its easier for vampire to suck your blood now")
    else:
        print"you took a lot of time to think"
        dead("vampired killed you and sucked your blood")
    
_start()
    
    
    
    
    
    
    
    
