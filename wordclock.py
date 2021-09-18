import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for i in range(1, 28):
    GPIO.setup(i, GPIO.OUT)

current_hour = int(time.strftime('%H'))
current_minute = int(time.strftime('%M'))
hour_out = 0


def m0_4():
    global hour_out
    global current_hour
    hour_out = current_hour
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(24, GPIO.HIGH)


def m5_9():
    global hour_out
    global current_hour
    hour_out = current_hour
    GPIO.output(1, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m10_14():
    global hour_out
    global current_hour
    hour_out = current_hour
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m15_19():
    global hour_out
    global current_hour
    hour_out = current_hour + 1
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m20_24():
    global hour_out
    global current_hour
    hour_out = current_hour
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m25_29():
    global hour_out
    global current_hour
    hour_out = current_hour + 1
    GPIO.output(1, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m30_34():
    global hour_out
    global current_hour
    hour_out = current_hour + 1
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m35_39():
    global hour_out
    global current_hour
    hour_out = current_hour + 1
    GPIO.output(1, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.HIGH)
    GPIO.output(8, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m40_44():
    global hour_out
    global current_hour
    hour_out = current_hour + 1
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m45_49():
    global hour_out
    global current_hour
    hour_out = current_hour + 1
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m50_54():
    global hour_out
    global current_hour
    hour_out = current_hour + 1
    GPIO.output(1, GPIO.LOW)
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def m55_59():
    global hour_out
    global current_hour
    hour_out = current_hour + 1
    GPIO.output(1, GPIO.HIGH)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(8, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.HIGH)


def h0():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h1():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h1_ein():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h2():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h3():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h4():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h5():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h6():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h7():
    GPIO.output(9, GPIO.HIGH)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h8():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h9():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)


def h10():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)


def h11():
    GPIO.output(9, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)


while True:
    current_hour = int(time.strftime('%H'))
    current_minute = int(time.strftime('%M'))
    if 0 <= current_minute <= 4:
        m0_4()
    elif 5 <= current_minute <= 9:
        m5_9()
    elif 10 <= current_minute <= 14:
        m10_14()
    elif 15 <= current_minute <= 19:
        m15_19()
    elif 20 <= current_minute <= 24:
        m20_24()
    elif 25 <= current_minute <= 30:
        m25_29()
    elif 30 <= current_minute <= 34:
        m30_34()
    elif 35 <= current_minute <= 39:
        m35_39()
    elif 40 <= current_minute <= 44:
        m40_44()
    elif 45 <= current_minute <= 49:
        m45_49()
    elif 50 <= current_minute <= 54:
        m50_54()
    elif 55 <= current_minute <= 59:
        m55_59()
    if hour_out == 0 or hour_out == 12 or hour_out == 24:
        h0()
    elif hour_out == 1 or hour_out == 13:
        if 0 <= current_minute <= 4:
            h1_ein()
        else:
            h1()
    elif hour_out == 2 or hour_out == 14:
        h2()
    elif hour_out == 3 or hour_out == 15:
        h3()
    elif hour_out == 4 or hour_out == 16:
        h4()
    elif hour_out == 5 or hour_out == 17:
        h5()
    elif hour_out == 6 or hour_out == 18:
        h6()
    elif hour_out == 7 or hour_out == 19:
        h7()
    elif hour_out == 8 or hour_out == 20:
        h8()
    elif hour_out == 9 or hour_out == 21:
        h9()
    elif hour_out == 10 or hour_out == 22:
        h10()
    elif hour_out == 11 or hour_out == 23:
        h11()
