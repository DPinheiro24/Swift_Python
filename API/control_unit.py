import functions as f
import json

def pass_aviso(message):
    return {"aviso": message}

def pass_error(message):
    return {"error": message}

def pass_success(message):
    return {"success": message}

def json_data(data):
    return {"data": data}