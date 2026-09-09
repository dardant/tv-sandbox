# tv-sandbox

A disposable sandbox for validating the TandemVelocity delivery slice end to end against real providers.

Nothing here is production code, and the repository is expected to accumulate throwaway branches and pull
requests. Delete it whenever it stops being useful.

`textkit.slugify` turns a title into a URL slug.

```python
>>> from textkit import slugify
>>> slugify("Hello World")
'hello-world'
```

Run the suite with `pytest -q`.
