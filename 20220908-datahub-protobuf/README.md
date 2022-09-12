# ...

```bash
# ensure that DATAHUB_TOKEN and DATAHUB_API is set

# build image
docker compose build
# publish metadata to datahub
docker compose run --rm devtools make publish
#
docker compose run --rm devtools bash -c 'jbang info classpath --catalog=jbang-catalog.json datahub-protobuf | tr ":" "\n" | xargs -n1 -t bsdtar -tvf | grep slf4j'
```
