import re
import os
from typing import Optional

def set_env_var(env_file_path: str,
                env_var: str,
                env_value: Optional[str] = None) -> None:         
    """Set or clear an environment variable as and export
        in a file to be sourced.
    
    Parameters
    ----------
    env_file_path
        path where export <env_var>=<env_value> will be written
    env_var
        the variable name to be set
    env_value
        the value to be set, or None if the variable is to be erased.
        
    Returns
    -------
        None
    """
    
    if os.path.isfile(env_file_path):
        open_mode = 'r+'
    else:
        open_mode = 'w+'
    
    delete_env = env_value is None
    
    with open(env_file_path, open_mode) as file:
        file.seek(0)
        content = file.read()
        print("Old envs: \n" + content)
        exp_str = "export {0}=".format(env_var)
        set_str = ""
        if not delete_env:
            set_str = exp_str + '"' + env_value + '"'
        if exp_str in content:
            reg_exp = re.compile(exp_str + ".*")
            content = reg_exp.sub(set_str, content)
        else:
            if len(content) > 0: 
                content = content + "\n" + set_str
            else:
                content = set_str
             
        lines = content.splitlines(False)
        file.seek(0)
        print("New envs: ")
        for line in lines:
            if len(line) > 0:
                file.write(line + '\n')
                print(line)    
        file.truncate()
 