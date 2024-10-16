#!/usr/bin/env python3
"""Module that executes wait_random."""
import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """Function that waits for a random number of seconds."""
    wait_time = random.random() * max_delay

    await asyncio.sleep(wait_time)
    return wait_time
