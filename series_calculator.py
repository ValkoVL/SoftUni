import math

name_serial = str(input())
seasons = int(input())
episodes = int(input())
time_episode = float(input())

real_episode = time_episode * 1.2
extantion_last_episodes = 3*10

total_time = math.floor(real_episode * episodes * seasons) + extantion_last_episodes

print(f"Total time needed to watch the {name_serial} series is {total_time} minutes.")