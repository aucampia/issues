import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import pytest
from attr import dataclass
from nomad_event_ingestor import EventConverter
from nomad_event_ingestor.util import (
    _guess_env,
    camel_to_snake_case,
    job_id_tags,
)
