### poc



- vulserver
    + test on Debian Jessie amd64
    + run vulserver
    + run nc -vv -l -p  4444  in localhost                       
    + run client.py shellcode (now the tcp reverse shellcode link to 127.0.0.1)
 
- vullocal
    + the shellcode now can run in stack 
        - -fno-stack-protector -z execstack
        - echo 0 > /proc/sys/kernel/randomize_va_space
    + the rop shellcode is ok now
        - -fno-stack-protector
        - echo 0 > /proc/sys/kernel/randomize_va_space  
        - ropper --file vullocal --search "% ?di"
        - testing via (cat in.txt ; cat) |  ../bin/vullocal
