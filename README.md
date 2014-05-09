Geordi
======
Geordi (La Forge) is a small GitHub webhook receiver written in python publishing Puppet modules to the Forge


Usage
-----
### Run webhook receiver
* Use [build.sh](build.sh) to prepare a virtual environment.
* [Puppet Forge](https://forge.puppetlabs.com) credentials need to be configured via environment variables:
```sh
export FORGE_USER=your-forge-username
export FORGE_PASS=your-forge-password
```
* run geordi: `python app.py`

### Configure GitHub
Once you start geordi it will bind to 0.0.0.0:5000 and listen for payloads on http://0.0.0.0:5000/github

* Create a GitHub Webhook and point it to http://your-host-or-ip:5000/github
* Select `Let me select individual events.'
* Select *only* the `Create' hook
* Save settings

Credits
-------
Created by:
* [Franz Pletz](https://github.com/fpletz)
* [Tristan Helmich](https://github.com/fadenb)
* 
Based on the work done by [@sashasimkin](https://github.com/sashasimkin) (https://github.com/sashasimkin/hook-receiver)

License
-------
GPLv3, see [LICENSE](LICENSE) for details.
