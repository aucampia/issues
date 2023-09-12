

```console
$ date +%Y%m%d%H%M%S.%N; env | grep '^VAULT_' | grep -v _TOKEN=; time GODEBUG=netdns=go+1 /home/iwana/lw/d.x/github.com/hashicorp/vault/vault.bin token lookup >/dev/null; date +%Y%m%d%H%M%S.%N;
20230912083255.923021794
VAULT_CACERT=/run/user/1000/opt/kron-cluster-sandbox/certs/vault_int-ca.pem
VAULT_ADDR=https://sandbox-server.local:8200
go package net: GODEBUG setting forcing use of Go's resolver

real	0m10.078s
user	0m0.067s
sys	0m0.033s
20230912083306.009492309
```

```console
$ date +%Y%m%d%H%M%S.%N; env | grep '^VAULT_' | grep -v _TOKEN=; time GODEBUG=netdns=cgo+1 /home/iwana/lw/d.x/github.com/hashicorp/vault/vault.bin token lookup >/dev/null; date +%Y%m%d%H%M%S.%N;
20230912083936.086708807
VAULT_CACERT=/run/user/1000/opt/kron-cluster-sandbox/certs/vault_int-ca.pem
VAULT_ADDR=https://sandbox-server.local:8200
go package net: using cgo DNS resolver

real	0m0.185s
user	0m0.059s
sys	0m0.037s
20230912083936.282172446
```
