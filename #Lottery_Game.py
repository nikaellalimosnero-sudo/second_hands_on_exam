#Lottery_Game
import random

def lottery_game():
  print("Lottery Game (6/60)")
  print("Each play costs ₱20. Enter 6 unique numbers between 1 and 60.\n")

  winning_numbers = set(random.sample(range(1, 61), 6))

  player_numbers = set()
  while len(player_numbers) < 6:
    try:
      num = int(input(f"Enter number {len(player_numbers)+1}: "))
      if num < 1 or num > 60:
        print("Invalid! Choose a number between 1 and 60.")
      elif num in player_numbers:
        print("You already picked this number. Choose another.")
      else:
        player_numbers.add(num)
    except ValueError:
      print("Invalid input. Please enter a number.")

  matches = winning_numbers.intersection(player_numbers)
  match_count = len(matches)

  if match_count == 6:
    prize = "You won ₱1,000,000 (Jackpot)"
  else:
    prize = f"₱{match_count * 1000:,}"
  print("\nWinning Numbers:", winning_numbers)
  print("Player Numbers:", player_numbers)
  print("Matches:", match_count)
  print("Prize:", "You won", prize)

if __name__ == "__main__":

  lottery_game()