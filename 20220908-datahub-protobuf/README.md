# ...

```bash
# ensure that DATAHUB_TOKEN and DATAHUB_API is set

# build image
docker compose build
# publish metadata to datahub
docker compose run --rm devtools make publish

docker compose run --rm devtools bash -c 'jbang info classpath --catalog=jbang-catalog.json datahub-protobuf | tr ":" "\\000" | xargs -0 -n1 -t bsdtar -tvf | grep slf4j'

```


```console
$ docker compose run --rm devtools make publish
find proto/ -name '*.proto' -type f -print0 \
	| DATAHUB_ENV=EI xargs -0 -t -I{} \
	jbang run --catalog=jbang-catalog.json datahub-protobuf var/generated/main.dsc {}
jbang run '--catalog=jbang-catalog.json' datahub-protobuf var/generated/main.dsc proto/example/greeter/v1/greeter.proto
[jbang] Resolving dependencies...
[jbang] org.slf4j:slf4j-simple:jar:1.7.30
         io.acryl:datahub-client:jar:0.8.44
         com.google.protobuf:protobuf-java:jar:3.19.3
         org.jgrapht:jgrapht-core:jar:1.5.1
         com.google.guava:guava:jar:27.0.1-jre
         com.google.code.gson:gson:jar:2.8.6
Done
[jbang] Dependencies resolved
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
jbang run '--catalog=jbang-catalog.json' datahub-protobuf var/generated/main.dsc proto/io/cloudevents/v1/cloudevents.proto
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
```


## jbang bug

```
curl --silent -L https://github.com/aucampia/issues/archive/heads/main.tar.gz | tar --strip-components 1 --wildcards -zxvf - -C /var/tmp/ '*/20220908-datahub-protobuf/'
(cd /var/tmp/20220908-datahub-protobuf/ && docker compose run --rm devtools jbang info classpath --verbose --catalog=jbang-catalog.json datahub-protobuf)
```
