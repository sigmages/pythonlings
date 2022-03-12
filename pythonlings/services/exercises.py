import os
import time
from functools import partial
import argparse
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from pythonlings.domain.exercises import Exercise


def get_exercises_root() -> str:
    """Returns the exercises path root

    Raises:
        FileNotFoundError: If exercises directory not found

    Returns:
        str: Exercises root
    """
    path = os.path.join(os.getcwd(), 'pythonlings', 'exercises')
    if not os.path.exists(path):
        raise FileNotFoundError(
            f'Path: {path} does not exist.'
            'Are you running Pythonlings in repository root?'
        )
    return path


def on_modified(event, exercise) -> None:
    exercise.process()
    print(exercise)


def observe_exercise_until_pass(exercise: Exercise) -> None:
    event_handler = PatternMatchingEventHandler(patterns=['*.py'], ignore_directories=True)
    event_handler.on_modified = partial(on_modified, exercise=exercise)
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(exercise.fp), recursive=False)
    observer.start()
    try:
        while exercise.error or exercise.to_do:
            time.sleep(1)
        else:
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def process_exercises(args: argparse.Namespace) -> None:
    root = get_exercises_root()
    for path, subdirs, files in os.walk(root):
        subdirs.sort()
        for file in sorted(files):
            fp = os.path.join(path, file)
            exercise = Exercise(fp)
            exercise.process()
            print(exercise)
            if exercise.error or exercise.to_do:
                observe_exercise_until_pass(exercise)


def process_single_exercise(args: argparse.Namespace) -> None:
    raise NotImplemented