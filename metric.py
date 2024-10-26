"""
This module contains utilities for calculating metrics.
"""
from schema import Performance, Process


def calculate_performance_metrics(processes: list[Process]) -> Performance:
    """
    Calculate performance metrics for the given processes.

    :param processes: list of Process objects
    :return: dict containing performance metrics
    """
    total_waiting_time = sum(p.waiting_time for p in processes)
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    n = len(processes)
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    total_time = max(p.completion_time for p in processes) - min(p.arrival_time for p in processes)
    total_burst_time = sum(p.burst_time for p in processes)
    cpu_utilization = (total_burst_time / total_time) * 100
    throughput = n / total_time
    return Performance(avg_waiting_time, avg_turnaround_time, cpu_utilization, throughput)
