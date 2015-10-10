from pybuilder.core import use_plugin, init, Author

use_plugin('filter_resources')

use_plugin('python.core')
use_plugin('python.coverage')
use_plugin('python.pyfix_unittest')
use_plugin('python.integrationtest')
use_plugin('python.install_dependencies')
use_plugin('python.flake8')
use_plugin('python.pydev')

name = 'flask-example'
authors = [Author('Chirag Ahuja', 'mail.ahujachirag@gmail.com')]
license = '0.1'
summary = 'Test'
version = '0.1.2'


default_task = ['install_dependencies', 'analyze', 'publish']


@init
def set_properties (project):
    project.build_depends_on('kafka')
    project.build_depends_on('avro')
    project.build_depends_on('MySQLdb')

    project.get_property('filter_resources_glob').append('**/lib/__init__.py')
