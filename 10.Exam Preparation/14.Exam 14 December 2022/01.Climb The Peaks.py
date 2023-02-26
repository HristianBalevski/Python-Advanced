from collections import deque

food_portions = [int(num) for num in input().split(', ')]
stamina = deque([int(num) for num in input().split(', ')])

mountain_peaks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70
}

conquered_peaks = []

while True:
    if len(food_portions) == 0 or len(stamina) == 0 or len(mountain_peaks) == 0:
        break

    daily_food = food_portions.pop()
    daily_stamina = stamina.popleft()

    for peak, height in mountain_peaks.items():
        daily_power = daily_food + daily_stamina

        if daily_power >= height:
            conquered_peaks.append(peak)
            del mountain_peaks[peak]
            break
        else:
            break

if len(mountain_peaks) == 0:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print("Conquered peaks:")
    [print(p, sep='\n') for p in conquered_peaks]
