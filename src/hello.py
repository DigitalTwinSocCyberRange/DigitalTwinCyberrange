import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask



def get_shell_script_output_using_check_output(command):
    #stdout = check_output(['docker ps -a']).decode('utf-8')
    result_success = subprocess.check_output(command, shell=True)
    return result_success

app = Flask(__name__)

@app.route('/attacker',methods=['GET'])
def home():
    get_shell_script_output_using_check_output("bash ../activate_directive.sh attacker")
    return "ok";



app.run(port=9090, host='192.168.2.158')

#access via http://192.168.2.158:9090/
