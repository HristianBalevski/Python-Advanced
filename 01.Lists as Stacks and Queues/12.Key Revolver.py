from collections import deque

price_of_bullet = int(input())
size_of_the_gun_barrel = int(input())
bullets = [int(num) for num in input().split()]
locks = deque([int(num) for num in input().split()])
value_of_the_intelligence = int(input())

shot_counter = 0
barrel_counter = 0

while True:
    if len(bullets) == 0 or len(locks) == 0:
        break
    current_bullet = bullets[-1]
    current_lock = locks[0]

    if current_bullet <= current_lock:
        print('Bang!')
        locks.popleft()
        bullets.pop()
        shot_counter += 1
        barrel_counter += 1
    else:
        shot_counter += 1
        barrel_counter += 1
        bullets.pop()
        print("Ping!")
        
    if len(bullets) > 0 and barrel_counter == size_of_the_gun_barrel:
        print("Reloading!")
        barrel_counter = 0

if len(bullets) >= 0 and len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${value_of_the_intelligence - shot_counter * price_of_bullet}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
