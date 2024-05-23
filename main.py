import os
import random

# ----------------------------------------------------------------------------------------
# Game files
# ----------------------------------------------------------------------------------------
file_name = 'money.txt'
file_2_name = 'status.txt'
if os.path.exists(file_name):
    with open(file_name, 'r') as money_file:
        money = int(money_file.read())
else:
    with open(file_name, 'w+') as money_file:
        money_file.write('700')
        money_file.seek(0)
        money = int(money_file.read())

if os.path.exists(file_2_name):
    with open(file_2_name, 'r') as status_file:
        status = status_file.read()
else:
    with open(file_2_name, 'w+') as status_file:
        status_file.write('low baller')
        status_file.seek(0)
        status = status_file.read()

# ----------------------------------------------------------------------------------------
# Symbols and pay table
# ----------------------------------------------------------------------------------------
symbols = ['🖥', '🖱', '💾', '📀', '🤖', '🕹', '👁']

pay_table = {
    '🖥💾🤖': {'extended reels': '🕹📀', 'high roller': 10000, 'low baller': 1000},
    '🖥🖥🖥': {'extended reels': '🖥🖥', 'high roller': 100, 'low baller': 10},
    '🖱🖱🖱': {'extended reels': '🖱🖱', 'high roller': 90, 'low baller': 9},
    '💾💾💾': {'extended reels': '💾💾', 'high roller': 80, 'low baller': 8},
    '📀📀📀': {'extended reels': '📀📀', 'high roller': 70, 'low baller': 7},
    '🤖🤖🤖': {'extended reels': '🤖🤖', 'high roller': 60, 'low baller': 6},
    '🕹🕹🕹': {'extended reels': '🕹🕹', 'high roller': 50, 'low baller': 5},
    '👁👁👁': {'extended reels': '👁👁', 'high roller': 40, 'low baller': 4},
}


def update_pay_table():
    global pay_table
    for symbol in symbols:
        if status == 'high roller':
            pay_table[symbol + symbol + symbol + symbol + '_'] = 20
            pay_table['_' + symbol + symbol + symbol + symbol] = 20
            pay_table[symbol + symbol + '_' + symbol + symbol] = 10
            pay_table[symbol + symbol + symbol + '_' + '_'] = 5
            pay_table['_' + symbol + symbol + symbol + '_'] = 5
            pay_table['_' + '_' + symbol + symbol + symbol] = 5
            pay_table[symbol + symbol + '_' + '_' + '_'] = 1
            pay_table['_' + symbol + symbol + '_' + '_'] = 1
            pay_table['_' + '_' + symbol + symbol + '_'] = 1
            pay_table['_' + '_' + '_' + symbol + symbol] = 1
        else:  # status = low baller
            pay_table[symbol + symbol + '_'] = 1
            pay_table['_' + symbol + symbol] = 1


# ----------------------------------------------------------------------------------------
# Game art
# ----------------------------------------------------------------------------------------
logo_art = '''
 $$$$$$\  $$$$$$\         $$$$$$\ $$\          $$\              
$$  __$$\$$  __$$\       $$  __$$\$$ |         $$ |             
$$ /  \__$$ /  \__|      $$ /  \__$$ |$$$$$$\$$$$$$\   $$$$$$$\ 
$$ |     \$$$$$$\        \$$$$$$\ $$ $$  __$$\_$$  _| $$  _____|
$$ |      \____$$\        \____$$\$$ $$ /  $$ |$$ |   \$$$$$$\  
$$ |  $$\$$\   $$ |      $$\   $$ $$ $$ |  $$ |$$ |$$\ \____$$\ 
\$$$$$$  \$$$$$$  |      \$$$$$$  $$ \$$$$$$  |\$$$$  $$$$$$$  |
 \______/ \______/        \______/\__|\______/  \____/\_______/
'''

jackpot_art = '''
   $$$$$\ $$$$$$\  $$$$$$\ $$\   $$\$$$$$$$\  $$$$$$\$$$$$$$$\$$\$$\$$\ 
   \__$$ $$  __$$\$$  __$$\$$ | $$  $$  __$$\$$  __$$\__$$  __$$ $$ $$ |
      $$ $$ /  $$ $$ /  \__$$ |$$  /$$ |  $$ $$ /  $$ | $$ |  $$ $$ $$ |
      $$ $$$$$$$$ $$ |     $$$$$  / $$$$$$$  $$ |  $$ | $$ |  $$ $$ $$ |
$$\   $$ $$  __$$ $$ |     $$  $$<  $$  ____/$$ |  $$ | $$ |  \__\__\__|
$$ |  $$ $$ |  $$ $$ |  $$\$$ |\$$\ $$ |     $$ |  $$ | $$ |            
\$$$$$$  $$ |  $$ \$$$$$$  $$ | \$$\$$ |      $$$$$$  | $$ |  $$\$$\$$\ 
 \______/\__|  \__|\______/\__|  \__\__|      \______/  \__|  \__\__\__|
'''

four_in_a_row_art = '''
$$\   $$\       $$\                                                               
$$ |  $$ |      \__|                                                              
$$ |  $$ |      $$\$$$$$$$\        $$$$$$\         $$$$$$\  $$$$$$\ $$\  $$\  $$\ 
$$$$$$$$ $$$$$$\$$ $$  __$$\$$$$$$$\____$$\$$$$$$\$$  __$$\$$  __$$\$$ | $$ | $$ |
\_____$$ \______$$ $$ |  $$ \______$$$$$$$ \______$$ |  \__$$ /  $$ $$ | $$ | $$ |
      $$ |      $$ $$ |  $$ |     $$  __$$ |      $$ |     $$ |  $$ $$ | $$ | $$ |
      $$ |      $$ $$ |  $$ |     \$$$$$$$ |      $$ |     \$$$$$$  \$$$$$\$$$$  |
      \__|      \__\__|  \__|      \_______|      \__|      \______/ \_____\____/
'''

three_in_a_row_art = '''
 $$$$$$\       $$\                                                               
$$ ___$$\      \__|                                                              
\_/   $$ |     $$\$$$$$$$\        $$$$$$\         $$$$$$\  $$$$$$\ $$\  $$\  $$\ 
  $$$$$ $$$$$$\$$ $$  __$$\$$$$$$$\____$$\$$$$$$\$$  __$$\$$  __$$\$$ | $$ | $$ |
  \___$$\______$$ $$ |  $$ \______$$$$$$$ \______$$ |  \__$$ /  $$ $$ | $$ | $$ |
$$\   $$ |     $$ $$ |  $$ |     $$  __$$ |      $$ |     $$ |  $$ $$ | $$ | $$ |
\$$$$$$  |     $$ $$ |  $$ |     \$$$$$$$ |      $$ |     \$$$$$$  \$$$$$\$$$$  |
 \______/      \__\__|  \__|      \_______|      \__|      \______/ \_____\____/
'''


def print_jackpot_art():
    print(jackpot_art)


def print_four_in_a_row_art():
    print(four_in_a_row_art)


def print_three_in_a_row_art():
    print(three_in_a_row_art)


# ----------------------------------------------------------------------------------------
# Main menu
# ----------------------------------------------------------------------------------------
def menu():
    while True:
        try:
            ch = int(input('- (1) To play, enter 1\n'
                           '- (2) To see the pay table, enter 2\n'
                           '- (3) To view your status and balance, enter 3\n'
                           '- (4) To view the instructions, enter 4\n'
                           '- (5) To exit, enter 5\n'
                           '-> Choice: '))
            if ch < 1 or ch > 5:
                print('Invalid choice.')
                continue
            else:
                return ch
        except ValueError:
            print('Invalid input. Please enter a number.')


# ----------------------------------------------------------------------------------------
# Display the welcome screen
# ----------------------------------------------------------------------------------------
def welcome():
    print('-------------------------🖥🖱💾📀🤖🕹👁---------------------------')
    print(logo_art)
    print('👋 Welcome to the CS Slots game 👋')
    print('By Steven Woodward for CIT 129')
    print('Come to my GitHub -> https://github.com/stevexero')
    print('🎰 Place your bet and spin to match the symbols and win big! 🎰')
    print('-------------------------🖥🖱💾📀🤖🕹👁---------------------------')


# ----------------------------------------------------------------------------------------
# Displays the instructions for the game to the player
# ----------------------------------------------------------------------------------------
def instructions():
    while True:
        print('--------------- INSTRUCTIONS -----------------------')
        print('Your goal, like most, is to make as much money as possible.\n'
              'In order to do that, you\'ve got to go big!\n'
              'But you\'re just small beans right now, a low baller.\n'
              'And that\'s how you\'re known around here, a low baller with 700 bucks.\n'
              'Get out there, place some bets, build your balance, and try to\n'
              'get that high roller status!  You\'ll see the perks of doing so!\n\n'
              'Starting status: low baller\n'
              'Starting balance: 700\n\n'
              'Low ballers can bet between 1 and 5 and have 3 reels\n'
              'that have 4 combos to win.\n\n'
              'High ballers can bet between 6 and 20 and have 5 reels\n'
              'that have 12 combos to win.\n\n'
              'Your bet amount is a multiplier for the specified winnings\n'
              'amount in the pay table, depending on the combination spun.\n\n'
              'To achieve high roller status, get your balance up to 1000\n'
              'If your balance falls below 800, you will be reverted to low baller status\n\n'
              'High rollers will see fun art when they hit certain combinations.\n')
        print('----------------------------------------------------')
        ch = input('Return to the main menu? [y | n]: ')
        if ch.lower() == 'y':
            break
        else:
            continue


# ----------------------------------------------------------------------------------------
# Calculate the payout
# ----------------------------------------------------------------------------------------
def pay_calc(results, bet):
    # Joins the results to a single string
    result_key = ''.join(results)
    # Checks if the results are in the pay_table dict
    if result_key in pay_table:
        if result_key == '🖥💾🤖🕹📀' and status == 'high roller':
            print_jackpot_art()
            return pay_table[result_key]['high roller'] * bet
        elif result_key == '🖥💾🤖' and status == 'low baller':
            print_jackpot_art()
            return pay_table[result_key]['low baller'] * bet
        return pay_table[result_key][status] * bet
    # Checks for sequences or patterns in the pay_table dict
    else:
        if status == 'high roller':
            # First four in a row
            if result_key[:4] + '_' in pay_table:
                print_four_in_a_row_art()
                return pay_table[result_key[:4] + '_'] * bet
            # Last four in a row
            elif '_' + result_key[1:] in pay_table:
                print_four_in_a_row_art()
                return pay_table['_' + result_key[1:]] * bet
            # First two, any, last two
            elif result_key[:2] + '_' + result_key[-2:] in pay_table:
                return pay_table[result_key[:2] + '_' + result_key[-2:]] * bet
            # First three in a row
            elif result_key[:3] + '_' + '_' in pay_table:
                print_three_in_a_row_art()
                return pay_table[result_key[:3] + '_' + '_'] * bet
            # any, three in a row, any
            elif '_' + result_key[1:4] + '_' in pay_table:
                print_three_in_a_row_art()
                return pay_table['_' + result_key[1:4] + '_'] * bet
            # Last three in a row
            elif '_' + '_' + result_key[-3:] in pay_table:
                print_three_in_a_row_art()
                return pay_table['_' + '_' + result_key[-3:]] * bet
            # First two in a row
            elif result_key[:2] + '_' + '_' + '_' in pay_table:
                return pay_table[result_key[:2] + '_' + '_' + '_'] * bet
            # any, two in a row, any, any
            elif '_' + result_key[1:3] + '_' + '_' in pay_table:
                return pay_table['_' + result_key[1:3] + '_' + '_'] * bet
            # any, any, two in a row, any
            elif '_' + '_' + result_key[2:4] + '_' in pay_table:
                return pay_table['_' + '_' + result_key[2:4] + '_'] * bet
            # Last two in a row
            elif '_' + '_' + '_' + result_key[-2:] in pay_table:
                return pay_table['_' + '_' + '_' + result_key[-2:]] * bet
        else:  # status = low baller
            # First two in a row
            if result_key[:2] + '_' in pay_table:
                return pay_table[result_key[:2] + '_'] * bet
            # Last two in a row
            elif '_' + result_key[1:] in pay_table:
                return pay_table['_' + result_key[1:]] * bet
    # Returns 0 if nothing is found in the pay_table dict
    return 0


# ----------------------------------------------------------------------------------------
# Spin reels
# ----------------------------------------------------------------------------------------
def spin():
    global status
    # Spins x number of reels depending on status
    if status == 'high roller':
        num_reels = 5
    else:  # low baller status
        num_reels = 3
    results = []
    for _ in range(num_reels):
        # Sets symbol to a random choice for each reel and appends to results array
        symbol = random.choice(symbols)
        results.append(symbol)
    return results


# ----------------------------------------------------------------------------------------
# Game play loop
# ----------------------------------------------------------------------------------------
def play():
    global money
    global status
    print('----------------------------------------------------')
    print('Your current balance is: ' + str(money))
    print('----------------------------------------------------')
    print('Ready to play!  Enter -1 at any time to quit to the main menu')
    print('----------------------------------------------------')
    while True:
        # Take the user's bet as input, -1 to return to the main menu
        # try-except to validate user's input
        try:
            # Get user's bet based on status
            if status == 'high roller':
                bet = int(input('Place your bet between 6 and 20: '))
                if bet != -1 and bet < 6 or bet > 20:
                    print('Invalid entry')
                    continue
            else:  # low baller
                bet = int(input('Place your bet between 1 and 5: '))
                if bet != -1 and bet < 1 or bet > 5:
                    print('Invalid entry')
                    continue
            # Check user's bet
            if bet == -1:
                exit_game()
                break
            else:
                print('----------------------------------------------------')
                print('You\'ve bet ' + str(bet) + ', good luck!')
                # Spin the reels and set to results
                results = spin()
                print('----------------------------------------------------')
                # Display the results of the spin
                print('You\'ve spun ' + str(results))
                # Calculate the payout
                payout = pay_calc(results, bet)
                if payout > 0:
                    print('****************************************************')
                    print('Woohoo!  You\'ve won ' + str(payout) + '!')
                    print('****************************************************')
                # Sets money to the payout less the bet amount
                money = money - bet + payout
                # Shows user their balance
                print('Your new balance is: ' + str(money))
                print('----------------------------------------------------')
                # Checks the status of the user's money
                # Gives user the chance to reset their balance if they go to 0
                if money <= 0:
                    print('So, you lost all your money, huh?\nHow are you going to pay for school now?')
                    ch = input('I suppose we can reset you to 700. [y | n]: ')
                    if ch.lower() == 'y':
                        money = 700
                    else:
                        break
                    continue_play = input("Continue playing? [y | n]: ")
                    if continue_play.lower() != 'y':
                        break
                # Upgrade the status of the user if their balance goes over 1000
                elif money >= 1000 and status != 'high roller':
                    print('💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑')
                    print('****************************************************')
                    print('Woohoo! You\'ve reached high-roller status!!!')
                    print('****************************************************')
                    print('💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑💰🤑')
                    status = 'high roller'
                    # Update the status file
                    with open(file_2_name, 'w') as status_file:
                        status_file.write('high roller')
                    # Call an update to the pay table to keep the payouts current
                    update_pay_table()
                elif money <= 800 and status != 'low baller':
                    print('😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰')
                    print('Womp Womp, you lost your high-roller status')
                    print('😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰')
                    status = 'low baller'
                    # Update the status file
                    with open(file_2_name, 'w') as status_file:
                        status_file.write('low baller')
                    # Call an update to the pay table to keep the payouts current
                    update_pay_table()
                else:
                    # Do nothing
                    pass
        except ValueError:
            print('Invalid input. Please enter a number.')


# ----------------------------------------------------------------------------------------
# Print pay table
# ----------------------------------------------------------------------------------------
def display_pay_table():
    while True:
        print('--------------- PAY TABLE --------------------------')
        print('High Rollers:\n\t🖥💾🤖🕹📀: 10000 * bet amount (Jackpot)\n'
              '\t🖥🖥🖥🖥🖥: 100 * bet amount\n'
              '\t🖱🖱🖱🖱🖱: 90 * bet amount\n'
              '\t💾💾💾💾💾: 80 * bet amount\n'
              '\t📀📀📀📀📀: 70 * bet amount\n'
              '\t🤖🤖🤖🤖🤖: 60 * bet amount\n'
              '\t🕹🕹🕹🕹🕹: 50 * bet amount\n'
              '\t👁👁👁👁👁: 40 * bet amount\n'
              '\tAny 4-in-a-row: 20 * bet amount\n'
              '\t2-in-the-front and 2-in-the-rear: 10 * bet amount\n'
              '\tAny 3-in-a-row: 5 * bet amount\n'
              '\tAny 2-in-a-row: 1 * bet amount\n'
              'Low Ballers:\n\t🖥💾🤖: 1000 * bet amount (Jackpot)\n'
              '\t🖥🖥🖥: 10 * bet amount\n'
              '\t🖱🖱🖱: 9 * bet amount\n'
              '\t💾💾💾: 8 * bet amount\n'
              '\t📀📀📀: 7 * bet amount\n'
              '\t🤖🤖🤖: 6 * bet amount\n'
              '\t🕹🕹🕹: 5 * bet amount\n'
              '\t👁👁👁: 4 * bet amount\n'
              '\tAny 2-in-a-row: 1 * bet amount\n'
              )
        print('----------------------------------------------------')
        ch = input('Return to the main menu? [y | n]: ')
        if ch.lower() == 'y':
            break
        else:
            continue


# ----------------------------------------------------------------------------------------
# View player status and balance
# ----------------------------------------------------------------------------------------
def view_status_and_balance():
    while True:
        print('--------------- STATUS & BALANCE -------------------')
        print('Your current status is: ' + status)
        print('Your current balance is: ' + str(money))
        print('----------------------------------------------------')
        ch = input('Return to the main menu? [y | n]: ')
        if ch.lower() == 'y':
            break
        else:
            continue


# ----------------------------------------------------------------------------------------
# Exit game
# ----------------------------------------------------------------------------------------
def exit_game():
    with open(file_name, 'w') as user_file_quit:
        user_file_quit.write(str(money))
    print('----------------------------------------------------')
    print('Thanks for playing CS slots!')
    print('Your status on leaving is: ' + status)
    print('Your balance on leaving is: ' + str(money))
    print('----------------------------------------------------')


# ----------------------------------------------------------------------------------------
# Main - Enter here
# ----------------------------------------------------------------------------------------
def main():
    global money
    while True:
        welcome()
        update_pay_table()
        ch = menu()
        if ch == 1:
            if money <= 0:
                print('Looks like you\'ve got no money')
                choice = input('I suppose we can reset you to 700. [y | n]: ')
                if choice.lower() == 'y':
                    money = 700
                else:
                    continue
            else:
                play()
        elif ch == 2:
            display_pay_table()
        elif ch == 3:
            view_status_and_balance()
        elif ch == 4:
            instructions()
        else:
            exit_game()
            break


main()
