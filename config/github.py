import mechanize
import glob
import os

# List of refs that to be substituted to re.compile(REFS.%i%).match(request.data.refs)
REFS = ['.*']
# List of commands, that will be spawned
COMMANDS = [
    'git clone -b {ref} {clone_url}',
    'puppet module build {name}',
]


# Hooks
def ref_not_fit(test_ref, payload):
    """
        Function called if ref doesn't fit

    :param test_ref: ref string which failed test from `REFS`
    :param payload: Request payload
    :return:
    """
    pass


def on_command(command, payload):
    """
        Function called on any command

    :param command: Command which will be spawned
    :param payload: Request payload
    :return:
    """
    return command.format(
            clone_url = payload['repository']['clone_url'],
            name = payload['repository']['name'],
            ref = payload['ref'])


def on_error(exception, payload):
    """
        Function called on any error

    :param exception: Raised exception
    :param payload: Request payload
    :return:
    """
    #raise exception
    pass

def publish(path, payload):
    tarball = glob.glob('{path}/*/pkg/*.tar.gz'.format(path=path))[0]
    print tarball
    user, modname = os.path.basename(tarball).split('-')[:2]

    br = mechanize.Browser()
    br.open('https://forge.puppetlabs.com/login')
    br.select_form(predicate = lambda f: f.attrs.get('id', '') == 'login-form')
    br['username'] = os.environ['FORGE_USER']
    br['password'] = os.environ['FORGE_PASS']
    br.submit()
    r2 = br.open('https://forge.puppetlabs.com/{user}/{modname}/upload'.format(user=user, modname=modname))
    br.select_form(predicate = lambda f: f.attrs.get('action', '').endswith('upload'))
    br.form.add_file(open(tarball), 'GET/A/FUCKING/API', 'seriously.exe')
    r3 = br.submit()

