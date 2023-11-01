import subprocess

def git_pull_push(version):

    if version is None:
        print('업데이트 사항이 없습니다.')
    else:
        print(f'업데이트 사항이 있습니다. version : {version}')

    pull_command = 'git pull'
    subprocess.call(pull_command, shell=True)

    add_command = f'git add ./lib_lib/hl_standards_new_tag_v{version}.json'
    subprocess.call(add_command, shell=True)

    add_command = 'git add ./hl_standards_new_tag.json'
    subprocess.call(add_command, shell=True)

    commit_command = 'git commit -m "tag lib update"'
    subprocess.call(commit_command, shell=True)

    push_command = 'git push'
    subprocess.call(push_command, shell=True)

if __name__=='__main__':
    git_pull_push()