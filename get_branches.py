import git
from bag_of_functions import yellow, cyan, green, magenta
import shutil
import os


def step3_is_directory_for_github_or_gitlab(path_to_zap):
    """
    Make sure that 'GITHUB' is in the string.
    This will be used to recuresily delete directories so - you know - 'don't screw up'
    """
    if "GITHUB" in path_to_zap or "GITLAB"in path_to_zap:
        return True
    else:
        return False
    
def step2_isDirectoryExist_andEither_github_or_gitlab(relative_path_to_zap):
    """
    Hard coded the begining path to prevent any accidently mammoth dumbness
    """
    fullpath = f'/Users/pmontgomery/DCP_2023/git_tools/{relative_path_to_zap}'
    okToZap = False
    if os.path.exists(fullpath):
        if step3_is_directory_for_github_or_gitlab(fullpath):
            okToZap = True

    thing_to_zap = {
        "status":okToZap,
        "absPath":fullpath
    }
    return thing_to_zap

def delete_a_directory(relativePath):
    obj = step2_isDirectoryExist_andEither_github_or_gitlab(relativePath)
    directory_path = obj["absPath"]
    reciept = False 
    if obj["status"] == True: 
        try:
            if os.path.exists(directory_path):
                shutil.rmtree(directory_path)
                print(f"Deleted {directory_path} recursively")
                reciept = True 
            else:
                print(f"{directory_path} does not exist")
        except Exception as e:
            print(f"Error deleting {directory_path}: {str(e)}")

    return reciept 

# // # Clone the repository
# // repo = git.Repo.clone_from('https://github.com/mulefish/dispense_version3', '/Users/pmontgomery/DCP_2023/git_tools/GITHUB')  

# // # Get the list of all branches
# // branches = repo.remote().refs

# // # Print the names of all the branches
# // for branch in branches:
# //     cyan(branch.name)


