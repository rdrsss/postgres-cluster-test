#!/usr/bin/env python
#
# @filename : build.py
# @author   : Manuel A. Rodriguez (manuel.rdrs@gmail.com)
# @breif    : Simple build script to quickly bring up and tear down
#             a postgres cluster, and possibly other configurations.
#
import os, getopt, sys, subprocess, json, time, ConfigParser

IMAGE_NAME = "test_postgres"


# Build docker image.
def build_postgres_image():
    print " Building postgres image ..."
    os.chdir("postgres")
    subprocess.call(["docker", "build", "-t", IMAGE_NAME, "."])
    os.chdir("..")
    print "done."

# Delete docker image.
def delete_image():
    subprocess.call(["docker", "rmi", IMAGE_NAME])

def usage():
    usage = """\
    --help          : Print out this usage text.
    --image         : Image options.
                        build : Build docker image.
                        delete : delete docker image.
    --start-single  : Start single node.
    """
    print usage

# Main
if __name__ == '__main__':
    # Get opts
    try:
        long_args = [
                "help",
                "image",
                "start-single"]
        opts, args = getopt.getopt(sys.argv[1:], "be:he:s:c:r:", long_args)
    except getopt.GetoptError as err:
        print "opt err: ", str(err)
        usage()
        sys.exit(2)
    # Check for no args passed
    if len(opts) == 0:
        usage()
        sys.exit(2)

    # Check options
    for o, a in opts:
        if o in ("--help"):
            usage()
        if o in ("--image"):
            for a in args:
                if a in ("build"):
                    build_postgres_image()
                elif a in ("delete"):
                    delete_image()
                else:
                    print "Provide arg, [build] or [delete]"


