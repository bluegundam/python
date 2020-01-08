import paramiko
import getpass

try:
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    # server = input('Server: ')
    # user = input('Username : ')
    # pwd = getpass.getpass('Password : ')

    server = "192.168.56.1"
    user = "red"
    pwd = "password"

    cli.connect(server, port=22, username=user, password=pwd)
    stdin, stdout, stderr = cli.exec_command('cat /etc/passwd')
    lines = stdout.readlines()
    print(''.join(lines))

    cli.close()

except EOFError as e:
    print(e)