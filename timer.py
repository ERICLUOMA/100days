"""
Created on Tue Nov 20 09:32:56 2018
Timer
"""

from datetime import datetime
from datetime import timedelta


def main():
    userinput = input("Please set the number of minutes for the Pomadoro Timer:")

    current = datetime.now().replace(microsecond=0)
    timerperiod = timedelta(minutes=int(userinput), microseconds=0)

    settimer = current + timerperiod

    print("Current time is:", current)
    print("Timer will expire at:", settimer)
    print("Running....")

    while True:

        current = datetime.now().replace(microsecond=0)

        if current >= settimer:
            print('Timer Done')
            break

    runagain = input("Do you want to run another timer. Type Y or N:").upper()

    if runagain == 'Y':
        main()
    else:
        print('Timer closing')


if __name__ == "__main__":
    print("Timer Started")
    print("Press Ctrl+C to terminate timer early")
    try:
        main()
    except KeyboardInterrupt:

        print("Ctrl+C pressed. Cancelling timer...")
