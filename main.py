"""
This module is the entry point for the simulation and plotting of scheduling algorithms.
"""
from algorithm import (
    fcfs_scheduling,
    sjf_non_preemptive,
    sjf_preemptive,
    round_robin_scheduling,
    priority_non_preemptive,
    priority_preemptive,
    multilevel_queue_scheduling
)
import matplotlib.pyplot as plt
from metric import calculate_performance_metrics
from utils import snake_case_to_title_case, generate_processes


def main() -> None:
    """
    Main function to run the simulation and plot the performance metrics.

    :return: None (plots the performance metrics).
    """
    algorithms = [
        ('FCFS', fcfs_scheduling),
        ('SJF Non-Preemptive', sjf_non_preemptive),
        ('SJF Preemptive', sjf_preemptive),
        ('Round Robin', lambda p: round_robin_scheduling(p, time_quantum=4)),
        ('Priority Non-Preemptive', priority_non_preemptive),
        ('Priority Preemptive', priority_preemptive),
        ('Multilevel Queue', multilevel_queue_scheduling)
    ]
    metrics = {}
    for name, algorithm in algorithms:
        processes = generate_processes()
        algorithm(processes)
        metrics[name] = calculate_performance_metrics(processes)

    metric_names =    ['avg_waiting_time', 'avg_turnaround_time', 'cpu_utilization', 'throughput']

    for metric_name in metric_names:
        plt.figure(figsize=(10, 6))
        algorithm_names = list(metrics.keys())
        metric_values = [getattr(metrics[algo], metric_name, None) for algo in algorithm_names]
        plt.bar(algorithm_names, metric_values, color='skyblue')
        plt.xlabel('Scheduling Algorithms')
        plt.ylabel(metric_name)
        plt.title(f'{snake_case_to_title_case(metric_name)} Comparison')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()