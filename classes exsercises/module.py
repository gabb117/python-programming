#import the module coin.py

import coin

def main():
    c = coin.Coin()#enter the name of module near the class name (coin.Coin())

    print(c.get_sideup())
    for i in range(5):
        c.flip()
        print(c.get_sideup())

main()

