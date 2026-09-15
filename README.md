# route_tester

A simple, open-source HTTP route testing client for developers — the same job as Postman,
Insomnia or Thunder Client, with one difference: it is built to be driven by an AI coding agent.

The idea is straightforward. Every time you write a new route, you should exercise it by hand
before calling it done — on top of the automated tests. Today that means leaving your editor and
retyping the URL, headers, body and auth into another tool. Your agent already knows all of that.
`route_tester` is designed so it can hand you the request fully prepared, and all you do is press
**Send** and read the response.

> **Status:** early development. The base application is being built first; the agent
> integration comes after.

## Installation

```bash
uv tool install git+https://github.com/LaboraP-D/cerne_route_tester.git
route-tester
```

Run it once without installing:

```bash
uvx --from git+https://github.com/LaboraP-D/cerne_route_tester.git route-tester
```

## Development

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12 or 3.13.

```bash
git clone https://github.com/LaboraP-D/cerne_route_tester.git route_tester
cd route_tester
uv sync
uv run route-tester
```

```bash
uv run pytest                 # tests
uv run ruff check src tests   # lint
```

## Design

The project is split in two, and the split is the whole point:

- **`core/`** — the headless engine: request models, the `requests` wrapper, collections,
  environments and variable interpolation. It never imports Qt, so it can run without a display
  and be driven programmatically.
- **`gui/`** — a thin PySide6 view over `core`. No HTTP logic lives here.

Every request round-trips losslessly through a single JSON document. That document is what an
agent produces to pre-fill the app.

## License

MIT — see [LICENSE](LICENSE).
