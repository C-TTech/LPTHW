print("""You enter a fark room with two doors.
Do you go through door #1 or Door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheescake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear. ")

    bear = input("> ")

    if bear == "1":
        print("The bear eats you")
    elif bear == "2":
        print("The bear eats half of you")
    else:
        print(f"Well, doing {bear} is probably better")
        print("Bear runs away. ")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("1. Blueberries. ")
    print("2. Yellow jacket clothespins. ")
    print("3. Understanding revolvers yelling melodies. ")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello")
        print("Good Job")
    else:
        print("The insanity bla bla bla bla")
        print("Good Job")

else:
    print("You stumble around")
