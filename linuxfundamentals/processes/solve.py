#!/opt/pwn.college/python
from os.path import exists
from time import sleep
from random import randint
import multiprocessing

DATA_FILE = "/tmp/.user.data"

def print_instructions():
    print("""
        In this challenge you will learn about Linux processes!
        A process is a running program on the computer. At any given time,
        there are many processes running. There are times where you will want
        to be able to view what processes are running on the system, and interact
        with them. To view the processes currently running, run the command "ps aux"
        in your terminal.

        For this challenge, I have started a process that will have the name
        "my_process_X", where X is a random number that I have assigned. Use the
        "ps aux" command to view the list of processes, and try to find the process
        that I have created. When you find it, run "/challenge/solve" again,
        enter the name of the process, and I will give you the flag!

        Good luck!
    """)

def process_func():
    while True:
        sleep(1)

def setup():
    process_name = f"my_process_{randint(1, 20)}"

    process = multiprocessing.Process(target=process_func, name=process_name)
    process.start()

def main():
    if not exists(DATA_FILE):
        print_instructions()
        setup()
        exit(0)

if __name__ == "__main__":
    main()
