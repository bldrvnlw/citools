### CITOOLS - python tools

citools is a python package designed to be installed directly from GitHub.

To install :

```
pip install git+https://github.com/bldrvnlw/citools.git#egg=citools
```

#### Available tools

The tools provides a number of functions to support odd cases in CI/CD that have been encountered using Conan build tools to build a separate repo.

##### functions

set_github_commit_status: A wrapper for [/repos/:owner/:repo/statuses/:sha](https://developer.github.com/v3/repos/statuses/)

Example - setting success in a python script:
```
import citools
citools.set_github_commit_status(secret_token, "superorg/superrepo", "a_forty_character_commit_sha", citools.State.success, "https://ci.provider.com/builds/abuildresult", "Just a test", "baldur/testing")
```

Example - setting pending from command line with a build_trigger.json. (Dummy URL)
```
python -c "from githubtools import set_build_status, State; set_build_status('build_trigger.json', 'CONAN_BLDRVNLW_TOKEN', 'https://google.com', 'bldrvnlw/test', State.pending)"
```
Example - setting success from command line with a build_trigger.json. (Dummy URL)
```
python -c "from githubtools import set_build_status, State; set_build_status('build_trigger.json', 'CONAN_BLDRVNLW_TOKEN', 'https://google.com', 'bldrvnlw/test', State.success)"
```
