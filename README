# getreqt
get requirements tree for installed pip packages

# from a list of packages merged to one requirements.txt (requires changing `--write` option to use append mode `'a'`)
`cat getreqt.list | xargs -I{} getreqt --write {} && awk '!seen[$0]++' requirements.txt > reqs_unique.txt && mv reqs_unique.txt requirements.txt && pip wheel --wheel-dir=. -r requirements.txt`
