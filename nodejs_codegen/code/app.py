from codegenhelper import debug
import os

def get_template_path():
    return os.path.join(os.path.split(__file__)[0], "..", "templates")

def gen(data, output_path):
    debug(output_path, 'gen:output_path')
    debug(get_template_path(), "gen:template_path")
