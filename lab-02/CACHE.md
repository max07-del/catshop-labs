# Cache

`actions/setup-python` with `cache: pip`, keyed on the hash of `lab-02/requirements*.txt`.

| Run | Cache | pip install |
|---|---|---|
| cold (first run, no cache) | miss | 6 s |
| warm (next run) | hit | 3 s |

The pip download step got faster because packages come from the Actions cache instead of PyPI; with only four dependencies the saving is small (about 3 s).