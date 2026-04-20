3.1 Mickey's Clock Application

Objective: Create a digital-style clock using Mickey Mouse hand graphics

Requirements:

Display current system time (minutes and seconds only)
Use Mickey Mouse's hands as clock hands
Right hand = minutes hand
Left hand = seconds hand
Synchronize with system clock in real-time
Update display every second
Implementation Tips:

Use pygame.transform.rotate() to rotate hands
Reference: StackOverflow - Rotating Graphics
Calculate rotation angles based on current time
Handle edge cases (leap seconds, etc.)
Repository Structure:

Practice7/
├── mickeys_clock/
│   ├── main.py
│   ├── clock.py
│   ├── images/
│   │   └── mickey_hand.png
│   └── README.md