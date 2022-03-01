import os
import time
import logging
from functools import partial
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess as subp
from abc import ABC, abstractmethod
from colorama import Fore

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


class BaseExercise(ABC):
    @abstractmethod
    def is_not_done(self):
        ...

    @abstractmethod
    def process(self) -> None:
        ...

    def __str__(self) -> str:
        raise NotImplemented

    def __bool__(self) -> str:
        raise NotImplemented


class Exercise:
    def __init__(self, filepath=None) -> None:
        self.fp = filepath
        self.error = False
        self.output = None
        self.to_do = None
        self.is_not_done()

    def __str__(self) -> str:
        error_msg = f'Oops, something goes wrong in {self.fp} {Fore.RED}[ERROR]\n\n{Fore.RESET}{self.output}'
        success_msg = f'{self.fp} {Fore.GREEN}[SUCCESS]!{Fore.RESET}'
        if self.to_do:
            return f'{self.fp} {Fore.CYAN}[MAKE IT PASS]!{Fore.RESET}'
        return error_msg if self.error else success_msg

    def __bool__(self) -> bool:
        """Bool protocol for class
        Returns:
            bool: True if the exercise pass, False otherwise.
        """
        return not self.error
    
    def is_not_done(self) -> bool:
        with open(self.fp, 'r') as fp:
            self.to_do = '# I AM NOT DONE' in fp.read()
        return self.to_do

    def process(self) -> None:
        if self.is_not_done():
            return
        command = ['python', self.fp]
        r = subp.run(command, stdout=subp.PIPE, stderr=subp.PIPE)
        self.error = bool(r.returncode)
        self.output = r.stderr if self.error else r.stdout
        self.output = self.output.decode()


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


def process_exercises() -> None:
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


if __name__ == '__main__':
    process_exercises()
