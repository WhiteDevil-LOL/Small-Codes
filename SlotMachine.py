#Python Slot Machine 
import random

def spin_row():
    symbols = ['🔥', '🎖️', '👑', '🍭']

    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))

    return result

def print_row(row):
    print(" | " .join(row))


def get_payout(row,bet):

    if row[0]==row[1]==row[2]:
        if row[0] == '👑':
            return bet * 20
        elif row[0] == '🎖️':
            return bet * 10
        elif row[0] == '💫':
            return bet * 15
        elif row[0] == '🔥':
            return bet * 10
        else:
            return bet * 5 
    return 0



def main():
    balance = 100

    print("------------------------")
    print("WELCOME TO SLOT MACHINE")
    print("Symbols : 🔥 🎖️  👑 🍭 💫 ")
    print("------------------------")
    
    while balance>0:
        print(f"Current Balance : ₹{balance}")
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Enter a valid bet.")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds.")
            continue
        if bet <= 0 :
            print("Bet must be greater that 0.")

        balance -= bet

        row = spin_row()
        print("Spinning............\n")
        print_row(row)

        payout= get_payout(row,bet)

        if payout>0:
            print(f"You Won ₹{payout}")
        else:
            print("You lost this round")
        balance += payout

        play_again = input("Do you want to spin again(Y/N) :").upper()

        if play_again != 'Y':
            break
        
     
if __name__ == "__main__":
    main()