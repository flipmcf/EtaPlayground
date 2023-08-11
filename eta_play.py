"""
Just playing with estimating completion time of loops.
"""
import argparse
import logging
import time
import random
from datetime import datetime, timedelta
from typing import Optional

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(name)s:%(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger("etaplay")


def process_args():
    parser = argparse.ArgumentParser(description="play with looping ETA",
                                     usage="usage: eta.py <iterations> <sleep>")
    parser.add_argument("iterations",
                        help="number of iterations",
                        type=int
                        )

    parser.add_argument("sleep",
                        help="sleep time for each iteration",
                        type=float
                        )
    parser.add_argument('--sigma',
                        help='create a normal distibution around "sleep" with this sigma value',
                        type=float,
                        required=False,
                        default=0)

    parser.add_argument("-v", "--verbose",
                         help="turn on debug",
                         action="store_true"
                        )

    parsed_args = parser.parse_args()

    return parsed_args


def eta_play(iterations: int, sleep_time: float, sigma: Optional[float] = 0.0):

    iterable = range(0, iterations)
    count = 0
    average_duration = 0.0001  # a guess
    logger.debug(f"{iterations} iterations, {sleep_time} seconds wait, {sigma} deviation")
    tstart = time.monotonic()
    for item in iterable:
        wait = max(*(random.gauss(sleep_time, sigma), 0))
        logger.debug(f"sleeping for {wait} seconds")
        time.sleep(wait)
        count += 1

        remaining_time = (iterations - count) * average_duration
        logger.info(f"{count/iterations:.1%} ETA: {remaining_time:.0f} seconds |" +
                    f"{(datetime.now()+timedelta(seconds=remaining_time)).strftime('%Y-%m-%d %X')}")

        # figure out the estimated time to completion.
        tend = time.monotonic()
        duration = tend-tstart
        average_duration = average_duration + ((duration-average_duration)/count)
        tstart = tend  # next loop iteration start time is this loop iteration end time.

    logger.info(f"complete.")


if __name__ == "__main__":
    args = process_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug("debug on")

    eta_play(args.iterations, args.sleep, args.sigma)
