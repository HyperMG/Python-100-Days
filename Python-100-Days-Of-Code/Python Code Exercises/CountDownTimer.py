import time

sec = int(input('How Many sec Countdown: '))

for x in range(sec):
    print(str(sec - x) + ' Seconds Remaining')
    time.sleep(1)