import json
from typing import Tuple

from citools.envtools import set_env_var

def get_build_trigger_info(triggerfile: str,
                            envfile: str = None) -> Tuple[str, str, str, str, str]:

    """ Read four key commit parameters and optionally 
        save them in the environment file.     
        
    Parameters
    ----------
    triggerfile
        the file containing the build trigger json data
        
    envfile
        an optional environment file that can be sourced
        to provide the data as environment variables
        
    Returns
    -------
        tuple containing: 
            commit_id - the SHA of the head commit
            commit_author - the author of the commit
            commit_email - the email of the commit author
            commit_url - the url of the commit on the git server
            commit_repo - the full name of the commit repo
    """
    
    with open(triggerfile) as json_file:
        data = json.load(json_file)
    
    commit_id = data['head_commit']['id']
    commit_author = data['head_commit']['author']['name']
    commit_email = data['head_commit']['author']['email']
    commit_url = data['head_commit']['url']
    commit_repo = data ['repository']['full_name']
    
    if not envfile is None:
        set_env_var(envfile, 'BUILD_COMMIT_ID', commit_id)
        set_env_var(envfile, 'BUILD_COMMIT_AUTHOR', commit_author)
        set_env_var(envfile, 'BUILD_COMMIT_EMAIL', commit_email)
        set_env_var(envfile, 'BUILD_COMMIT_URL', commit_url)
        set_env_var(envfile, 'BUILD_COMMIT_REPO', commit_repo)
    
    return commit_id, commit_author, commit_email, commit_url, commit_repo