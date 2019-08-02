# Pydiatra Code Analyzer Plugin for Flake8

[pydiatra](http://jwilk.net/software/pydiatra) ([github](https://github.com/jwilk/pydiatra)) is yet another static checker for Python code.

## Why another static checker

Among other checks pydiatra offers number of regexp checks which are hard to find 
within other analyzers:

* duplicate range (e.g. re.compile("[aa]"))
* overlapping ranges (e.g. re.compile("[a-zA-z]"))
* bad escape sequences (e.g. re.compile(r"\eggs"))
* misplaced inline flags (e.g. re.compile("eggs(?i)"); Python 3.6+ only)
* combining incompatible flags
* redundant flags
* misplaced flags arguments in re.split(), re.sub(), re.subn()

And some other nice to have checks:

* invalid escape sequences in strings (Python 3.6+ only)
* hardcoded errno values (e.g. exc.errno == 2 instead of exc.errno == errno.ENOENT)

## Supported checks

For complete list of implemented checks consult pydiatra page.

Below is list of checks supported by this plugin:

* `PYD001` assertion always true
* `PYD002` async await used as name
* `PYD003` embedded code copy
* `PYD004` except shadows builtin
* `PYD005` bare except
* `PYD006` hardcoded errno value
* `PYD007` inconsistent indentation
* `PYD008` mkstemp file descriptor leak
* `PYD009` obsolete pil import
* `PYD010` py3k compat warning
* `PYD011` regexp bad escape
* `PYD012` regexp duplicate range
* `PYD013` regexp incompatible flags
* `PYD014` regexp misplaced inline flags
* `PYD015` regexp misplaced flags argument
* `PYD016` regexp overlapping ranges
* `PYD017` regexp redundant flag
* `PYD018` regexp syntax error
* `PYD019` regexp syntax warning
* `PYD020` string exception
* `PYD021` string formatting error
* `PYD022` syntax error
* `PYD023` syntax warning
* `PYD024` sys.hexversion comparison
* `PYD025` sys.version comparison

## Flake8 violation classes

This plugin uses `PYD0` as violation class. Add it to flake8's `select` to enable.

```bash
flake8 --select PYD0 .
```
