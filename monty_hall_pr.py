import random


class mhp():
    def __init__(self):
        pass

    def lets_play(self, choice):

        x = random.randint(1, 3)
        if (x % 2 == 0):
            d = {1: 'Nothing', x: 'Car', 3: 'Nothing'}
            if (choice == 1):
                print("Door 1: XXXX || Door 2: XXXX || Door 3: {}".format(d[3]))
            else:
                print("Door 1: {} || Door 2: XXXX || Door 3: XXXX ".format(d[1]))
            print("Do you want to change door: y-yes n-no -> ")
            st = input()
            if (st == 'no'):
                print("Door {} : {}".format(choice, d[choice]))
            else:
                if choice != 2:
                    print("Door 2 : {} ".format(d[2]))
                else:
                    print("Door 3 : {} ".format(d[3]))
        else:
            flag = 0
            #print(x)
            if x == 3:
                d = {1: 'Nothing', 2: 'Nothing', 3: 'Car'}
            else:
                d = {1: 'Car', 2: 'Nothing', 3: 'Nothing'}
            if (choice == 1 or choice == 3):
                print("Door 1: XXXX || Door 2: {} || Door 3: XXXX".format(d[2]))
            elif (choice == 2 and x == 3):
                print("Door 1: {} || Door 2: XXXX || Door 3: XXXX".format(d[1]))
                flag = 1
            else:
                print("Door 1: XXXX || Door 2: XXXX || Door 3: {}".format(d[3]))

            print("Do you want to change door: y-yes n-no ->")
            st = input()
            if (st == 'no'):
                print("Door {} : {}".format(choice, d[choice]))
            else:
                if choice == 1:
                    print("Door 3: {}".format(d[3]))
                elif choice == 3:
                    print("Door 1: {}".format(d[1]))
                elif choice == 2 and flag == 1:
                    print("Door 3: {}".format(d[3]))
                else:
                    print("Door 1: {}".format(d[1]))


i_mhp = mhp()
i_mhp.lets_play(int(input("Enter Door (1/2/3): ")))
