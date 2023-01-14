from collections import deque

bullet_price = int(input())
size_of_gun_barrel = int(input())
bullets = [int(num) for num in input().split()]
locks = deque([int(num) for num in input().split()])
intelligence = int(input())

shoot_counter = 0
shooting = 0

while True:
    if len(bullets) == 0 or len(locks) == 0:
        break

    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_lock >= current_bullet:
        print("Bang!")
    else:
        locks.appendleft(current_lock)
        print("Ping!")

    shooting += 1
    shoot_counter += 1

    if shooting == size_of_gun_barrel and bullets:
        shooting = 0
        print("Reloading!")

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - shoot_counter * bullet_price}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
