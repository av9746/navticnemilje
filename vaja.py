name = raw_input("whats your name")

print("hello {}. I am a program that convertes km miles to miles".format(name))

def calculate(number):
    try:
        print (float(number) * float(0.621371192))
    except ValueError:
        print("Opps thats is not a number")


while True:
    answer_km = raw_input("enter kilometere: ")
    calculate(answer_km)
    answer_c = raw_input("would you like to do it again? ")
    if answer_c.lower() == "da":
        pass
    else:
        print("program shut down")
        break