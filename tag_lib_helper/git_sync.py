import subprocess

pull_command = 'git pull'

add_command = 'git add hl_standards_new_tag_v1.3.67.json'

commit_command = 'git commit -m "tag lib update"'

push_command = 'git push'

subprocess.call(pull_command, shell=True)
subprocess.call(add_command, shell=True)
subprocess.call(commit_command, shell=True)
subprocess.call(push_command, shell=True)
