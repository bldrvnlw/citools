import os
from enum import Enum
from github import Github
from citools.buildtriggertools import get_build_trigger_info

class State(Enum):
    error = 0
    failure = 1
    pending = 2
    success = 3
 
def set_github_commit_status(token: str, 
                             repo:str, 
                             commit_id: str, 
                             state: State,
                             target_url: str,
                             description: str, 
                             context: str) -> None:
    """
    Set the server status for a git commit for a build system.
    
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
        None
    
    """
    
    g = Github(token)
    repo = g.get_repo(repo)
    commit = repo.get_commit(commit_id)
    commit.create_status(state.name, target_url, description, context)

    
def set_build_status(triggerfile: str, 
                      token: str, 
                      target_url: str,
                      context: str,
                      status: State) -> None:

    """ Set the original commit status, as specified in the triggerfile
        that contains the webhook data, to pending. Use the access_token_var
        to retrieve the access token"
        
    Parameters
    ----------
    triggerfile 
        path to the build trigger json
    
    token
        the access token value
        
    target_url
        link to CI result
        
    context
        context string groups the statuses
        
    Returns
    -------
    None
    """
        
    commit_id, commit_author, commit_email, commit_url, commit_repo = get_build_trigger_info(triggerfile)
    
    set_github_commit_status(
        token, 
        commit_repo, 
        commit_id, 
        status,
        target_url,
        "Using separate build repo",
        context)
        
        
    