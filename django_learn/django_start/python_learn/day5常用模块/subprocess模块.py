import subprocess
# retcode = subprocess.call(['ls','-l'])
# subprocess.run('ls')
# p = subprocess.Popen('find / -size +100000 -exec ls -shl {} \;',shell=True,
#                      stdout=subprocess.PIPE)
# print(p.stdout.read())

# subprocess.run(...)

# obj = subprocess.Popen(['python'],stdin=subprocess.PIPE,
#                        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# obj.stdin.write('print 1 \n')
# obj.stdin.write('print 2 \n')
# obj.stdin.write('print 3 \n')
# obj.stdin.write('print 4 \n')
# out_error_list = obj.communicate(timeout=10)
# print(out_error_list)

def mypass():
    mypass = 'lee123'
    return mypass

echo = subprocess.Popen(['echo',mypass()],stdout=subprocess.PIPE,)

sudo = subprocess.Popen(['sudo','-S','iptables','-L'],stdin=echo.stdout,
                        stdout=subprocess.PIPE,)
end_of_pipe = sudo.stdout
print ("Password ok \n Iptables Chains %s") % end_of_pipe.read()