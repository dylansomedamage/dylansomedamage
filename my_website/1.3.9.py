import time
#This is a comment
def ralph():
    print("You wake up to realize that you are Wreck-It-Ralph.")
    time.sleep(3)                  
    print('  __       _       _         __       _               __                      _   _     _')          
    print('/__\ __ _| |_ __ | |__     /__\_   _(_)_ __  ___    /__\_   _____ _ __ _   _| |_| |__ (_)_ __   __ _')
    print('/ \/// _` | | \'_ \| \'_ \/ \// | | | | \'_ \/ __|  /_\ \ \ / / _ \ \'__| | | | __| \'_ \| | \'_ \ / _\` | ')
    print('/ _  \ (_| | | |_) | | | |/ _  \ |_| | | | | \__ \ //__  \ V /  __/ |  | |_| | |_| | | | | | | | (_| |')
    print('\/ \_/\__,_|_| .__/|_| |_| \/ \_/\__,_|_|_| |_|___/ \__/   \_/ \___|_|   \__, |\__|_| |_|_|_| |_|\__, |')                                                 
    time.sleep(2)
    print('You look around to find yourself in a penthouse and walk out to explore.')
    time.sleep(1)
    choice=raw_input('You heard a loud noise coming from Game Central Station. Do you go to Game Central Station? (Y/N)')
    if choice == "Y":
        print ('You think about going to Game Central Station, but you decide not to.')
    if choice == "N":
        print('You watch Netflix until you get bored.')
    time.sleep(3)
    choice=raw_input('Will you now go to Game Central Station? (Y/N)')
    if choice == "Y":
        print ("Finally, some excited!")
    if choice == "N":
        print ("You go to take a nap and then you go to Game Central Station.")
    time.sleep(1)
    choice=raw_input('You find Vanellope running from Stormtroopers. Where do you take them?(Sugar Rush/Slaughter Race)')
    while choice != 'Sugar Rush' and choice !='Slaughter Race':
        choice=raw_input('Invalid Answer. Try again(Sugar Rush/SlaughterRace)')
    if choice == 'Sugar Rush':
        print('The Sugar Rush Racers welcome their princess back.')
        time.sleep(1)
        print('They hand her a new racecar.')
        time.sleep(1)
        print('She goes to race the most predictable tracks and wins first again and you go back to your game.')
        return
    else: #you chose Slaughter Race
        choice=raw_input('You must get to it before the arcade opens. How do you do it?(Glitching/Virus):')
        while choice != 'Glitching' and choice != 'Virus':
            choice=raw_input('Invalid Answer.Try again. (Glitching/Virus)')
        if choice == 'Glitching':
            print('You go to the internet.')
            time.sleep(1)
            print('Vanellope glitches until you both get to Slaughter Race and you go back to your game.')
            time.sleep(1)
            return
        else: #you chose Virus
            print('You obtained a virus from a suspicious character.')
        time.sleep(3)
        print('Oh no! It got out of control!')
        time.sleep(2)
        for blank in ['Malware']:
            print('The '+blank+' virus infects the internet... but it misses you and Vanellope.')
            time.sleep(2)
        print('You save Vanellope.')
        time.sleep(1)
        choice=raw_input('You guys escape the virus and the internet and decide to go back to Game Central Station. Where do you go?(New game called TPAA/Tapper)')
        while choice != 'New game called TPAA' and choice != 'Tapper':
            choice=raw_input('Invalid Answer.Try again. (New game called TPAA/Tapper)')
        if choice =='New Game called TPAA':
            print('You go into TPAA.')
            time.sleep(1)
            print('You see a building.')
            time.sleep(1)
            print('You wreck it because of the incident in the internet and you want to let off some steam.')
            return
        else: #choice was Tapper
            print('You and Vanellope grab a root beer')
            time.sleep(1)
            print('You guys disagree on your favorite video game, you fight and decide to not be friends anymore.')