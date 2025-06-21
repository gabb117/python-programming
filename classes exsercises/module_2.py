import coin

def main():
    c1 = coin.Coin()
    c2 = coin.Coin()

    for i in range(5):
        c1.flip()
        c2.flip()

    print("Coin 1: ",c1,"Coin 2: ",c2)

main()

#this module will print also the __str__ function
