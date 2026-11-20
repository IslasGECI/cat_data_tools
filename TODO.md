# Backlog

- [ ] Fix the `make mutants` gate: the final `expr "{mutmut results | wc -l}" == "0"` compares a literal string, so the target exits 1 even when no mutant survives (`Makefile`).
- [ ] Add a `.gitignore` for `__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.mutmut-cache`, `coverage.xml`, and the artifacts tests never delete (`tests/data/traps_info_updated.csv`, `tests/posterior_samples_summary.json`).
- [ ] Tag `v1.5.0`: `__version__` and `CHANGELOG.md` say 1.5.0 but `git tag` stops at `v1.4.0`, so tag-based diffs skip a release.
- [ ] Pin the versions of the development tools installed in `Dockerfile` (black, flake8, mypy, mutmut, pylint) so a fresh CI image cannot break `make check` on its own.
- [ ] Pin the revision of `mvillasante/opencode_agents` cloned in `Dockerfile.dev` instead of tracking its default branch.
