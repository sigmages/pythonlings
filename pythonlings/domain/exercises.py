from colorama import Fore
import subprocess as subp
from abc import ABC, abstractmethod


class BaseExercise(ABC):
    @abstractmethod
    def is_not_done(self):
        ...

    @abstractmethod
    def process(self) -> None:
        ...

    def __str__(self) -> str:
        raise NotImplementedError

    def __bool__(self) -> str:
        raise NotImplementedError


class Exercise:
    def __init__(self, filepath=None) -> None:
        self.fp = filepath
        self.error = False
        self.output = None
        self.to_do = None
        self.is_not_done()

    def __str__(self) -> str:
        error_msg = f"Oops, something goes wrong in {self.fp} {Fore.RED}[ERROR]\n\n{Fore.RESET}{self.output}"
        success_msg = f"{self.fp} {Fore.GREEN}[SUCCESS]!{Fore.RESET}"
        if self.to_do:
            return f"{self.fp} {Fore.CYAN}[MAKE IT PASS]!{Fore.RESET}"
        return error_msg if self.error else success_msg

    def __bool__(self) -> bool:
        """Bool protocol for class
        Returns:
            bool: True if the exercise pass, False otherwise.
        """
        return not self.error

    def is_not_done(self) -> bool:
        with open(self.fp, "r") as fp:
            self.to_do = "# I AM NOT DONE" in fp.read()
        return self.to_do

    def process(self) -> None:
        if self.is_not_done():
            return
        command = ["python", self.fp]
        r = subp.run(command, stdout=subp.PIPE, stderr=subp.PIPE)
        self.error = bool(r.returncode)
        self.output = r.stderr if self.error else r.stdout
        self.output = self.output.decode()
