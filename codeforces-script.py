import os
import subprocess

curr_dir = (f"/home/starvader/ashutosh_workspace/cp_ws/codeforces/codeforces_code")
print(curr_dir)
target_dir = "/home/starvader/ashutosh_workspace/git_ws/github/CPP-Practice/Codeforces_Solution"

for root,dirs,files in os.walk(curr_dir):
    for file_list in files:
        temp_file = file_list.strip(".cpp")
        command = (f"mkdir {target_dir}/{temp_file}")
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        command1 = (f"cp {curr_dir}/{file_list} {target_dir}/{temp_file}/")
        result = subprocess.run(command1, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        command3 = (f"chmod a+rwx {target_dir}/{temp_file}")
        result = subprocess.run(command3, stdout=subprocess.PIPE, shell=True, universal_newlines=True)     

command4 = (f"date")
result = subprocess.run(command4, stdout=subprocess.PIPE, shell=True, universal_newlines=True)     
print(result.stdout)
