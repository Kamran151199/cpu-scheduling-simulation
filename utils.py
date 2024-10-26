"""
This module contains utility functions for the project.
"""
import random

from schema import Process


def snake_case_to_title_case(snake_case: str) -> str:
    """
    Convert a string from snake_case to Title Case.

    :param snake_case: The snake_case string.
    :return: The Title Case string.
    """
    return ' '.join(word.capitalize() for word in snake_case.split('_'))


def generate_processes() -> list[Process]:
    """
    Generate a list of processes with random attributes (since it's a simulation).

    :return: A list of processes.
    """
    processes = []
    for i in range(1, 21):
        arrival_time = random.randint(0, 20)
        burst_time = random.randint(1, 10)
        priority = random.randint(1, 5)
        process = Process(pid=i, arrival_time=arrival_time, burst_time=burst_time, priority=priority)
        processes.append(process)
    return processes
