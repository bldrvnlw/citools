from enum import Enum
from github import Github

class State(Enum):
    error: 0
    failure: 1
    pending: 2
    success: 3
 
def set_github_commit_status(token: str, 
                             repo:str, 
                             commit_id: str, 
                             state: State,
                             target_url: str,
                             description: str, 
                             context: str) -> None:
    """
    Parameters
    ----------
    token 
        access token for the repo 
    repo
        repo the two part repo name: org/repo
    commit_id
        40 character commit sha
    state
        one of the 4 job states
    target_url
        a url pointing to the CI system build output
    description
        a short description of the status
    context
        the reporting system context
        
    Returns
    -------
        True if the status was changed
        False if the change failed for any reason
    
    """
    
    g = Github(token)
    repo = g.get_repo(repo)
    commit = repo.get_commit(commit_id)
    commit.create_status(state.name, target_url, description, context)

    
    