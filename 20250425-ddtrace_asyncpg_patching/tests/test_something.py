import logging

from aucampia.issues.ddtrace_asyncpg_patching import package_function


def test_something() -> None:
    logging.info("entry: ...")
    assert package_function() == "value"
