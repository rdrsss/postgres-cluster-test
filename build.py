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

# Start a single node instance
def start_single_node():
    ps = subprocess.Popen([
        "docker",
        "run",
        "-d",
        "--name=postgres_single",
        "-p",
        "5432:5432",
        IMAGE_NAME
        ])
    out, err = ps.communicate()
    if len(str(err)) > 0 and str(err) != "None":
        print "Error starting single node : " + str(err)
        return False
    if len(str(out)) > 0:
        print "\t Container id : " + str(out)
    return True

# Stop a single node instance
def stop_single_node():
    # Stop the Process
    ps = subprocess.Popen([
        "docker",
        "stop",
        "postgres_single"
        ])
    out, err = ps.communicate()
    if len(str(err)) > 0:
        print "Error starting single node : " + str(err)
    if len(str(out)) > 0:
        print "\t Container id : " + str(out)
    # Clean up the container
    ps = subprocess.Popen([
        "docker",
        "rm",
        "postgres_single"
        ])
    out, err = ps.communicate()
    if len(str(err)) > 0:
        print "Error starting single node : " + str(err)
    if len(str(out)) > 0:
        print "\t Container id : " + str(out)

def usage():
    usage = """\
    --help          : Print out this usage text.
    --image         : Image options.
                        build : Build docker image.
                        delete : delete docker image.
    --start-single  : Start single node instance.
    --stop-single   : Stop single node instance.
    """
    print usage

# Main
if __name__ == '__main__':
    # Get opts
    try:
        long_args = [
                "help",
                "image",
                "start-single",
                "stop-single"]
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
        if o in ("--start-single"):
            start_single_node()
        if o in ("--stop-single"):
            stop_single_node()


