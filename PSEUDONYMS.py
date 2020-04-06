"""Generatefunnynamesbyrandomlycombiningnamesfrom2separate
lists."""
import sys
import random

def main():
        
    """Choosenamesatrandomfrom2tuplesofnamesandprinttoscreen."""

    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first=('BabyOil','BadNews','BigBurps',"Bill'Beenie-Weenie'",
        "Bob'Stinkbug'",'BowelNoises','Boxelder',"Bud'Lite'",
        'Butterbean','Buttermilk','Buttocks','Chad','Chesterfield',
        'Chewy','Chigger','Cinnabuns','Cleet','Cornbread',
        'CrabMeat','Crapps','DarkSkies','DennisClawhammer',
        'Dicman','Elphonso','Fancypants','Figgs','Foncy','Gootsy',
        'GreasyJim','Huckleberry','Huggy','Ignatious','Jimbo',
        "Joe'PottinSoil'",'Johnny','Lemongrass','LilDebil',
        'Longbranch','"LunchMoney"','Mergatroid','"MrPeabody"',
        'Oil-Can','Oinks','OldScratch','Ovaltine','Pennywhistle',
        'PitchforkBen','PotatoBug','Pushmeet','RockCandy',
        'Schlomo','Scratchensniff','Scut',"Sid'TheSquirts'",
        'Skidmark','Slaps','Snakes','Snoobs','Snorki','SoupcanSam',
        'Spitzitout','Squids','Stinky','Storyboard','SweetTea',
        'TeeTee','WheezyJoe',"Winston'JazzHands'",'Worms')

    last=('Appleyard','Bigmeat','Bloominshine','Boogerbottom',
        'Breedslovetrout','Butterbaugh','Clovenhoof','Clutterbuck',
        'Cocktoasten','Endicott','Fewhairs','Gooberdapple',
        'Goodensmith','Goodpasture','Guster','Henderson','Hooperbag',
        'Hoosenater','Hootkins','Jefferson','Jenkins',
        'Jingley-Schmidt','Johnson','Kingfish','Listenbee',"M'Bembo",
        'McFadden','Moonshine','Nettles','Noseworthy','Olivetti',
        'Outerbridge','Overpeck','Overturf','Oxhandler','Pealike',
        'Pennywhistle','Peterson','Pieplow','Pinkerton','Porkins',
        'Putney','Quakenbush','Rainwater','Rosenthal','Rubbins',
        'Sackrider','Snuggleshine','Splern','Stevens','Stroganoff',
        'Sugar-Gold','Swackhamer','Tippins','Turnipseed',
        'Vinaigrette','Walkingstick','Wallbanger','Weewax','Weiners',
        'Whipkey','Wigglesworth','Wimplesnatch','Winterkorn',
        'Woolysocks')
    
    while True:
        first_name= random.choice(first)
        last_name= random.choice(last)
        
        print("\n\n")
        # Trick IDLE by using "fatal error" setting to print name in red.
        print("{}{}".format(first_name,last_name),file=sys.stderr)
        print("\n\n")
        
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")

        if try_again.lower() == "n":
            break
        input("\nPress Enter to exit.")
        
if __name__ == "__main__":
    main()