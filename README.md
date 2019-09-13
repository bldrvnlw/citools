### CITOOLS - python tools

citools is a python package designed to be installed directly from GitHub.

To install :

```
pip install git+git://github.com/bldrvnlw/citools.git#egg=citools
```

#### Available tools

The tolls support a number of functions to support odd cases in CI/CD that have been encountered using Conan build tools to build a separate repo.

##### functions

set_github_commit_status: A wrapper for [/repos/:owner/:repo/statuses/:sha](https://developer.github.com/v3/repos/statuses/)
