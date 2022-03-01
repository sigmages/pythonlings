from pythonlings import __version__
from pythonlings.__main__ import get_exercises_root, Exercise
from uuid import uuid4
import os
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_get_exercises_root_success():
    get_exercises_root()


def test_get_exercises_root_fail(mocker):
    invalid_dir = uuid4().hex
    mocker.patch('os.getcwd', return_value=invalid_dir)
    with pytest.raises(FileNotFoundError):
        get_exercises_root()


def test_exercise_success(fixtures_dir):
    epath = os.path.join(fixtures_dir, 'exercise_sample_success.py')
    exercise = Exercise(epath)
    exercise.process()

    assert exercise.error is False
    assert bool(exercise) is True
    assert '[SUCCESS]' in str(exercise)


def test_exercise_to_do(fixtures_dir):
    epath = os.path.join(fixtures_dir, 'exercise_sample_to_do.py')
    exercise = Exercise(epath)
    exercise.process()

    assert exercise.to_do is True
    assert bool(exercise) is True
    assert '[MAKE IT PASS]' in str(exercise)


def test_exercise_fail(fixtures_dir):
    epath = os.path.join(fixtures_dir, 'exercise_sample_fail.py')
    exercise = Exercise(epath)
    exercise.process()

    assert exercise.error is True
    assert bool(exercise) is False
    assert '[ERROR]' in str(exercise)