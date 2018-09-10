from nose import with_setup
from ..code.app import gen
from codegenhelper import put_folder, remove
import demjson

output_path = "./test"

def setup_test_app():
    put_folder(output_path)

def clear():
    pass


'''
generate the code that subscribe to "app"
'''
@with_setup(setup_test_app, clear)
def test_app():
    gen("app", demjson.decode_file("./demo/data.json"), output_path)

@with_setup(setup_test_app, clear)
def test_app_with_None():
    gen("app", demjson.decode_file("./demo/data.json"), output_path)

@with_setup(setup_test_app, clear)
def test_app_with_dependencies():
    gen("dependencies", demjson.decode_file("./demo/data.json"), output_path)
