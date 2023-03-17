#!/usr/bin/python3
import os

userlist = ["dookie", "ubuntu", "centos"]

for user in userlist:
    exitcode = os.system(f"id {user}")
    if exitcode != 0:
        print("adding user")
        os.system(f"useradd {user}")
    else:
        print(f"{user} exists")

exitcode = os.system("grep admins /etc/group")
if exitcode != 0:
    os.system("groupadd admins")
    print("Adding admins group")
else:
     print("admins group already exists")

for user in userlist:
    print(f"Adding {user} to admin groups")
    os.system(f"usermod -G admins {user}")

if os.path.isdir("/opt/admins_dir"):
    print("admins dir exists.")
else:
    os.mkdir("/opt/admins_dir")

print("Assigning users to the directory...")
os.system("chown :admins /opt/admins_dir")
os.system("chmod 770 /opt/admins_dir")