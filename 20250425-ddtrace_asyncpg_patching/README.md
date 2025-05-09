# ...

```bash
poetry install
poetry run aucampia.issues.ddtrace_asyncpg_patching-cli


task help
task validate:fix validate

```

## Using docker devtools

```bash
make -C devtools -B
docker compose build


docker compose run --rm python-devtools task help
docker compose run --rm python-devtools task validate:fix validate

```

## Updating from template base

```bash
pipx run --spec=cruft cruft update
```



```bash
export PGPORT=39432 PGUSER=postgres PGPASSWORD=postgres

# Okay
DDTRACE_ENABLE= POOL_CONNECT_DEFAULT= uv run reproduce.py

# Fails
DDTRACE_ENABLE=true POOL_CONNECT_DEFAULT= uv run reproduce.py

# Also Okay
DDTRACE_ENABLE=true POOL_CONNECT_DEFAULT=true uv run reproduce.py
```

```console
$ DDTRACE_ENABLE= POOL_CONNECT_DEFAULT= poetry run python src/aucampia/issues/ddtrace_asyncpg_patching/patched.py
2025-05-09T11:38:23.054 905922 135979696965440 020:INFO     root         patched:33:main Result: result = [<Record ?column?=1>]

```
