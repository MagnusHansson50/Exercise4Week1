

# Function that calculate the times it takes to travel 470km
# Return travel time in hours, minutes and seconds.
def calculateTime(v):
    seconds = ((470 / int(v)) * 3600)
    hours = seconds // 3600
    secondsLeft = seconds % 3600
    minutes = secondsLeft // 60
    secondsLeft = int (secondsLeft % 60)
    return hours, minutes, secondsLeft

v = input("Vilken hastighet i km/h kommer ni köra? ")

#try:
#    v = int(v)
#    h, m, s = calculateTime(v)
#    print(f"Det kommer att ta {h} timmar {m} minuter och {s} sekunder.")
#except ValueError:
#    print("Det är ingen giltig hastighet")

#if v.isdigit():
#    v = int(v)
#    h, m, s = calculateTime(v)
#    print(f"Det kommer att ta {h} timmar {m} minuter och {s} sekunder.")
#else:
#    print("Det är ingen giltig hastighet")

while True:
    v = input("Vilken hastighet i km/h kommer ni köra? ")

    try:
        v = int(v)
        if v > 0:
            h, m, s = calculateTime(v)
            print(f"Det kommer att ta {h} timmar {m} minuter och {s} sekunder.")
            break
        else:
            print("DeLorean hastighet är inte ok, ange en positiv hastighet")
    except ValueError:
        print("Det är ingen giltig hastighet")