import time
import logging


def run_scheduler(interval, task):
    logging.info(
        f"Scheduler iniciado. Intervalo: {interval}s"
    )

    while True:
        task()
        time.sleep(interval)
