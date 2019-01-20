# MODULE:     file
# PURPOSE:    copies files, changes modes, renders templates, deletes files, slices, dices
# CATEGORY:   general
# PROVIDERS:  file
# RELATED:    directory
# FYI:        See the online documentation for the full parmameter list
#
# DESCRIPTION:
# 
# The File module handles all major types of file operations in OpsMop.
# =======================================================================================

from opsmop.core.easy import *
import getpass
USERNAME = getpass.getuser()

# --------------------------------------------------------------------------------------
# EXAMPLE: Template
# SEE_FILE: templates/foo.txt.j2
#
# DESCRIPTION:
#
# Templating a file from a jinja2 template
#
# See the official `Jinja2 documentation <http://jinja.pocoo.org/docs>`_ for full capabilities
# of Jinja2 templates
# =======================================================================================

class Jinja2TemplateExample(Role):

    def set_variables(self):
        return dict(a=1, b=5150, c="badwolf")

    def main(self):
        # for template language and variable scoping information, please consult the language docs
        File(name="/tmp/opsmop-demo/foo1.txt", from_template="templates/foo.txt.j2")
        Shell("cat /tmp/opsmop-demo/foo1.txt")



# --------------------------------------------------------------------------------------
# EXAMPLE: Copy
#
# DESCRIPTION:
#
# Copying a file with owner, permission, and mode
# =======================================================================================

class CopyExample(Role):

    def main(self):
             
        # owner/group/mode can be used with any of these forms, just showing one example here
        File(name="/tmp/opsmop-demo/foo2.txt", from_file="files/foo.txt", owner=USERNAME, mode=0x755)
        Shell("cat /tmp/opsmop-demo/foo2.txt") 

# --------------------------------------------------------------------------------------
# EXAMPLE: Copy From String
#
# DESCRIPTION:
#
# For very small files, this is also possible
# =======================================================================================

class ContentExample(Role):

    def set_variables(self):
        return dict(a=2, b=2112, c="darmok")

    def main(self):

        File(name="/tmp/opsmop-demo/foo3.txt", from_content="Happy Birthday")
        Shell("cat /tmp/opsmop-demo/foo3.txt")
        File(name="/tmp/opsmop-demo/foo4.txt", from_content=T("Template test! a={{ a}}"))
        Shell("cat /tmp/opsmop-demo/foo4.txt")

# ---------------------------------------------------------------------------------------
# EXAMPLE: Downloading a File
#
# DESCRIPTION:
#
# Grabbing a file from a web location
# =======================================================================================

class FromUrlExample(Role):


    def main(self):
        
        src = "https://raw.githubusercontent.com/opsmop/opsmop/master/README.md"
        File(name="/tmp/opsmop-demo/foo5.txt", from_url=src, overwrite=False)

# ---------------------------------------------------------------------------------------
# EXAMPLE: Deleting a File
#
# DESCRIPTION:
#
# Ensure that a file does not exist
# =======================================================================================

class AbsentExample(Role):

    def main(self):
        File(name="/tmp/opsmop-demo/foo4.txt", absent=True)
        Shell("ls /tmp/opsmop-demo/foo4.txt", ignore_errors=True)

# ---------------------------------------------------------------------------------------
# SETUP: a helper role that sets up for this demo
# =======================================================================================

class CommonSetup(Role):

    def main(self):
        Directory(name="/tmp/opsmop-demo/")

# ---------------------------------------------------------------------------------------
# POLICY: loads all of the above roles
# =======================================================================================

class Demo(Policy):

    def set_roles(self):
       return Roles(
           CommonSetup(),
           Jinja2TemplateExample(d=4, e=5, f=6),
           CopyExample(),
           ContentExample(),
           FromUrlExample(),
           AbsentExample()
       )

if __name__ == '__main__':
    Cli(Demo())




 
