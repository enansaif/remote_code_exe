import json
import subprocess
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    if request.method == 'GET':
        return render(request, 'r1code/index.html')

def write_to_file(content):
    with open('script.py', 'w') as script:
        script.write(content)

def execute_script():
    stdout, error = "", ""
    output = subprocess.run(".rce/bin/python script.py", shell=True, 
                            capture_output=True, text=True)
    if output.stdout:
        stdout = output.stdout
    if output.returncode != 0:
        error = output.stderr
    return {
        "stdout": stdout,
        "error": error
    }

def execute_code(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        code = json_data.get('code')
        write_to_file(code)
        response = execute_script()
        return JsonResponse(response)
