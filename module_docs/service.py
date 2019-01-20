# MODULE:     service
# PURPOSE:    starts/stops and enables/disables services
# CATEGORY:   general
# PROVIDERS:  providers.brew, providers.systemd
# RELATED:    file, package
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The Service module starts, stops, and enables or disables services. The default provider 
# for the operating system (for example, 'apt') is used unless the parameter 'method' is 
# supplied to pick an alternate provider.  See :ref:`method`.
# =======================================================================================

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

# --------------------------------------------------------------------------------------
# EXAMPLE: Basic Example
#
# DESCRIPTION:
#
# Various service operations.  Change the name to a service you don't mind
# restarting.
# =======================================================================================

class BasicExample(Role):

    def main(self):
                
        Service(name='postgres', started=True, enabled=True)
        Service(name='postgres', started=False, enabled=False)
        Service(name='postgres', started=True, enabled=True)


# ---------------------------------------------------------------------------------------
# SETUP: a helper role that sets up for this demo
# =======================================================================================

class CommonSetup(Role):

    def main(self):
        pass

# ---------------------------------------------------------------------------------------
# POLICY: loads all of the above roles
# =======================================================================================

class Demo(Policy):

    def set_roles(self):
       return Roles(
           CommonSetup(),
           BasicExample(),
       )

if __name__ == '__main__':
    Cli(Demo())




 
