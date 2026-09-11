# tv-sandbox

A disposable sandbox for validating TandemVelocity end to end against real providers.

Nothing here is production code, and the repository is expected to accumulate throwaway branches and pull
requests. Delete it whenever it stops being useful.

## textkit

| Function | Does |
|---|---|
| `slugify(text)` | a lowercase, hyphen-separated URL slug |
| `truncate(text, width)` | text shortened to `width`, the cut marked with `...` |
| `title_case(text)` | each word capitalized |
| `snake_case(text)` | an identifier in snake case |
| `kebab_case(text)` | a lowercase, hyphen-separated identifier |
| `collapse_whitespace(text)` | runs of whitespace collapsed, ends trimmed |
| `fold_accents(text)` | accented letters folded to ASCII |

```python
>>> from textkit import slugify
>>> slugify("Hello World")
'hello-world'
```

Run the unit tests with `pytest -q`. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request: CI
checks more than the unit tests.
