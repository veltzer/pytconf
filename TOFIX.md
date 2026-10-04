# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pytconf/config.py:374` - `max_free_args` check uses `>=`, so `max_free_args=2` rejects two args (verified: "too many free args - 2 required"); the built-in `help` command (line 289) therefore accepts only one name. Use `>` and fix the message ("at most N allowed").
- `src/pytconf/param.py:111` - `s2t_generate_from_default` calls the generator with `(self.default, s)`, but only `convert_str_to_int_default` takes two args; for list/str/bool/str_or_none params (lines 283, 309, 332, 352, 373, 394) the `=value` edit syntax always fails with "could not convert" (verified for `create_list_str`). Give those params two-arg generators or drop the edit feature for them.

## Medium

- `src/pytconf/color_utils.py:50` - typo `color_warm = identity`; with `PYTCONF_DISABLE_COLORS` set, `color_warn` still emits ANSI codes. Rename to `color_warn`.
- `src/pytconf/param.py:226` - `ParamChoice.s2t` returns any string without checking `choice_list` (verified: `--ch=zzz` accepted); raise on values outside the list.
- `src/pytconf/param.py:444` - `create_existing_folder` / `create_existing_file` (line 423) never check that the path exists - `ParamFilename.s2t` only checks suffixes; validate existence (and `isdir` for folders) or rename them.
- `src/pytconf/config.py:415` - `--flag=value` is rejected when the value contains `=` (verified: `--names=a=b` -> "can not parse argument"), and the `==x` edit form is unreachable; use `real.split("=", 1)`.
- `src/pytconf/config.py:441` - `get_html` lists every registered function under every group instead of `group.names`, so each function is repeated per group; iterate `sorted(group.names)`.
- `pyproject.toml:84` - mypy override sets `ignore_missing_imports` for `pytconf.*`, the package itself, not a stub-less third-party lib as the comment says; a config-level suppression without reason - remove it.

## Low

- `src/pytconf/config.py:236` - `yaml.safe_load` of an empty config file returns `None`, and line 238 then crashes on `.items()`; treat `None` as `{}`.
- `src/pytconf/convert.py:40` - any unrecognised bool string (e.g. `flase`) silently becomes `False`; raise on values outside a known true/false set.
- `src/pytconf/config.py:116` - `version` passed to `register_main` is stored but never used; there is no `--version`/`version` command. Add one or drop the parameter.
- `src/pytconf/data.py:5` - duplicate `LOGGER_NAME` already generated in `static.py`; remove `data.py`.
- `doc/default_issue/Makefile:3` - runs `pylint`, which is not in the dev group or the fleet toolchain; delete the Makefile (the `doc/default_issue/` experiment is superseded by `src/pytconf`).
- `src/pytconf/__init__.py:3` - `# noqa F401` without the colon is a blanket `noqa` to ruff; replace with `__all__`. Docstring on line 1 says "condif".
