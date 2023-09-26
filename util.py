import os

from flask import url_for

def get_root_dir():
    return os.getcwd()
    #test


def get_uploads_folder_url():
    return url_for('static', filename='uploads')
    
