import subprocess
import os, requests, json

username ='#'
password='#'
dow_repos = {}

os.chdir('..')
npm_file = os.path.join(os.getcwd(),'package.json')

#read the json requires and split each dependency at @ if it is github.dowjones.net
with open(npm_file, 'r') as json_data:
    data = json.load(json_data)
    for repo in data['dependencies']:
        if 'dowjones.net' in data['dependencies'][repo]:
            dow_repos[repo] = data['dependencies'][repo].replace("git+ssh://git@","")

#create node_modules
module_dir = os.path.join(os.getcwd(),'node_modules')
if not os.path.exists(module_dir):
    os.makedirs(module_dir)

os.chdir(module_dir)

#clone git repos into node_modules
for repo in dow_repos:
    #new_repo = os.path.join(module_dir, repo)
    #if not os.path.exists(new_repo):
    #    os.makedirs(new_repo)
    cmd = "git clone https://"+username+":"+password+"@"+str(dow_repos[repo])
    print cmd
    subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
