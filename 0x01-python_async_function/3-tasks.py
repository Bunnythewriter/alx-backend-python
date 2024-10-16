#!/usr/bin/env python3
"""Defines a task_wait_random function."""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that returns a task that waits for a random number
    of seconds."""
    return asyncio.create_task(wait_random(max_delay))
