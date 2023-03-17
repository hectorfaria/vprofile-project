from fabric.api import *

def system_info():
    print("Disk Space")
    local("df -h")
    print("Ram Size")
    local("free -m")
    print("System uptime")
    local("uptime")

def remote_exec():
    print("Get system info")
    run("hostname")
    run("uptime")
    run("df -h")
    run("free -m")


def web_setup(WEBURL,DIRNAME):
    local("apt install zip unzip -y")
    sudo("yum install httpd wget unzip -y")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")
    local(("wget -O website.zip %s") % WEBURL)
    local("unzip -o website.zip")
    with lcd(DIRNAME):
        local("zip -r tooplate.zip *")
        put("tooplate.zip", "/var/www/html", use_sudo=True)
    with cd("/var/www/html/"):
        sudo("unzip -o tooplate.zip")
        sudo("systemctl restart httpd")
        print("done...")