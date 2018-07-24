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

@with_setup(setup_test_app, clear)
def test_app():
    gen(data, output_path)
