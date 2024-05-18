from machine import Pin
import time

# Create a Pin object for the built-in LED.
# Pin.OUT means we're going to write to the pin.
# LED is connected to pin 25.
led = Pin("LED", Pin.OUT)

# Create a function of an AND gate.


def andGate(a, b):
    if a == 1 and b == 1:
        print("\nA =", a, "B =", b)
        led.value(1)
        print("\nLED is activated")
    else:
        print("\nA =", a, "B =", b)
        led.value(0)
        print("\nLED is not activated.")

# Create a function of a NOT gate.


def notGate(a):
    if a == 0:
        print("\nA =", a)
        led.value(1)
        print("\nLED is activated")
    else:
        print("\nA =", a)
        led.value(0)
        print("\nLED is not activated.")

# Create a function of an XOR gate.


def xorGate(a, b):
    if a == b:
        print("\nA =", a, "B =", b)
        led.value(0)
        print("\nLED is not activated.")
    else:
        print("\nA =", a, "B =", b)
        led.value(1)
        print("\nLED is activated.")


# Define an endless loop to test the gates.
while True:
    print("\nSelect a gate to test.")  # Print the menu of the available gates.
    print("\n1 -> AND-Gate")
    print("\n2 -> NOT-Gate")
    print("\n3 -> XOR-Gate")
    print("\n4 -> Exit")

    choice = int(input("\nEnter your choice (1) to (4): "))
    if choice == 1:
        a = int(input("\nEnter the value of A: "))
        b = int(input("\nEnter the value of B: "))
        andGate(a, b)
        continue
    elif choice == 2:
        a = int(input("\nEnter the value of A: "))
        notGate(a)
        continue
    elif choice == 3:
        a = int(input("\nEnter the value of A: "))
        b = int(input("\nEnter the value of B: "))
        xorGate(a, b)
        continue
    elif choice == 4:
        break
    else:
        print("\nInvalid choice. Please try again.")
        continue
