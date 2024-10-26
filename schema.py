"""
This module contains the schemas/dtos for the service.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Process:
    """
    Represents a process in the system.
    """
    pid: int
    arrival_time: int
    burst_time: int
    priority: int
    remaining_time: int = field(init=False)
    start_time: Optional[int] = None
    completion_time: Optional[int] = None
    waiting_time: int = 0
    turnaround_time: int = 0

    def __post_init__(self):
        self.remaining_time = self.burst_time


@dataclass
class Performance:
    """
    Represents the performance metrics of the processes in the system.
    """
    avg_waiting_time: float
    avg_turnaround_time: float
    cpu_utilization: float
    throughput: float