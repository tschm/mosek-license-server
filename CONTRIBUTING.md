# Contributing to mosek-license-server

This document is a guide to contributing to mosek-license-server

We welcome all contributions. You don't need to be an expert (in optimization)
to help out.

## Checklist

Contributions are made through
[pull requests](https://help.github.com/articles/using-pull-requests/).
Before sending a pull request, make sure you do the following:

- Run 'task mosek:fmt' to make sure your code adheres to our [coding style](#code-style).
  This step also includes our license on top of your new files.

## Building mosek-license-server from source

Please install [task](https://taskfile.dev).

You'll need to build mosek-license-server locally in order to start editing code.
To install mosek-license-server from source, clone the Github
repository, navigate to its root, and run the following command:

```bash
task mosek:install
```

We assume you have [poetry](https://python-poetry.org) installed.

## Contributing code

To contribute to mosek-license-server, send us pull requests.
For those new to contributing, check out Github's
[guide](https://help.github.com/articles/using-pull-requests/).

Once you've made your pull request, a member of the mosek-license-server
development team will assign themselves to review it. You might have a few
back-and-forths with your reviewer before it is accepted, which is completely normal.
Your pull request will trigger continuous integration tests for many different
Python versions and different platforms. If these tests start failing, please
fix your code and send another commit, which will re-trigger the tests.

If you'd like to add a new feature to mosek-license-server, please do propose your
change on a Github issue, to make sure that your priorities align with ours.

If you'd like to contribute code but don't know where to start, try one of the
following:

- Read the mosek-license-server source and enhance the documentation,
  or address TODOs
- Browse the [issue tracker](https://github.com/tschm/mosek-license-server/issues),
  and look for the issues tagged "help wanted".

## License

A license is added to new files automatically as a pre-commit hook.

## Code style

We use black and ruff to enforce our Python coding style.
Before sending us a pull request, navigate to the project root
and run

```bash
task mosek:fmt
```

to make sure that your changes abide by our style conventions. Please fix any
errors that are reported before sending the pull request.
