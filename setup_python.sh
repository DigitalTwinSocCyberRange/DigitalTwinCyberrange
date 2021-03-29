apt-get install -y screen &&
apt-get install -y python3 &&
sudo apt-get -y install python3-distutils &&
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py &&
python3 get-pip.py &&
pip3 install flask flask-cors 
