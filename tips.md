# For installing and setting Selenium in the environmet
sudo apt-get install python3-pip -y
sudo apt-get install -y chromium-browser
pip3 install -U selenium

wget https://chromedriver.storage.googleapis.com/105.0.5195.52/chromedriver_linux64.zip && \
unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip

# For understand Custom Logs
videos para entender custom logs

https://www.youtube.com/watch?v=N-aYZ3WDRII 

https://www.youtube.com/watch?v=Zoo-RsJGCu0

https://youtu.be/cTdpgT-RcCk

# Steps for create Custom Logs

- crear el log analytic
- crear maquina virtual
- crear mi archivo log.txt en la maquina virtual
- enlazar el log analytic con la vm linux
- las urls al parecer no son leidas por el log
- crear el custom log selenium_cl
- buscar

# sample log
2022-11-02 00:17:25,817:INFO:myLogger:Iniciando el log