Poetry ignores pre-release preference when doing upgrade. Below is
output which shows poetry upgrading dbt to a pre-release version when an
upgrade of sqlplus is requested (see `Updating dbt-core (1.5.2 -> 1.6.0b8)`).


```console
$ docker compose build
[... elided ...]

#15 [check check 1/6] RUN echo MARK-000
#15 0.167 MARK-000
#15 DONE 0.2s

#16 [check check 2/6] COPY poetry.lock pyproject.toml /var/tmp/project/
#16 DONE 0.1s

#17 [check check 3/6] WORKDIR /var/tmp/project
#17 DONE 0.1s

#18 [check check 4/6] RUN     poetry install &&     poetry show --tree &&     true
#18 0.438 Creating virtualenv example-DUsXTPpF-py3.11 in /root/.cache/pypoetry/virtualenvs
#18 0.790 Installing dependencies from lock file
#18 0.900
#18 0.900 Package operations: 45 installs, 0 updates, 0 removals
#18 0.900
#18 0.900   • Installing attrs (23.1.0)
#18 0.901   • Installing rpds-py (0.8.10)
#18 1.283   • Installing referencing (0.29.1)
#18 1.334   • Installing certifi (2023.5.7)
#18 1.335   • Installing charset-normalizer (3.2.0)
#18 1.335   • Installing idna (3.4)
#18 1.335   • Installing future (0.18.3)
#18 1.336   • Installing jsonschema-specifications (2023.6.1)
#18 1.363   • Installing six (1.16.0)
#18 1.364   • Installing text-unidecode (1.3)
#18 1.365   • Installing urllib3 (2.0.3)
#18 2.824   • Installing babel (2.12.1)
#18 2.825   • Installing isodate (0.6.1)
#18 2.825   • Installing jsonschema (4.18.2)
#18 2.826   • Installing leather (0.3.4)
#18 2.826   • Installing markupsafe (2.1.3)
#18 2.827   • Installing msgpack (1.0.5)
#18 2.828   • Installing parsedatetime (2.4)
#18 2.828   • Installing pycparser (2.21)
#18 2.829   • Installing python-dateutil (2.8.2)
#18 2.830   • Installing python-slugify (8.0.1)
#18 2.831   • Installing pytimeparse (1.1.8)
#18 2.832   • Installing requests (2.31.0)
#18 2.833   • Installing typing-extensions (4.7.1)
#18 3.015 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 3.022 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 3.043 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 3.769   • Installing agate (1.7.0)
#18 3.770   • Installing cffi (1.15.1)
#18 3.771   • Installing click (8.1.4)
#18 3.772   • Installing colorama (0.4.6)
#18 3.773   • Installing dbt-extractor (0.4.1)
#18 3.773   • Installing hologram (0.0.16)
#18 3.774   • Installing jinja2 (3.1.2)
#18 3.775   • Installing logbook (1.5.3)
#18 3.776   • Installing mashumaro (3.6)
#18 3.777   • Installing minimal-snowplow-tracker (0.0.2)
#18 3.778   • Installing networkx (2.8.8)
#18 3.778   • Installing packaging (23.1)
#18 3.779   • Installing pathspec (0.11.1)
#18 3.779   • Installing protobuf (4.23.4)
#18 3.781   • Installing pytz (2023.3)
#18 3.782   • Installing pyyaml (6.0)
#18 3.782   • Installing sqlparse (0.4.3)
#18 3.783   • Installing werkzeug (2.3.6)
#18 3.997 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 4.002 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 4.006 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 4.010 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 4.012 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 4.016 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 4.024 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 4.029 Connection pool is full, discarding connection: pypi.org. Connection pool size: 10
#18 5.044   • Installing dbt-core (1.5.2)
#18 5.045   • Installing psycopg2-binary (2.9.6)
#18 5.353   • Installing dbt-postgres (1.5.2)
#18 5.834 dbt-postgres 1.5.2 The postgres adapter plugin for dbt (data build tool)
#18 5.834 ├── dbt-core 1.5.2
#18 5.834 │   ├── agate >=1.6,<1.7.1
#18 5.834 │   │   ├── babel >=2.0
#18 5.834 │   │   ├── isodate >=0.5.4
#18 5.834 │   │   │   └── six *
#18 5.834 │   │   ├── leather >=0.3.2
#18 5.834 │   │   │   └── six >=1.6.1 (circular dependency aborted here)
#18 5.834 │   │   ├── parsedatetime >=2.1,<2.5 || >2.5,<2.6 || >2.6
#18 5.834 │   │   │   └── future *
#18 5.834 │   │   ├── python-slugify >=1.2.1
#18 5.834 │   │   │   └── text-unidecode >=1.3
#18 5.834 │   │   └── pytimeparse >=1.1.5
#18 5.834 │   ├── cffi >=1.9,<2.0.0
#18 5.834 │   │   └── pycparser *
#18 5.834 │   ├── click >=7.0,<9
#18 5.834 │   │   └── colorama *
#18 5.834 │   ├── colorama >=0.3.9,<0.4.7 (circular dependency aborted here)
#18 5.834 │   ├── dbt-extractor >=0.4.1,<0.5.0
#18 5.834 │   ├── hologram >=0.0.14,<=0.0.16
#18 5.835 │   │   ├── jsonschema >=3.0
#18 5.835 │   │   │   ├── attrs >=22.2.0
#18 5.835 │   │   │   ├── jsonschema-specifications >=2023.03.6
#18 5.835 │   │   │   │   └── referencing >=0.28.0
#18 5.835 │   │   │   │       ├── attrs >=22.2.0 (circular dependency aborted here)
#18 5.835 │   │   │   │       └── rpds-py >=0.7.0
#18 5.835 │   │   │   ├── referencing >=0.28.4 (circular dependency aborted here)
#18 5.835 │   │   │   └── rpds-py >=0.7.1 (circular dependency aborted here)
#18 5.835 │   │   └── python-dateutil >=2.8,<2.9
#18 5.835 │   │       └── six >=1.5 (circular dependency aborted here)
#18 5.835 │   ├── idna >=2.5,<4
#18 5.835 │   ├── isodate >=0.6,<0.7 (circular dependency aborted here)
#18 5.835 │   ├── jinja2 3.1.2
#18 5.835 │   │   └── markupsafe >=2.0
#18 5.835 │   ├── logbook >=1.5,<1.6
#18 5.835 │   ├── mashumaro 3.6
#18 5.835 │   │   ├── msgpack >=0.5.6
#18 5.835 │   │   └── typing-extensions >=4.1.0
#18 5.835 │   ├── minimal-snowplow-tracker 0.0.2
#18 5.835 │   │   ├── requests >=2.2.1,<3.0
#18 5.835 │   │   │   ├── certifi >=2017.4.17
#18 5.835 │   │   │   ├── charset-normalizer >=2,<4
#18 5.835 │   │   │   ├── idna >=2.5,<4 (circular dependency aborted here)
#18 5.835 │   │   │   └── urllib3 >=1.21.1,<3
#18 5.835 │   │   └── six >=1.9.0,<2.0 (circular dependency aborted here)
#18 5.835 │   ├── networkx >=2.3,<3
#18 5.835 │   ├── packaging >20.9
#18 5.835 │   ├── pathspec >=0.9,<0.12
#18 5.835 │   ├── protobuf >=4.0.0
#18 5.835 │   ├── pytz >=2015.7
#18 5.835 │   ├── pyyaml >=6.0
#18 5.835 │   ├── requests <3.0.0 (circular dependency aborted here)
#18 5.835 │   ├── sqlparse >=0.2.3,<0.4.4
#18 5.835 │   ├── typing-extensions >=3.7.4 (circular dependency aborted here)
#18 5.835 │   └── werkzeug >=1,<3
#18 5.835 │       └── markupsafe >=2.1.1 (circular dependency aborted here)
#18 5.835 └── psycopg2-binary >=2.8,<3.0
#18 5.835 sqlparse 0.4.3 A non-validating SQL parser.
#18 DONE 6.6s

#19 [check check 5/6] RUN     poetry update sqlparse &&     poetry show --tree &&     true
#19 0.687 Updating dependencies
#19 0.689 Resolving dependencies...
#19 8.362
#19 8.362 Package operations: 6 installs, 8 updates, 4 removals
#19 8.362
#19 8.362   • Removing jsonschema-specifications (2023.6.1)
#19 9.066   • Removing referencing (0.29.1)
#19 9.364   • Removing rpds-py (0.8.10)
#19 9.659   • Removing werkzeug (2.3.6)
#19 9.996   • Installing pyrsistent (0.19.3)
#19 9.996   • Updating setuptools (67.8.0 -> 68.0.0)
#19 9.997   • Updating typing-extensions (4.7.1 -> 4.6.3)
#19 9.997   • Updating urllib3 (2.0.3 -> 1.26.16)
#19 9.998   • Installing zipp (3.16.1)
#19 10.61   • Installing importlib-metadata (6.6.0)
#19 10.61   • Updating jsonschema (4.18.2 -> 3.2.0)
#19 10.61   • Installing more-itertools (8.10.0)
#19 10.62   • Installing pydantic (1.10.11)
#19 10.97   • Installing dbt-semantic-interfaces (0.1.0.dev8)
#19 10.97   • Updating mashumaro (3.6 -> 3.8.1)
#19 10.97   • Updating sqlparse (0.4.3 -> 0.4.4)
#19 11.42   • Updating dbt-core (1.5.2 -> 1.6.0b8)
#19 12.01   • Updating dbt-postgres (1.5.2 -> 1.6.0b8)
#19 12.80
#19 12.80 Writing lock file
#19 13.24 dbt-postgres 1.6.0b8 The postgres adapter plugin for dbt (data build tool)
#19 13.24 ├── agate *
#19 13.24 │   ├── babel >=2.0
#19 13.24 │   ├── isodate >=0.5.4
#19 13.24 │   │   └── six *
#19 13.24 │   ├── leather >=0.3.2
#19 13.24 │   │   └── six >=1.6.1 (circular dependency aborted here)
#19 13.24 │   ├── parsedatetime >=2.1,<2.5 || >2.5,<2.6 || >2.6
#19 13.24 │   │   └── future *
#19 13.24 │   ├── python-slugify >=1.2.1
#19 13.24 │   │   └── text-unidecode >=1.3
#19 13.24 │   └── pytimeparse >=1.1.5
#19 13.24 ├── dbt-core 1.6.0b8
#19 13.24 │   ├── agate >=1.7.0,<1.8.0
#19 13.24 │   │   ├── babel >=2.0
#19 13.24 │   │   ├── isodate >=0.5.4
#19 13.24 │   │   │   └── six *
#19 13.24 │   │   ├── leather >=0.3.2
#19 13.24 │   │   │   └── six >=1.6.1 (circular dependency aborted here)
#19 13.24 │   │   ├── parsedatetime >=2.1,<2.5 || >2.5,<2.6 || >2.6
#19 13.24 │   │   │   └── future *
#19 13.24 │   │   ├── python-slugify >=1.2.1
#19 13.24 │   │   │   └── text-unidecode >=1.3
#19 13.24 │   │   └── pytimeparse >=1.1.5
#19 13.24 │   ├── cffi >=1.9,<2.0.0
#19 13.24 │   │   └── pycparser *
#19 13.24 │   ├── click >=7.0,<9
#19 13.24 │   │   └── colorama *
#19 13.24 │   ├── colorama >=0.3.9,<0.5 (circular dependency aborted here)
#19 13.24 │   ├── dbt-extractor >=0.4.1,<0.5.0
#19 13.24 │   ├── dbt-semantic-interfaces 0.1.0.dev8
#19 13.24 │   │   ├── click >=7.1.2 (circular dependency aborted here)
#19 13.24 │   │   ├── importlib-metadata 6.6.0
#19 13.24 │   │   │   └── zipp >=0.5
#19 13.24 │   │   ├── jinja2 3.1.2
#19 13.24 │   │   │   └── markupsafe >=2.0
#19 13.24 │   │   ├── jsonschema 3.2.0
#19 13.24 │   │   │   ├── attrs >=17.4.0
#19 13.24 │   │   │   ├── pyrsistent >=0.14.0
#19 13.24 │   │   │   ├── setuptools *
#19 13.24 │   │   │   └── six >=1.11.0 (circular dependency aborted here)
#19 13.24 │   │   ├── more-itertools 8.10.0
#19 13.24 │   │   ├── pydantic >=1.10.8,<1.11.0
#19 13.24 │   │   │   └── typing-extensions >=4.2.0
#19 13.24 │   │   ├── python-dateutil 2.8.2
#19 13.24 │   │   │   └── six >=1.5 (circular dependency aborted here)
#19 13.24 │   │   ├── pyyaml >=6.0,<7.0
#19 13.24 │   │   └── typing-extensions >=4.6.1,<4.7.0 (circular dependency aborted here)
#19 13.24 │   ├── hologram >=0.0.16,<0.1.0
#19 13.24 │   │   ├── jsonschema >=3.0 (circular dependency aborted here)
#19 13.24 │   │   └── python-dateutil >=2.8,<2.9 (circular dependency aborted here)
#19 13.24 │   ├── idna >=2.5,<4
#19 13.24 │   ├── isodate >=0.6,<0.7 (circular dependency aborted here)
#19 13.24 │   ├── jinja2 >=3.1.2,<3.2.0 (circular dependency aborted here)
#19 13.24 │   ├── logbook >=1.5,<1.6
#19 13.24 │   ├── mashumaro >=3.8.1,<3.9.0
#19 13.24 │   │   ├── msgpack >=0.5.6
#19 13.24 │   │   └── typing-extensions >=4.1.0 (circular dependency aborted here)
#19 13.24 │   ├── minimal-snowplow-tracker >=0.0.2,<0.1.0
#19 13.24 │   │   ├── requests >=2.2.1,<3.0
#19 13.24 │   │   │   ├── certifi >=2017.4.17
#19 13.24 │   │   │   ├── charset-normalizer >=2,<4
#19 13.24 │   │   │   ├── idna >=2.5,<4 (circular dependency aborted here)
#19 13.24 │   │   │   └── urllib3 >=1.21.1,<3
#19 13.24 │   │   └── six >=1.9.0,<2.0 (circular dependency aborted here)
#19 13.24 │   ├── networkx >=2.3,<4
#19 13.24 │   ├── packaging >20.9
#19 13.24 │   ├── pathspec >=0.9,<0.12
#19 13.24 │   ├── protobuf >=4.0.0
#19 13.24 │   ├── pytz >=2015.7
#19 13.24 │   ├── pyyaml >=6.0 (circular dependency aborted here)
#19 13.24 │   ├── requests <3.0.0 (circular dependency aborted here)
#19 13.24 │   ├── sqlparse >=0.2.3
#19 13.24 │   ├── typing-extensions >=3.7.4 (circular dependency aborted here)
#19 13.24 │   └── urllib3 >=1.0,<2.0 (circular dependency aborted here)
#19 13.24 └── psycopg2-binary >=2.8,<3.0
#19 13.24 sqlparse 0.4.4 A non-validating SQL parser.
#19 DONE 13.5s

#20 [check check 6/6] RUN     set -x &&     poetry show dbt-core &&     poetry run dbt --version &&     DBT_VERSION=$(tomlq -r '.package[] | select( .name == "dbt-core" ) | .version' poetry.lock) &&     1>&2 echo "Check that dbt ${DBT_VERSION} is not a pre-release version" &&     ! { echo "${DBT_VERSION}" | grep -E -- '[ab][0-9]$'; } &&     true
#20 0.299 + poetry show dbt-core
#20 0.625  name         : dbt-core
#20 0.625  version      : 1.6.0b8
#20 0.625  description  : With dbt, data analysts and engineers can build analytics the way engineers build applications.
#20 0.625
#20 0.625 dependencies
#20 0.625  - agate >=1.7.0,<1.8.0
#20 0.625  - cffi >=1.9,<2.0.0
#20 0.625  - click >=7.0,<9
#20 0.625  - colorama >=0.3.9,<0.5
#20 0.625  - dbt-extractor >=0.4.1,<0.5.0
#20 0.625  - dbt-semantic-interfaces 0.1.0.dev8
#20 0.625  - hologram >=0.0.16,<0.1.0
#20 0.625  - idna >=2.5,<4
#20 0.625  - isodate >=0.6,<0.7
#20 0.625  - Jinja2 >=3.1.2,<3.2.0
#20 0.625  - logbook >=1.5,<1.6
#20 0.625  - mashumaro >=3.8.1,<3.9.0
#20 0.625  - minimal-snowplow-tracker >=0.0.2,<0.1.0
#20 0.625  - networkx >=2.3,<4
#20 0.625  - packaging >20.9
#20 0.625  - pathspec >=0.9,<0.12
#20 0.625  - protobuf >=4.0.0
#20 0.625  - pytz >=2015.7
#20 0.625  - pyyaml >=6.0
#20 0.625  - requests <3.0.0
#20 0.625  - sqlparse >=0.2.3
#20 0.625  - typing-extensions >=3.7.4
#20 0.625  - urllib3 >=1.0,<2.0
#20 0.625
#20 0.625 required by
#20 0.625  - dbt-postgres 1.6.0b8
#20 0.665 + poetry run dbt --version
#20 3.266 Core:
#20 3.266   - installed: 1.6.0-b8
#20 3.266   - latest:    1.5.2    - Ahead of latest version!
#20 3.266
#20 3.266 Plugins:
#20 3.266   - postgres: 1.6.0b8 - Ahead of latest version!
#20 3.266
#20 3.266
#20 3.431 ++ tomlq -r '.package[] | select( .name == "dbt-core" ) | .version' poetry.lock
#20 3.816 + DBT_VERSION=1.6.0b8
#20 3.816 + echo 'Check that dbt 1.6.0b8 is not a pre-release version'
#20 3.816 Check that dbt 1.6.0b8 is not a pre-release version
#20 3.817 + echo 1.6.0b8
#20 3.817 + grep -E -- '[ab][0-9]$'
#20 3.818 1.6.0b8
#20 ERROR: process "/bin/bash -o pipefail -c set -x &&     poetry show dbt-core &&     poetry run dbt --version &&     DBT_VERSION=$(tomlq -r '.package[] | select( .name == \"dbt-core\" ) | .version' poetry.lock) &&     1>&2 echo \"Check that dbt ${DBT_VERSION} is not a pre-release version\" &&     ! { echo \"${DBT_VERSION}\" | grep -E -- '[ab][0-9]$'; } &&     true" did not complete successfully: exit code: 1
------
 > [check check 6/6] RUN     set -x &&     poetry show dbt-core &&     poetry run dbt --version &&     DBT_VERSION=$(tomlq -r '.package[] | select( .name == "dbt-core" ) | .version' poetry.lock) &&     1>&2 echo "Check that dbt ${DBT_VERSION} is not a pre-release version" &&     ! { echo "${DBT_VERSION}" | grep -E -- '[ab][0-9]$'; } &&     true:
3.266   - postgres: 1.6.0b8 - Ahead of latest version!
3.266
3.266
3.431 ++ tomlq -r '.package[] | select( .name == "dbt-core" ) | .version' poetry.lock
3.816 + DBT_VERSION=1.6.0b8
3.816 + echo 'Check that dbt 1.6.0b8 is not a pre-release version'
3.816 Check that dbt 1.6.0b8 is not a pre-release version
3.817 + echo 1.6.0b8
3.817 + grep -E -- '[ab][0-9]$'
3.818 1.6.0b8
------
failed to solve: process "/bin/bash -o pipefail -c set -x &&     poetry show dbt-core &&     poetry run dbt --version &&     DBT_VERSION=$(tomlq -r '.package[] | select( .name == \"dbt-core\" ) | .version' poetry.lock) &&     1>&2 echo \"Check that dbt ${DBT_VERSION} is not a pre-release version\" &&     ! { echo \"${DBT_VERSION}\" | grep -E -- '[ab][0-9]$'; } &&     true" did not complete successfully: exit code: 1

```
