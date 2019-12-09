
def speed_limit_checker(speed):
    points = 0
    temp = 0
    if speed <= 70:
        print("OK")
    else:
        temp = speed - 70 
        points = temp // 5 
        if points < 12:
            print("Points: %d" % (points))
        else:
            print("Liicense Suspendend ")

def main():
    input_hanlder = input("Sense Speed :")
    speed = int(input_hanlder)
    speed_limit_checker(speed)
    
if __name__=="__main__":
    main()
