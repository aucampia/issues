import logging
import os
import sys

logging.basicConfig(
    level=os.environ.get("PYTHON_LOGGING_LEVEL", logging.INFO),
    stream=sys.stderr,
    datefmt="%Y-%m-%dT%H:%M:%S",
    format=(
        "%(asctime)s.%(msecs)03d %(process)d %(thread)d %(levelno)03d:%(levelname)-8s "
        "%(name)-12s %(module)s:%(lineno)s:%(funcName)s %(message)s"
    ),
)


class SomeClass:
    type = ""


def black_likes_this():
    input = sys.argv[1] if len(sys.argv) > 1 else ""
    match input + SomeClass.type:
        case "SECRET":
            logging.info("YOU GOT IT")
        case _:
            logging.info("TRY AGAIN")


def black_does_not_like_this():
    input = sys.argv[1] if len(sys.argv) > 1 else ""
    match (input + SomeClass.type):
        case "SECRET":
            logging.info("YOU GOT IT")
        case _:
            logging.info("TRY AGAIN")


if __name__ == "__main__":
    black_likes_this()
    black_does_not_like_this()
