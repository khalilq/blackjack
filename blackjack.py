import random
import time
wins = 0
ties = 0
count = 0



suits = {'Hearts':1,'Diamonds':2,'Clubs':3,'Spades':4}
cards = {'2':2,'3':3,'4':4,'5':5,
         '6':6,'7':7,'8':8,'9':9,'10':10,
         'J':10,'Q':10,'K':10,'A':11}


def calculate_hand(hand):
    score = 0
    ace_count = 0
    for card in hand:
        rank = card[0]
        score += cards[rank]
        if rank == 'A':
            ace_count += 1
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

while True:
    print("\n" + "="*30)
    print("NEW BLACKJACK GAME")
    print("\n" + "="*30)
    deck = []
    for suit in suits:
        for card in cards:
            deck.append((card,suit))
    player_hand = []
    dealer_hand = []
    random.shuffle(deck)

    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())


    player_score = calculate_hand(player_hand)
    dealer_score = calculate_hand(dealer_hand)

    print("Your hand:", player_hand)
    time.sleep(1)
    print("Dealer's showing card:", str(dealer_hand[0]) + ',', "(?, ?)")
    time.sleep(1)

    if player_score == 21 or dealer_score == 21:
        print("\n=== Blackjack! ===")
        print(f"Dealer's full hand: {dealer_hand} (Score: {dealer_score})")
        time.sleep(1)

        if player_score == 21 and dealer_score == 21:
            print("Both player and dealer have Blackjack! It's a tie.")
            ties += 1
            time.sleep(1)
        elif player_score == 21:
            print("Blackjack! You win!")
            wins += 1
            time.sleep(1)
        else:
            print("Dealer has Blackjack. You lose.")
            time.sleep(1)
    else:
        while True:
            print("Your score:",calculate_hand(player_hand))
            time.sleep(1)

            if calculate_hand(player_hand) > 21:
                print("Bust! You went over 21.")
                time.sleep(1)
                break
            if calculate_hand(player_hand) == 21:
                print("You got 21! Automatically standing.")
                time.sleep(1)
                break
            if len(player_hand) == 2:
                choice = input("Do you want to [h]it, [s]tand, or [d]ouble down? ").lower()
                time.sleep(1)
            else:
                choice = input("Do you want to [h]it or [s]tand? ").lower()
                time.sleep(1)
            if choice == "h":
                new_card = deck.pop()
                player_hand.append(new_card)
                print(f"You drew: {new_card[0]} of {new_card[1]}")
            elif choice == "s":
                print(f"Final score: {calculate_hand(player_hand)}")
                time.sleep(1)
                break
            elif choice == "d" and len(player_hand) == 2:
                new_card = deck.pop()
                player_hand.append(new_card)
                print(f"You drew: {new_card[0]} of {new_card[1]}")
                print("Your hand after doubling down:", player_hand)
                time.sleep(1)
                print("Your final score:", calculate_hand(player_hand))
                time.sleep(1)
                break
        if calculate_hand(player_hand) <= 21:
            print("\n--- Dealer's Turn ---")
            time.sleep(1)
            print("Dealer's hand:",dealer_hand)
            time.sleep(1)
            print("Dealer's score:",calculate_hand(dealer_hand))
            time.sleep(1)
            while calculate_hand(dealer_hand) < 17:
                print("Dealer hits...")
                time.sleep(1)
                dealer_new_card = deck.pop()
                dealer_hand.append(dealer_new_card)
                print("Dealer drew:",dealer_new_card)
                print("Dealer's score:",calculate_hand(dealer_hand))
                time.sleep(1)

        def check_winner(player_hand,dealer_hand):
            global wins
            global ties
            player_score = calculate_hand(player_hand)
            dealer_score = calculate_hand(dealer_hand)
            print("\n=== Final Results ===")
            time.sleep(1)
            print(f"Your score: {player_score} | Dealer's score: {dealer_score}")
            time.sleep(1)
            if player_score > 21:
                print("Bust! Dealer wins.")
                time.sleep(1)
            elif dealer_score > 21:
                print("Dealer busts! You win!")
                wins += 1
                time.sleep(1)
            elif player_score > dealer_score:
                print("You win!")
                wins += 1
                time.sleep(1)
            elif player_score < dealer_score:
                print("Dealer wins!")
                time.sleep(1)
            else:
                print("It's a tie!")
                ties += 1
                time.sleep(1)
        # Run the winner check
        if calculate_hand(player_hand) <= 21:
            check_winner(player_hand, dealer_hand)
        else:
            print("Dealer wins because you busted.")
    count += 1
    play_again = input("\nDo you want to play another hand? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
print("Wins:",wins)
print("Losses:",count-wins)
print("Ties:",ties)
print(f"Win percentage: {(wins * 100 / count):.2f}%")


