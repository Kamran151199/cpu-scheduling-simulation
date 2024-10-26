"""
This module contains the algorithms of CPU scheduling.
"""
from schema import Process


def fcfs_scheduling(processes: list[Process]) -> list[Process]:
    """
    First Come First Serve Scheduling Algorithm implementation.
    This algorithm schedules processes based on their arrival time and processes them in the order they arrive.

    :param processes: list of processes
    :return: list of processes with updated start_time, completion_time, waiting_time, turnaround_time
    """
    processes.sort(key=lambda x: x.arrival_time)
    time = 0
    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time
        process.start_time = time
        process.waiting_time = time - process.arrival_time
        time += process.burst_time
        process.completion_time = time
        process.turnaround_time = process.completion_time - process.arrival_time
    return processes


def sjf_non_preemptive(processes: list[Process]) -> list[Process]:
    """
    Shortest Job First (SJF) Non-Preemptive Scheduling Algorithm implementation.
    This algorithm schedules processes based on their burst time and processes them in the order of shortest burst time.
    It is non-preemptive, meaning once a process starts executing, it will run to completion without interruption.

    :param processes: list of processes
    :return: list of processes with updated start_time, completion_time, waiting_time, turnaround_time
    """
    processes.sort(key=lambda x: x.arrival_time)
    completed = []
    time = processes[0].arrival_time
    ready_queue = []

    while len(completed) < len(processes):
        for process in processes:
            if process.arrival_time <= time and process not in completed and process not in ready_queue:
                ready_queue.append(process)
        if ready_queue:
            ready_queue.sort(key=lambda x: x.burst_time)
            current_process = ready_queue.pop(0)
            current_process.start_time = time
            current_process.waiting_time = time - current_process.arrival_time
            time += current_process.burst_time
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            completed.append(current_process)
        else:
            time += 1
    return processes

def sjf_preemptive(processes: list[Process]) -> list[Process]:
    """
    Shortest Job First (SJF) Preemptive Scheduling Algorithm implementation.
    This algorithm schedules processes based on their burst time and processes them in the order of shortest burst time.
    It is preemptive, meaning a process can be interrupted if a new process arrives with a shorter burst time.

    :param processes: list of processes
    :return: list of processes with updated start_time, completion_time, waiting_time, turnaround_time
    """
    time = 0
    completed = 0
    n = len(processes)
    ready_queue = []
    current_process = None

    while completed < n:
        for process in processes:
            if process.arrival_time == time:
                ready_queue.append(process)
        if current_process:
            if any(p.remaining_time < current_process.remaining_time for p in ready_queue):
                ready_queue.append(current_process)
                current_process = min(ready_queue, key=lambda x: x.remaining_time)
                ready_queue.remove(current_process)
        else:
            if ready_queue:
                current_process = min(ready_queue, key=lambda x: x.remaining_time)
                ready_queue.remove(current_process)
        if current_process:
            if current_process.start_time is None:
                current_process.start_time = time
            current_process.remaining_time -= 1
            if current_process.remaining_time == 0:
                current_process.completion_time = time + 1
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                current_process = None
                completed += 1
        time += 1
    return processes

def round_robin_scheduling(processes: list[Process], time_quantum: int = 2) -> list[Process]:
    """
    Round Robin Scheduling Algorithm implementation.
    This algorithm schedules processes in a circular queue and processes them in a cyclic order.
    Each process is assigned a fixed time quantum and if a process is not completed within the time quantum,
        it is moved to the end of the queue.

    :param processes: list of processes
    :param time_quantum: fixed time quantum for each process
    :return: list of processes with updated start_time, completion_time, waiting_time, turnaround_time
    """
    processes.sort(key=lambda x: x.arrival_time)
    time = 0
    ready_queue = []
    completed = []
    while len(completed) < len(processes):
        for process in processes:
            if process.arrival_time <= time and process not in completed and process not in ready_queue:
                ready_queue.append(process)
        if ready_queue:
            current_process = ready_queue.pop(0)
            if current_process.start_time is None:
                current_process.start_time = time
            execution_time = min(time_quantum, current_process.remaining_time)
            current_process.remaining_time -= execution_time
            time += execution_time
            for process in processes:
                if process.arrival_time <= time and process not in completed and process not in ready_queue and process != current_process:
                    ready_queue.append(process)
            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed.append(current_process)
            else:
                ready_queue.append(current_process)
        else:
            time += 1
    return processes

def priority_non_preemptive(processes: list[Process]) -> list[Process]:
    """
    Priority Scheduling Algorithm implementation.
    This algorithm schedules processes based on their priority and processes them in the order of highest priority.
    It is non-preemptive, meaning once a process starts executing, it will run to completion without interruption.

    :param processes: list of processes
    :return: list of processes with updated start_time, completion_time, waiting_time, turnaround_time
    """
    processes.sort(key=lambda x: x.arrival_time)
    completed = []
    time = processes[0].arrival_time
    ready_queue = []

    while len(completed) < len(processes):
        for process in processes:
            if process.arrival_time <= time and process not in completed and process not in ready_queue:
                ready_queue.append(process)
        if ready_queue:
            ready_queue.sort(key=lambda x: x.priority)
            current_process = ready_queue.pop(0)
            current_process.start_time = time
            current_process.waiting_time = time - current_process.arrival_time
            time += current_process.burst_time
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            completed.append(current_process)
        else:
            time += 1
    return processes


def priority_preemptive(processes: list[Process]) -> list[Process]:
    """
    Priority Scheduling Algorithm implementation.
    This algorithm schedules processes based on their priority and processes them in the order of highest priority.
    It is preemptive, meaning a process can be interrupted if a new process arrives with a higher priority.

    :param processes: list of processes
    :return: list of processes with updated start_time, completion_time, waiting_time, turnaround_time
    """
    time = 0
    completed = 0
    n = len(processes)
    ready_queue = []
    current_process = None

    while completed < n:
        for process in processes:
            if process.arrival_time == time:
                ready_queue.append(process)
                if current_process and process.priority < current_process.priority:
                    ready_queue.append(current_process)
                    current_process = None
        if not current_process and ready_queue:
            ready_queue.sort(key=lambda x: x.priority)
            current_process = ready_queue.pop(0)
            if current_process.start_time is None:
                current_process.start_time = time
        if current_process:
            current_process.remaining_time -= 1
            if current_process.remaining_time == 0:
                current_process.completion_time = time + 1
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                current_process = None
                completed += 1
        time += 1
    return processes


def multilevel_queue_scheduling(processes: list[Process]) -> list[Process]:
    """
    Multilevel Queue Scheduling Algorithm implementation.
    This algorithm schedules processes based on multiple queues with different priority levels.
    It could be implemented with different scheduling algorithms for each queue.

    :param processes: list of processes
    :return: list of processes with updated start_time, completion_time, waiting_time, turnaround_time
    """
    # Define queues
    rr_queue = []  # we gonna use Round Robin for this queue
    fcfs_queue = []  # we gonna use FCFS for this queue
    for process in processes:
        if process.priority <= 2:
            rr_queue.append(process)
        else:
            fcfs_queue.append(process)
    # Schedule queue1 with Round Robin
    round_robin_scheduling(rr_queue, time_quantum=4)
    # Schedule queue2 with FCFS
    fcfs_scheduling(fcfs_queue)
    # Combine results
    all_processes = rr_queue + fcfs_queue
    all_processes.sort(key=lambda x: x.pid)
    return all_processes


