# show psk on windows
netsh wlan show profile <input-profile> key=clear

# show psk on linux
cat /etc/NetworkManager/system-connections/<input-profile>
