MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
  while True:
    amount = input("Would you like to deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else: 
        print("Amount is less than 0.")
    else: 
      print("enter a number")
      
  return amount

def get_number_of_lines():
  while True:
    lines = input("How many lines would you like to bet on? (1-" + str(MAX_LINES) + "?)")
    if lines.isdigit():
      lines = int(lines)
      if lines <= MAX_LINES:
        break
      else:
        print("Enter a valid Number of lines")
    else:
      print("Please enter a number")

  return lines  


def get_bet():
  while True:
    amount = input("How much would you like to bet? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > MAX_BET:
        print(f"Enter a bet between {MIN_BET} - {MAX_BET}")
      else:
        break
    else: 
      print("Enter a valid bet")
  return amount

def main():
  balance = deposit()
  lines = get_number_of_lines()
  
  while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
      print(f"You don't have enough money to bet that much, your current amount is ${balance}")
    else:
      break

  print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()

    
