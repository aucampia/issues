

```bash
task example:parallel --output group \
  --output-group-begin '::group::{{.TASK}}' \
  --output-group-end '::endgroup::' 2>&1
```
