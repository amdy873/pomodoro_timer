#pomodoro timer app
import time
import winsound
import os

def out(time_min,time_sec):
    if(time_sec == 0):
        time_sec = "0"+str(time_sec)
    print("\r"+str(time_min)+":"+str(time_sec),end=" ")

def get_tasks():
    tasks = []
    for i in range(4):
        tasks.append(input("Task #"+str(i+1)+": "))

    return tasks

tasks = get_tasks()
timer_start = True


def timer_run(time_min, time_sec):
    out(time_min,time_sec)
    while(time_min != 0 or time_sec != 0):
        time.sleep(1)
        time_sec -= 1
        if(time_sec < 0):
            time_sec = 59
            time_min -= 1
        out(time_min,time_sec)


def run_task(task):
    print("Working on: " + task)
    timer_run(25,0)
    print("\n")
    winsound.PlaySound("SystemMessageNudge",winsound.SND_ALIAS)
    


def run_break():
    print("Break Time")
    timer_run(5,0)
    print("\n")
    winsound.PlaySound("SystemQuestion",winsound.SND_ALIAS)
    

def run_long_break():
    print("\nBreak Time")
    timer_run(20,0)
    print("\n")
    winsound.PlaySound("SystemHand",winsound.SND_ALIAS)

while True:
    for x,i in enumerate(tasks):
        run_task(i)
        if(x != 3):
            run_break()
    run_long_break()

    cont = input("Continue (N to quit)? ")
    if(cont == "N" or cont == "n"):
        break

    if(input("Would you like to change the tasks (Y for yes)? ") == "y" or "Y"):
        tasks = get_tasks()
    
