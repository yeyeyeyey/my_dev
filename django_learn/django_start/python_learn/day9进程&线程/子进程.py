import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

# 如果子进程还需要输入，则可以通过communicate()方法输入：
print('$ nslookup')

p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)
# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：

