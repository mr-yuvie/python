import random

MAX_LINES = 5
MAX_BET=1000
MIN_BET=100

ROWS=5
COLS=5

symbol_count = {"A":5,"X":1,"5":4,"9":3,"7":2}
symbol_value = {"A":2,"X":50,"5":5,"9":10,"7":20}

def deposit():
    while True:
        amount = input("Enter your Deposit: $")
        if amount.isdigit():
            amount =int(amount)
            if amount > 0 and amount <= 10000:
                break
            else:
                print("Amount must be between $0 and $10K.")
        else:
            print("Enter a valid amount.")

    return amount

def get_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines =int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print(f"Lines must be between 1 and {MAX_LINES}.")
        else:
            print("Enter a valid number.")

    return lines

def get_bet():
    while True:
        bet = input(f"What would you like to bet(${MIN_BET}-${MAX_BET}): $")
        if bet.isdigit():
            bet =int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print("Bet must be between $100 and $1000.")
        else:
            print("Enter a valid bet.")

    return bet

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols= []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]

        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row])

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbool]*bet
            winning_lines.append(line + 1)
        
    return winnings,winning_lines

def spin(balance):
    lines=get_lines()
    
    while True:
        bet=get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You do not have enough balance. Your current balance is: ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines.Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}. on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance ${balance}")
        play = input("Press enter to play(x to exit).")
        if play == "x":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
    
main()