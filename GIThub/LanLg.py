import random
dem = 0
suits = ["Heart", "Diamonds", "Spades", "Club"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack",
         "Queen", "King", "Ace"]
values = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
          "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        compite = ""
        for card in self.cards:
            compite += ('\n'+card.__str__())
        return "The deck has:\n"+compite

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        result = self.cards.pop()
        return result


"""d =Deck()
d.shuffe()
a = d.deal()
print(a)"""


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_from_ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def Xuat(self):
        print(self.cards)


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def win_double_bet(self):
        self.total += (self.bet*2)


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much do you want to bet? "))
        except ValueError:
            print("Try again")
        else:
            if chips.bet > chips.total:
                print("Something's Wrong! Try again")
            else:
                break


def hit(deck, hand):
    a = deck.deal()
    hand.add_card(a)
    hand.adjust_from_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        choose = input('Do you want to hit or stand (h/s)?')
        if choose.lower() == 'h':
            hit(deck, hand)
        elif choose.lower() == 's':
            print('Waiting for dealer ')
            playing = False
        else:
            print('Try again')
            continue
        break


def show_apart(player, dealer):
    print("Dealer's Hand")
    print("<Hidden Card>")
    print(dealer.cards[0], '\n')
    print("Player's Hand", *player.cards, sep='\n')


def show_all(player, dealer):
    print("Dealer's Hand:", *dealer.cards, sep='\n')
    print('value:', dealer.value)
    print("Player's Hand:", *player.cards, sep='\n')
    print('value:', player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def player_win_final(player, dealer, chips):
    print("Player win five")
    chips.win_double_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    print("Welcome you to the game")
    d = Deck()
    d.shuffle()

    player = Hand()
    player.add_card(d.deal())
    player.add_card(d.deal())
    dealer = Hand()
    dealer.add_card(d.deal())
    dealer.add_card(d.deal())
    global player_chips
    player_chips = Chips()
    take_bet(player_chips)
    while playing:
        show_apart(player, dealer)
        hit_or_stand(d, player)
        # Check value of Player
        dem += 1
        if player.value > 21:
            show_all(player, dealer)
            player_busts(player, dealer, player_chips)
            break
    if player.value <= 21:
        while dealer.value < 17:
            hit(d, dealer)
        show_all(player, dealer)
        if dem == 5:
            player_win_final(player, dealer, player_chips)
        elif dealer.value > 21:
            dealer_busts(player, dealer, player_chips)
        elif dealer.value > player.value:
            dealer_wins(player, dealer, player_chips)
        elif dealer.value < player.value:
            player_wins(player, dealer, player_chips)
        else:
            push(player, dealer)
    # show_all(player,dealer)
    print("Chips= ", player_chips.total)
    c = input("Do you want to another hand?(y/n) ")
    if c[0].lower() == 'n':
        print("Thanks for playing")
        break
    elif player_chips.total <= 0:
        print("Sorry!! But you don't have enough money")
        break
    elif c[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Try a gain')
