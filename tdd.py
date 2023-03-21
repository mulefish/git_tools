from bag_of_functions import verdict
from get_branches import step2_isDirectoryExist_andEither_github_or_gitlab, delete_a_directory

def step2_isDirectoryExist_andEither_github_or_gitlab_test(): 
    given = {
        "GITHUB":True,
        "GITHUB/static":True,
        "git_tools/GIThUB":False,
        "git_tools/":False,
        "":False,
    }
    isOk = True 

    for path in given:
        expected = given[path]
        obj = step2_isDirectoryExist_andEither_github_or_gitlab(path)
        absPath = obj["absPath"]
        status = obj["status"]
        if path not in absPath or status != expected:
            isOk = False 
    
    verdict(isOk, True, "is_directory_existing_test")

def delete_a_directory_test(): 
    obj = delete_a_directory("GITHUB")

if __name__ == '__main__':
    step2_isDirectoryExist_andEither_github_or_gitlab_test()
    delete_a_directory_test()