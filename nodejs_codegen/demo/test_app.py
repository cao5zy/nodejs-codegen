from nose import with_setup
from nodejs_codegen import gen
from codegenhelper import put_folder, remove


data = {
  "name": "test_app"
}
output_path = "./test"

def setup_test_app():
    put_folder(output_path)

def clear():
    pass


'''
generate the code that subscribe to "app"
    data = {
        "name": "name of app",
        "methods": ["get_data", "update_data"],
        "dep_services": ["app1", "app2"]
    }
'''
@with_setup(setup_test_app, clear)
def test_app():
    data = {
        "name": "interface_data_service",
        "methods": ["get_data", "update_data"],
        "dep_services": ["app1", "app2"]
    }
    
    gen("app", data, output_path)
