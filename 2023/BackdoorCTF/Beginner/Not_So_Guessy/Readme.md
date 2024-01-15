# Problem
- Figure out the secret_number from 1970
- Find the winning hand for 2020

# Solve
``` python
import subprocess

items = "Heads, Tails, Heads, Tails, Tails, Heads, Tails, Heads, Heads, Heads, Tails, Heads, Tails, Heads, Tails, Heads, Heads, Tails, Heads, Heads, Heads, Heads, Tails, Heads, Tails, Heads, Tails, Heads, Heads, Heads"
numbers = [1 if item.strip() == "Heads" else 0 for item in items.split(",")]
Secret_Number = 0
for i, num in enumerate(numbers):
    Secret_Number |= num << i
print(Secret_Number)
print(bin(Secret_Number))
print()

AI = {2: "Scissors", 1: "Paper", 0: "Rock"}
win = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}

hands = []
while Secret_Number:
    hand = AI[Secret_Number % 3]
    Secret_Number //= 3
    hands.append(win[hand])

print(hands)
command = ["python", "clone.py"]
# command = ["nc", "34.70.212.151", "8010"]
with subprocess.Popen(
    command,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
) as process:
    hand = "".join([hand + "\n" for hand in hands])
    stdout, stderr = process.communicate(hand.encode())
    print(stdout.decode())
    print(stderr.decode())
```