# readme file for the cyber-security-stuff branch

This branch includes different tools to exploit vulnerabilities. 
DO NOT USE THEM TO COMMIT CRIME AND ONLY USE THEM ON YOUR OWN DEVICES.


These are the following tools:

cmd-flood-virus.bat -- this is a simple 4 line batch file which will open multiple times the cmd.exe programm.

arpspoofx.py -- arp-spoofing is a well known procedure to prepare a man-in-the-middle attack.

DoS.py -- denial of service script to flood a target with requests. 

keylogger.py -- keylogger is a type of spyware to catch a pressed key and write it into a logfile 'log.txt'. 
                After a specific count of keys which got detected, it will send an email to your prefered account.
                You have to edit the python file and replace the fields [PASSWORD], [EMAIL], [DEST-EMAIL], [NAME],
                [SUBJECT] and [MESSAGE] with your values. 
  
fuzzer.py -- fuzzing is an usually automated technique used to detect implementation bugs in a code. For example 
             buffer overflows
             fuzzer.py is only a piece of code which includes different kinds of fuzzers. An automated testing
             fuzzer to find the right buffer range where the programm crashes, one fuzzer to manually find the
             exact offset of the crash and the last fuzzer helps to exlude bad chars
            
exploit.py -- exploit.py is only an example for an exploit of a buffer overflow vulnerability 

pincracker.zip -- pincracker is a fun tool. It only finds a 4 digit number.

integrity.py -- this tool is only supported for unix-systems yet. It creates a hash of every system path but can 
                be enlarged by the user. 
     
rmsf.py -- after deleting a file it is often possible to restore the file. To avoid restoring sensitive data rmsf.py 
           encrypts a selected file with an one-time-key and deletes it. In case of a restoring the data will be encrypted. 

ultron  -- ultron is a collection of different tools including cyber-security-tools 




