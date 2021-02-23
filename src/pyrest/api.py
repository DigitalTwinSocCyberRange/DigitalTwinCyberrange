import subprocess
import os
from subprocess import Popen, PIPE
from flask_cors import CORS, cross_origin
from subprocess import check_output
from flask import Flask
from flask import request
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


        
@app.route('/deactivate_directives',methods=['GET'])
@cross_origin()
def deactivate():
    result_success = subprocess.check_output("bash deactivate.sh", shell=True);
    return "deactivated directives";
   
@app.route('/restart_dt',methods=['GET'])
@cross_origin()
def restart():
    result_success = subprocess.check_output("bash restart_dt.sh", shell=True);
    return "restarted dt";

@app.route('/docker_stop',methods=['GET'])
@cross_origin()
def compose():
    result_success = subprocess.check_output("bash docker_stop.sh &>/dev/null", shell=True);
    return "stopped all docker containers";

@app.route('/docker_restart',methods=['GET'])
@cross_origin()
def docker():
    os.system("sudo reboot")
    #result_success = subprocess.check_output("bash reboot.sh", shell=True)
    return "rebooted maschine";

@app.route('/attacker',methods=['GET'])
@cross_origin()
def attacker():
    result_success = subprocess.check_output("bash activate_directive.sh attacker", shell=True)
    return "ok";

@app.route('/mitm',methods=['GET'])
@cross_origin()
def mitm():
    result_success = subprocess.check_output("bash activate_directive.sh mitm", shell=True)
    return "ok";

@app.route('/dos',methods=['GET'])
@cross_origin()
def dos():
    result_success = subprocess.check_output("bash activate_directive.sh dos", shell=True)
    return "ok";

@app.route('/log_manipulation',methods=['GET'])
@cross_origin()
def log_manipulation():
    result_success = subprocess.check_output("bash activate_directive.sh log_manipulation", shell=True)
    return "ok";

@app.route('/arp',methods=['GET'])
@cross_origin()
def arp():
    result_success = subprocess.check_output("bash activate_directive.sh arp", shell=True)
    return "ok";



ip_vm = subprocess.check_output("bash get_ip.sh", shell=True).rstrip();
print ip_vm


app.run(port=9090, host=ip_vm)


