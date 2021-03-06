try:
    import os
    import sys
    import imp 
    import tqdm
    import time
    import getpass
    import optparse
    import platform
    from optparse import OptionParser
    from tqdm import *
    from time import sleep
    from sys import platform as osid
    ## Custom Module Directory ##
    sys.path.insert(0,"modules")
    import filewrite
    from filewrite import writehtml
except ImportError as e43:
    print "[ ERROR ] - %s..." % (e43)
    print "\nI will attempt to install the modules...\n"
    os.system('pip install tqdm')

## Project: A.N.D-X (Andromeda-x)  -  Version: 1.0.0  -  Xver: 1.0 ##

__version__ = '1.0.0'

## Check if the user is running windows ##
if osid == 'win32':
    # Print the error message
    print "[!] I cannot run on windows. It will break my modules..."
    print("")
    os.system("pause")
    sys.exit(1)

## Check if the user is in root ##
if os.geteuid() == 1:
    print "\033[31m[-]\033[30 Please run this script as root. Try [sudo] python xcheck.py or 'sudo su' than run the script."
    sys.exit(1)

build = '[1.1]'
version = '1.0'
if version > __version__ or version >= build and __version__ + 1:
    print "[I] Older version in use: " + version + ".build[ " + version + 1 + " ]"
    pass
else:
    pass

## Opts ##
def opts():
    parser = OptionParser(usage="[sudo] xcheck.py [OPTIONS] [ARGS]", conflict_handler="resolve")
    parser.add_option("-D", "--dir", dest="chkDir", default="False", help="Check for a directory")
    parser.add_option("-f", "--file", dest="chkFile", default="False", help="Check for a file")
    parser.add_option("-C", "--createdir", dest="createDir", default="False", help="Create a directory")
    parser.add_option("-c", "--createfile", dest="createFile", default="False", help="Create a file")
    parser.add_option("-v", "--verbose", dest="verbose", default="False", help="Be verbose")
    parser.add_option("-V", "--version", dest="verbose", default="False", help="Show the current script version")

    (option, args) = parser.parse_args()
    if options.chkDir == '1':
        dir1 = raw_input("Enter a directory: ")
        if os.path.exists(dir1):
            print "\033[32m[+]\033[30m Directory exists..."
            sys.exit(1)
        else:
            print "\033[31m[-]\033[30m Directory doesn't exist..."
            sys.exit(1)
    elif options.chkFile == '1':
        file1 = raw_input("Enter a file: ")
        if os.path.isfile("file1"):
            print "\033[32m[+]\033[30m File exists..."
            sys.exit(1)
        else:
            print "\033[31m[-]\033[30m File doesn't exist..."
            sys.exit(1)
    elif options.createDir == '1':
        dir2 = raw_input("Directory to create (with path if needed): ")
        try:
            os.makedirs(dir2)
            pass
        except Exception as e:
            print "\033[31m[-]\033[30m Could not create directory  -  error -> " + str(e)
            sys.exit(1)
    elif options.createFile == '1':
        file2 = raw_input("File to create (with path if needed): ")
        try:
            file3 = open(file2,"wr+")
            file3.close()
        except Exception as e:
            print "\033[31m[-]\033[30m Could not create file  -  error -> " + str(e)
            sys.exit(1)
    # Verbose 

    elif options.version == 'show':
        print __version__
        sys.exit(1)
    else:
        print "\033[31m[-]\033[30m Option not found..."
        sys.exit(1)

# **************************************************************************************************************************************************************************
# st.int(a) = 1.st.int[]{'1':'A' -> '2':'B' <- '$a':'C':$result};
# st.int(b) = 2.st.int[]{'1':'${a}' -> '2':'$B + $C' <- '$a[$B + $C]':$result};
# func main(int *(a), int *(b) -> $result[int *(a + ${$[a]} * b + ${$[b]})]) { a1 = char &*int[{2}] >> ${*} + ${'$a' + $b >> %}; result2 = a1 * 2 / 100; os.print $result }
# **************************************************************************************************************************************************************************

## Main ##
os.system("clear")

print "Loading, please wait...\n"
for x in tqdm(range(100)):
    sleep(0.05)
print "\nDone\n"

## Variables ##
author = 'S1lent'
email = 'silentcore32@gmail.com'
email2 = 'gleb.bair@my.sinclair.edu'
xver = '1.0'
xgs = "\033[32m"                                   # Green start
xge = "\033[30m"                                   # Green end
xrs = "\033[31m"                                   # Red start
xre = "\033[30m"                                   # Red end
xbs = "\033[34m"                                   # Blue start
xbe = "\033[30m"                                   # Blue end
xes = "\033[33m"                                   # Yellow start
xse = "\033[30m"                                   # Yellow end 
plus = "\033[32m[+]\033[30m"                       # Green [+]
minus = "\033[31m[-]\033[30m"                      # Red [-]
exc = "\033[31m[!]\033[30m"                        # Red [!]
info = "[I]"                                       # Self explanitory
info_urgent = "\033[31m[I]\033[30m"                # Red [I]
regular = "[*]"                                    # Self explanitory
regular_urgent = "\033[31m[*]\033[30m"             # Red [*]

## Directories ##
CONFIG = "/root/andx/config"
BOTS = "/root/andx/bots"
XRTK = "/root/andx/xrtk"
XBD = "/root/andx/xbd"
SRCS = "/root/andx/srcs"
SCANNERS = "/root/andx/scanners"
# Directories (Scanners [scanners])
scn_c = "/root/andx/scanners/c"
# - Directories (/scanners/c)
scn_c_src = "/root/andx/scanners/c/src"
scn_c_ps = "/root/andx/scanners/c/portscanner"
scn_c_vulns = "/root/andx/scanners/c/vulns"
# --------------------------------------------
scn_cpp = "/root/andx/scanners/c++"
scn_web = "/root/andx/scanners/web"
scn_os = "/root/andx/scanners/os"
REPORTER = "/root/andx/reporter"
XGUI = "/root/andx/xgui"
LOGS = "/root/andx/logs"
CHAT_BOT = "/root/andx/chat_bot"
SITE = "/root/andx/site"
# Directories (Site [site])
site_downloads = "/root/andx/site/downloads"
site_css = "/root/andx/site/css"
site_images = "/root/andx/site/images"
site_js = "/root/andx/site/javascript"
site_php = "/root/andx/site/php"
site_java = "/root/andx/site/java"
site_python = "/root/andx/site/python"

## Files ##
xconfig = "/root/andx/config/xconfig.txt"
xlog_a = "/root/andx/logs/xlogs-a.txt"
# Files (Site [site] {HTML (.html)})
index_html = "/root/andx/site/index.html"
downloads_html = "/root/andx/site/downloads.html"
help_html = "/root/andx/site/help.html"
about_html = "/root/andx/site/about.html"
register_html = "/root/andx/site/registeration.html"

## Lists ##
list_tools = ['Responder', 'Metasploit', 'Sqlmap', 'Nikto', 'Nmap']

## Main ##
print("")
# print xrs + "*" * 84 + xre                                                                                         # Prints 84 "*"
print xgs + "=" * 84 + xge + "\n"                                                                                    # Prints 84 "="
print "\t\t\t " + "-" * 4 + "=" * 5 + "[" + xes + " By: " + xse + xgs + author + xge + " ]" + "=" * 5 + "-" * 4      # Prints ----=====[ By: ${author} ]=====---- 
print "\t\t\t          " + xes + "Version: " + xse + xgs + __version__ + xge + "\n"                                  # Prints Version ${__version__}
print "\t\t\t " + xes + "Questions? " + xse + xgs + email + xge                                                      # Prints Questions? ${email}
print "\t\t\t\t" + xes + "  Running in: " + xse + xgs + getpass.getuser() + xge                                      # Prints Running in: root
print xgs + "-" * 84 + xge                                                                                           # Prints 84 "-"
print xgs + "*" * 84 + xge + "\n"                                                                                    # Prints 84 "*"
print regular + " Note: Some directories will create sub-directories.\n"
# Check for needed directories, if the directory exists, print that it exists
print regular + " Checking directories...\n"
if os.path.exists(LOGS):
    pass
else:
    try:
        os.makedirs(LOGS)
        file1 = open(xconfig,"w")
        pass
    except Exception as e:
        print minus + " Could not create directory..."
        pass
# ------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(CONFIG):
    print plus + " Directory: " + xgs + CONFIG + xge + " exists..."
    try:
        file1 = open(xconfig,"w")
        file1.write("==========[ Xcheck " + __version__ + " ]==============================================\n\n")
        file1.write("Directory [Config (config)]:           " + CONFIG + " exists...\n")
    except IOError as e54:
        print "Unable to open file: " + xgs + xconfig + xge + " error -> " + str(e54)
        pass
    if os.stat(CONFIG) == 0:
        print minus + " Directory: " + xgs + CONFIG + xge + " existed, but isn't there now..."
        question_02 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_02 or 'm' in question_02:
            dir_02 = raw_input("Enter the new directory: ")
            while len(dir_02) == 0:
                print minus + " I need a directory...\n"
            if os.path.exists(dir_02) and os.path.join(dir_02, "/config") or os.path.join(dir_02, "config"):
                file1.write("Directory [ Alt ] Config (config):      " + dir_02 + "\n")
            else:
                print minus + " Directory cannot be found..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_02 or 'd' in question_02:
            print info + " Creating directory: " + xgs + CONFIG + xge
            try:
                os.makedirs(CONFIG)
                pass
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e:
                print exc + " Could not create directory: " + xgs + CONFIG + xge + " error -> " + str(e)
                print info + " Exiting..."
                sys.exit(1)
        if not 'M' or 'm' or 'D' or 'd' in question_02 or len(question_02) == 0:
            print minus + " I need an input, please enter a 'M' ('m') if the file was moved, or 'D' ('d') if the file was deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + CONFIG + xge
    try:
        os.makedirs(CONFIG)
        file1.write("Directory [Config (config)]:     " + CONFIG + " created...\n")
        pass
    except Exception as e:
        print exc + " Could not create directory: " + xgs + CONFIG + xge + " error -> " + str(e)
        # Write to log file
        file1.write("\n[ ERROR ] -> " + str(e) + "\n")
        print info + " Exiting..."
        sys.exit(1)
# ----------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(XRTK):
    print plus + " Directory: " + xgs + XRTK + xge + " exists..."
    file1.write("Directory [ Xrtk (xrtk)]:              " + XRTK + " exists...\n")
    pass
    if os.stat(XRTK) == 0:
        print minus + " Directory: " + xgs + XRTK + xge + " existed, but isn't there now..."
        question_01 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_01 or 'm' in question_01:
            dir_01 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_01) and os.path.join(dir_01, "/config") or os.path.join(dir_01, "config"):
                file1.write("Directory [ Alt ] Xrtk (xrtk):     " + XRTK + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_01 or 'd' in question_01:
            print info + " Creating directory: " + xgs + XRTK + xge
            try:
                os.makedirs(XRTK)
                pass
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e2:
                print exc + " Could not create directory: " + xgs + XRTK + xge + " error -> " + str(e2)
                file2.write("[ ERROR ]: " + str(e2) + "\n")
        if not 'M' or 'm' or 'D' or 'd' in question_01 or len(question_01) == 0:
            print minus + " Input needed: please type an [ 'M' ('m') = Moved or 'D' ('d') = Deleted ]...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + XRTK + xge
    try:
        os.makedirs(XRTK)
        file1.write("Directory [ Xrtk (xrtk)]:         " + XRTK + " created...\n")
    except Exception as e3:
        print minus + " Could not create directory: " + xgs + XRTK + xge + " error -> " + str(e3)
        file2.write("[ ERROR ]: " + str(e3) + "\n")
        print info + " Exiting..."
        sys.exit(1)
# ---------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(SCANNERS):
    print plus + " Directory: " + xgs + SCANNERS + xge + " exists... Will now check for it's sub-directories..."
    try:
        file1.write("Directory [ Scanners (scanners)]:      " + SCANNERS + " exists...\n")
    except IOError as e38:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e38)
        pass
    if os.stat(SCANNERS) == 0:
        print minus + " Directory: " + xgs + SCANNERS + xge + " existed, but isn't there now..."
        question_08 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_08 or 'm' in question_08:
            dir_08 = raw_input("Enter the new directory: ")
            # After this program (project) is complete, no Anti-Virus will be able to protect you...You won't find, me - S1lent
            if os.path.exists(dir_08) or os.path.join(dir_08, "/scanners") or os.path.join(dir_08, "scanners"):
                file1.write("Directory [ Alt ] Scanners (scanners):     " + dir_08 + "\n")
            else:
                print minus + " Directory not found..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_08 or 'd' in question_08:
            print info + " Creating directory: " + xgs + SCANNERS + xge
            try:
                os.makedirs(SCANNERS)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e4:
                print exc + " Could not create directory: " + xgs + SCANNERS + xge + " error -> " + str(e4)
                print info + " Exiting..."
                sys.exit(1)
        if not 'M' or 'm' or 'D' or 'd' in question_08 or len(question_08) == 0:
            print minus + " Please type an 'M' ('m') for Moved or 'D' ('d') for Deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + SCANNERS + xge
    try:
        os.makedirs(SCANNERS)
        try:
            file1.write("Directory [ Scanners (scanners)]:     " + SCANNERS + " created...\n")
        except IOError as e37:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e37)
            pass
    except Exception as e5:
        print exc + " Could not create directory: " + xgs + SCANNERS + xge + " error -> " + str(e5)
        print info + " Exiting..."
        sys.exit(1)
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Create the sub-directories and files for the [ Scanners (scanners)] directory
## Check for directories and files ##
# [+] Directory: [ PATH_TO_SCANNERS ] exists...
# |_[SUB_DIR] - [ C ] exists...
# | |_[SUB_DIR] - [ SRC ] exists...
# | |_[SUB_DIR] - [ PORT_SCANNER ] exists...
# | |_[SUB_DIR] - [ VULNS ] exists...
# |-------------------------------------------
# |_[SUB_DIR] - [ C++ ] exists...
# |_[SUB_DIR] - [ Web ] exists...
# |_[SUB_DIR] - [ OS ] exists...
#####################################################################################
# I try to ask for help, no one replies...I try to talk to them, they won't listen, or not attempt to try to understand...They looked like people I could talk to, they sounded promising, they looked like they would understand...But no, I was mistaken, it was a mistake to think that I could put my hopes in them...Now, I do this alone...Without their help...My help, is the search engine, and knowledge of what I need to accomplish...
# ------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(scn_c):
    print xgs + "|__|_" + xge + "[Sub-Dir] - " + xgs + scn_c + xge + " exists..."
    try:
        file1.write("|_[SUB_DIR] - " + scn_c + " exists...\n")
    except IOError as e36:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e36)
        pass
    if os.stat(scn_c) == 0:
        print minus + " Directory: " + xgs + scn_c + xge + " existed, but isn't there now..."
        question_09 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_09 or 'm' in question_09:
            dir_09 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_09) or os.path.join(dir_09, "/c") or os.path.join(dir_09, "c"):
                file1.write("|_[SUB_DIR_ALT] - " + dir_09 + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_09 or 'd' in question_09:
            print info + " Creating directory: " + xgs + scn_c + xge
            try:
                os.makedirs(scn_c)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e8:
                print exc + " Could not create directory: " + xgs + scn_c + xge + " error -> " + str(e8)
                print info + " Exiting..."
                sys.exit(1)
        if not 'M' or 'm' or 'D' or 'd' or len(question_09) == 0:
            print minus + " Inputs are 'M' ('m') for Moved or 'D' ('d') for Deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + scn_c + xge
    try:
        os.makedirs(scn_c)
        try:
            file1.write("|_[SUB_DIR] - " + scn_c + " created...\n")
        except IOError as e35:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e35)
            pass
    except Exception as e9:
        print exc + " Could not create directory: " + xgs + scn_c + xge + " error -> " + str(e9)
        print info + " Exiting..."
        sys.exit(1)
# -----------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(scn_c_src):
    print xgs + "|____|_" + xge + "[SUB_DIR_C] - " + xgs + scn_c_src + xge + " exists..."
    try:
        file1.write("      |_[SUB_DIR_C] - " + scn_c_src + " exists...\n")
    except IOError as e34:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e34)
        pass
    if os.stat(scn_c_src) == 0:
        print minus + " [ SUB ] - Directory: " + xgs + scn_c_src + xge + " existed, but isn't there..."
        question_07 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_07 or 'm' in question_07:
            dir_07 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_07) or os.path.join(dir_07, "/src") or os.path.join(dir_07, "src"):
                file1.write("      |_[SUB_DIR_C] - " + dir_07 + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_07 or 'd' in question_07:
            print info + " Creating directory: " + xgs + scn_c_src + xge
            try:
                os.makedirs(scn_c_src)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e10:
                print exc + " Could not create directory: " + xgs + scn_c_src + xge + " error -> " + str(e10)
                print info + " Exiting..."
                sys.exit(1)
        if not 'M' or 'm' or 'D' or 'd' in question_07 or len(question_07) == 0:
            print minus + " Input needed, [M] = Moved, [D] = Deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + scn_c_src + xge
    try:
        os.makedirs(scn_c_src)
        try:
            file1.write("|____|_[SUB_DIR_C] - " + scn_c_src + " created...\n")
        except IOError as e33:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e33)
        pass
    except Exception as e11:
        print exc + " Could not create directory: " + xgs + scn_c_src + xge + " error -> " + str(e11)
        print info + " Exiting..."
        sys.exit(1)
# ------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(scn_c_ps):
    print xgs + "|____|_" + xge + "[SUB_DIR_C] - " + xgs + scn_c_ps + xge + " exists..."
    try:
        file1.write("      |_[SUB_DIR_C] - " + scn_c_ps + " exists...\n")
    except IOError as e32:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e32)
        pass
    if os.stat(scn_c_ps) == 0:
        print minus + " Directory: " + xgs + scn_c_ps + xge + " existed, but isn't there..."
        question_03 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_03 or 'm' in question_03:
            dir_03 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_03) or os.path.join(dir_03, "/portscanner") or os.path.join(dir_03, "portscanner"):
                file1.write("     |_[SUB_DIR_C] - " + scn_c_ps + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_03 or 'd' in question_03:
            print info + " Creating directory: " + xgs + scn_c_ps + xge
            try:
                os.makedirs(scn_c_ps)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e12:
                print exc + " Could not create directory: " + xgs + scn_c_ps + xge + " error -> " + str(e12)
                print info + " Exiting..."
                sys.exit(1)
        else:
            pass
else:
    print info + " Creating directory: " + xgs + scn_c_ps + xge
    try:
        os.makedirs(scn_c_ps)
        try:
            file1.write("      |_[SUB_DIR_C] - " + scn_c_ps + " created...\n")
        except IOError as e31:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e31)
            pass
    except Exception as e13:
        print exc + " Could not create directory: " + xgs + scn_c_ps + xge + " error -> " + str(e13)
        print info + " Exiting..."
        sys.exit(1)
# ------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(scn_cpp):
    print xgs + "|_" + xge + "[SUB_DIR] - " + xgs + scn_cpp + xge + " exists..."
    try:
        file1.write("|_[SUB_DIR] - " + scn_cpp + " exists...\n")
    except IOError as e30:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e30)
        pass
    if os.stat(scn_cpp) == 0:
        print minus + " Directory: " + xgs + scn_cpp + xge + " existed, but isn't there..."
        question_05 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_04 or 'm' in question_04:
            dir_05 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_05) or os.path.join(dir_05, "/cpp") or os.path.join(dir_05, "cpp"):
                file1.write("|_[SUB_DIR] - (Alt): " + dir_05 + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_04 or 'd' in question_04:
            print info + " Creating directory: " + xgs + scn_cpp + xge
            try:
                os.makedirs(scn_cpp)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e14:
                print exc + " Could not create directory: " + xgs + scn_cpp + xge + " error -> " + str(e14)
                print info + " Exiting..."
                sys.exit(1)
        else:
            print minus + " Option not found..."
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + scn_cpp + xge
    try:
        os.makedirs(scn_cpp)
        try:
            file1.write("|_[SUB_DIR] - " + scn_cpp + " created...\n")
        except IOError as e29:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e29)
            pass
    except Exception as e15:
        print exc + " Could not create directory: " + xgs + scn_cpp + xge + " error -> " + str(e15)
        print info + " Exiting..."
        sys.exit(1)
# -------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(SITE):
    print plus + " Directory: " + xgs + SITE + xge + " exists...  -  Will now check it's sub-directories"
    try:
        file1.write("Directory [Site (site)]:               " + SITE + " exists...\n")
    except IOError as e28:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e28)
        pass
    if os.stat(SITE) == 0:
        print minus + " Directory: " + xgs + SITE + xge + " existed, but isn't there anymore...\n"
        question = raw_input("Was the file [M]oved or [D]eleted? : ")
        if 'M' in question or 'm' in question:
            dir3 = raw_input("Enter the new directory: ")
            if os.path.exists(dir3) or os.path.join(dir3,"/site") or os.path.join(dir3,"site"):
                file1.write("Directory [ Alt ] Site (site):     " + SITE + "\n")
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        if 'D' in question or 'd' in question:
            print info + " Creating directory: " + xgs + SITE + xge
            try:
                os.makedirs(SITE)
            except KeyboardInterrupt:
                # print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e16:
                print exc + " Could not create directory: " + xgs + SITE + xge + " error -> " + str(e16)
                print info + " Exiting..."
                sys.exit(1)
        if not 'M' in question or not 'm' in question or not 'D' in question or 'd' in question:
            print minus + " I need your input...Please select (type) 'M' or 'm' if the file was moved, or 'D' ('d') if the file was deleted...\n"
            pass
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + SITE + xge
    try:
        os.makedirs(SITE)
        try:
            file1.write("Directory [Site (site)]:             " + SITE + " created...\n")
        except IOError as e27:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e25)
            pass
    except Exception as e17:
        print exc + " Could not create directory: " + xgs + SITE + xge + " error -> " + str(e17)
        print info + " Exiting..."
        sys.exit(1)
# Create the sub-directories for the main directory [ Site (site)]
# -> [SUB_DIR] >> [Site (site)] >>> [Site >> downloads (site)]
if os.path.exists(site_downloads):
    print xgs + "|_" + xge + site_downloads + xgs + " exists..." + xge
    try:
        file1.write("|_[SUB_DIR] - " + site_downloads + "\n")
    except IOError as e26:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e26)
        pass
    if os.stat(site_downloads) == 0:
        print minus + " The directory: " + xgs + site_downloads + xge + " existed, but isn't there anymore..."
        question01 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        while len(question01) == 0:
            print minus + " I need a directory...\n"
        if 'M' or 'm' in question01:
            newDir = raw_input("Enter the new directory: ")
            while len(newDir) == 0 or newDir == False:
                print("")
                print info + " I need a(n) directory, try typing the path...\n"
            if os.path.exists(newDir) or os.path.join(newDir,"/downloads") or os.path.join(newDir,"downloads"):
                file1.write("Directory [Site (site)] Alt:    " + newDir + "\n")
                pass
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' or 'd' in question01:
            print info + " Creating directory: " + xgs + site_downloads + xge
            try:
                os.makedirs(site_downloads)
                pass
            except KeyboardInterrupt:
                # print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e18:
                print exc + " Could not create the directory: " + xgs + site_downloads + xge + " error -> " + str(e18)
                print info + " Exiting..."
                sys.exit(1)
        elif not 'M' or 'm' or 'D' or 'd' in question01 or len(question01) == 1 - 1:
            print minus + " Please enter an [M] for Moved or [D] for Deleted..."
            pass
        else:
            print minus + " Invalid input.."
            pass
else:
    print info + " Creating directory: " + xgs + site_downloads + xge
    try:
        os.makedirs(site_downloads)
        try:
            file1.write("|_[SUB_DIR] - " + site_downloads + " Created" + "\n")
        except IOError as e23:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e23)
            pass
    except Exception as e19:
        print exc + " Could not create directory: " + xgs + site_downloads + xge + " error -> " + str(e19)
        print info + " Exiting..."
        sys.exit(1)
# -> [SUB_DIR] >> SITE_IMAGES >>> [Site (site) sub_dir_images]
if os.path.exists(site_images):
    print xgs + "|_" + xge + site_images + xgs + " exists..." + xge
    try:
        file1.write("|_[SUB-DIR] - " + site_images + " exists...\n")
        pass
    except IOError as e20:
        print minus + " Could not write to file: " + xgs + file1 + xge + " error -> " + str(e20)
        pass
    if os.stat(site_images) == 0:
        print minus + " Directory: " + xgs + site_images + xge + " existed, but isn't there anymore..."
        question02 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        while len(question02) == 0 or question02 == False:
            print("")
            print info + " I need an input, please select [M] for Moved or [D] for Deleted...\n"
        if 'M' or 'm' in question02:
            dir4 = raw_input("Enter the new directory: ")
            while len(dir4) == 0 or len(dir) == False:
                print info + " I need a(n) directory, try typing the path...\n"
            if os.path.exists(dir4) or os.path.join(dir4,"/images") or os.path.join(dir4,"images"):
                try:
                    file1.write("|_[SUB-DIR]:Alt - " + dir4 + "\n")
                    pass
                except Exception as e21:
                    print minus + " Couldn't write to file: " + xgs + xconfig + xge + " error -> " + str(e21)
                    pass
            else:
                print minus + " Could not find the directory specified..."
        elif 'D' or 'd' in question02:
            print info + " Creating directory: " + xgs + site_images + xge
            try:
                os.makedirs(site_images)
            except KeyboardInterrupt:
                # print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e22:
                print exc + " Could not create directory: " + xgs + site_images + xge + " error -> " + str(e22)
                print info + " Exiting..."
                sys.exit(1)
        else:
            print minus + " Option not found..."
    else:
        pass
else:
    print info + " Creating directory: " + xgs + site_images + xge
    try:
        os.makedirs(site_images)
        try:
            file1.write("|_[SUB-DIR] - " + site_images + " created...\n")
        except IOError as e23:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e23)
            pass
    except Exception as e24:
        print exc + " Could not create directory: " + xgs + site_images + xge + " error -> " + str(e24)
        print info + " Exiting..."
        sys.exit(1)
# -> [SUB_DIR] >> SITE_CSS >>> [Site (site) sub_dir_css]
if os.path.exists(site_css):
    print xgs + "|_" + xge + site_css + xgs + " exists..." + xge
    try:
        file1.write("|_[SUB-DIR] - " + site_css + " exists...\n")
    except IOError as e25:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e25)
        pass
# *******************[ TRANSMISSION LOG - 01  -  A  -  S1lent -> [|||||||] ]****************************************************************
# [|||||||] >> Will this do?
# S1lent >> Yes, this is fine.
# [|||||||] >> Ok, but, why like this??? Isn't there another way???
# S1lent >> Not the way this program will turn out...The tool
# [|||||||] >> Won't this confuse people??? It did me before I got it, the way you see it...
# S1lent >> Relax, they will figure it out...Although, it might take them a while...
# [|||||||] >> A while is kind of underestimating it...
# S1lent >> Trust me, someone is bound to look through (top  to bottom) of this script and figure out how to read it...
# [|||||||] >> Has anyone done THAT yet???
# S1lent >> Lol, no, not yet.
# ******************[ TRANSMISSION LOG - 01  -  A  -  END ]********************************************************************************    
    if os.stat(site_css) == 0:
        print minus + " The directory: " + xgs + site_css + xge + " existed, but isn't there anymore..."
        question03 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        while len(question03) == 0 or len(question03) == 2:
            print info + " Please enter a valid input..."
            pass
        if 'M' or 'm' in question03:
            newDir2 = raw_input("Enter the new directory: ")
            while len(newDir2) == 0 or len(newDir2) == 2:
                print minus + " Please enter a(n) [ Valid ] directory..."
                pass
            if os.path.exists(newDir2) or os.path.join(newDir2,"/css") or os.path.join(newDir2,"css"):
                try:
                    file1.write("[SUB-DIR] - Alt: " + newDir2 + "\n")
                except IOError as e39:
                    print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e25)
                    pass
            else:
                print minus + " Directory " + xgs + newDir2 + xge + " not found..."
                pass
        elif 'D' or 'd' in question03:
            print info + " Creating directory: " + xgs + site_css + xge
            try:
                os.makedirs(site_css)
                pass
            except KeyboardInterrupt:
                # print "Manual Program Termination (Ctrl + C)"
                sys.exit()
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + site_css + xge
    try:
        os.makedirs(site_css)
        try:
            file1.write("[SUB-DIR] - " + site_css + " created...")
        except IOError as e41:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e25)
            pass
    except Exception as e42:
        print exc + " Could not create directory: " + xgs + site_css + xge + " error -> " + str(e42)
        print info + " Exiting..."
        sys.exit(1)
# -> [SUB_DIR] SITE_JS >> [Site (site)]
if os.path.exists(site_js):
    print xgs + "|_" + xge + site_js + xgs + " exists..." + xge
    try:
        file1.write("|_[SUB-DIR] - " + site_js + " exists...\n")
        pass
    except IOError as e47:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e47)
        pass
    if os.stat(site_js) == 0:
        print minus + " The directory: " + xgs + site_js + xge + " existed, but isn't there anymore..."
        question04 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        while not 'M' or 'm' or 'D' or 'd' in question04 or len(question04) == 0:
            print minus + " Please enter a valid input..."
        if 'M' or 'm' in question04:
            newDir3 = raw_input("Enter the new directory: ")
            while not os.path.exists(newDir3) or len(newDir3) == 0:
                print minus + " Please enter a valid directory..."
            if os.path.exists(newDir3) or os.path.join(newDir3,"/javascript") or os.path.join(newDir3,"javascript"):
                try:
                    file1.write("|_[SUB-DIR] - Alt: " + newDir3 + "\n")
                    pass
                except IOError as e48:
                    print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e48)
                    pass
            else:
                print minus + " Could not find the directory..."
                pass
        elif 'D' or 'd' in question04:
            print info + " Creating directory: " + xgs + site_js + xge
            try:
                os.makedirs(site_js)
            except KeyboardInterrupt:
                # print "Manual Program Termination (Ctrl + C)"
                sys.exit()
            except Exception as e49:
                print exc + " Could not create directory: " + xgs + site_js + xge + " error -> " + str(e49)
                print info + " Exiting..."
                sys.exit(1)
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + site_js + xge
    try:
        os.makedirs(site_js)
        try:
            file1.write("|_[SUB-DIR] - " + site_js + " created...\n")
            pass
        except IOError as e50:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e50)
            pass
    except Exception as e51:
        print exc + " Could not create directory: " + xgs + site_js + xge + " error -> " + str(e51)
        print info + " Exiting..."
        sys.exit(1)
# -> [SUB_DIR] >> SITE_PHP (Site [site])
if os.path.exists(site_php):
    print xgs + "|_" + xge + site_php + xgs + " exists..." + xge
    try:
        file1.write("|_[SUB-DIR] - " + site_php + " exists...\n")
        pass
    except IOError as e52:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e52)
        pass
    if os.stat(site_php) == 0:
        print minus + " Directory: " + xgs + site_php + xge + " existed, but isn't there anymore..."
        question05 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        while len(question05) == 0 or len(question05) < 1:
            print info + " Please enter a valid input..."
        if 'M' or 'm' in question05:
            newDir4 = raw_input("Enter the new directory: ")
            while len(newDir4) == 0 or len(newDir4) >= 2 or 'help' in newDir4:
                print minus + " Please enter the path to the new directory..."
            if os.path.exists(newDir4) or os.path.join(newDir4,"/php") or os.path.join(newDir4,"php"):
                file1.write("|_[SUB-DIR] - Alt: " + newDir4 + "\n")
                pass
            else:
                print minus + " Path: " + xgs + newDir4 + xge + " could not be found..."
        elif 'D' or 'd' in question05:
            print info + " Creating directory: " + xgs + site_php + xge
            try:
                os.makedirs(site_php)
                pass
            except KeyboardInterrupt:
                # print "Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e53:
                print exc + " Could not create directory: " + xgs + site_php + xge + " error -> " + str(e25)
                print info + " Exiting..."
                sys.exit(1)
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + site_php + xge
    try:
        os.makedirs(site_php)
        try:
            file1.write("|_[SUB-DIR] - " + site_php + " created...\n")
            pass
        except IOError as e26:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e26)
            pass
    except Exception as e27:
        print exc + " Could not create directory: " + xgs + site_php + xge + " error -> " + str(e26)
        print info + "Exiting..."
        sys.exit(1)
# -> [SUB_DIR] >> SITE_JAVA (Site [site])
if os.path.exists(site_java):
    print xgs + "|_" + xge + site_java + xgs + " exists..." + xge
    try:
        file1.write("|_[SUB-DIR] - " + site_java + " exists...")
        pass
    except IOError as e55:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e55)
        pass
    if os.stat(site_java) == 0:
        print minus + " Directory: " + xgs + site_java + xge + " was there before, but isn't there now..."
        question = raw_input("Was the directory [M]oved or [D]eleted: ")
        while len(question) == 0 or question == "help":
            print("")
            print info + " Just press M or m or D or d"
            print("")
        if 'M' or 'm' in question:
            new_dir = raw_input("Where is the new directory located? : ")
            while len(new_dir) == 0:
                print("")
                print info + " Please input a directory i.e: '/root/andx/site' or something like that..."
                print("")
            if os.path.exists(new_dir) or os.path.join(new_dir,"/java") or os.path.join(new_dir,"java"):
                file1.write("|_[SUB-DIR] - Alt: " + new_dir + "\n")
                pass
            else:
                print("")
                print minus + " Could not find the directory specified..."
                print("")
        elif 'D' or 'd' in question:
            print info + " Creating directory: " + xgs + site_java + xge
            try:
                os.makedirs(site_java)
            except KeyboardInterrupt:
                # print "Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e56:
                print exc + " Could not create directory: " + xgs + site_java + xge + " error -> " + str(e56)
                print info + " Exiting..."
                sys.exit(1)
        else:
            pass
    else:
        pass
else:
    print info + " Creating directory: " + xgs + site_java + xge
    try:
        os.makedirs(site_java)
        pass
        try:
            file1.write("|_[SUB-DIR] - " + site_java + " created...\n")
            pass
        except IOError as e57:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e57)
            pass
    except Exception as e58:
        print exc + " Could not create directory: " + xgs + site_java + xge + " error -> " + str(e58)
        print info + " Exiting..."
        sys.exit(1)



# -------------------------------------------------------------------------------------------------------------------------------------------------
if os.path.exists(XBD):
    print("")
    print plus + " Directory: " + xgs + XBD + xge + " exists..."
    try:
        file1.write("\nDirectory [Xbd (xbd)]:                 " + XBD + " exists...\n")
        file1.close()
    except IOError as e44:
        print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e25)
        pass
    if os.stat(XBD) == 0:
        print minus + " Directory: " + xgs + XBD + xge + " existed, but isn't there anymore..."
        question_04 = raw_input("Was the directory [M]oved or [D]eleted? : ")
        if 'M' in question_04 or 'm' in question_04:
            dir_04 = raw_input("Enter the new directory: ")
            if os.path.exists(dir_04) or os.path.join(dir_04,"/xbd") or os.path.join(dir_04,"xbd"):
                try:
                    file1.write("Directory [ Alt ] Xbd (xbd):    " + XBD + "\n")
                    file1.close()
                except IOError as e45:
                    print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e45)
                    pass
            else:
                print minus + " Could not find directory..."
                print info + " Exiting..."
                sys.exit(1)
        elif 'D' in question_04 or 'd' in question_04:
            print info + " Creating directory: " + xgs + XBD + xge
            try:
                os.makedirs(XBD)
            except KeyboardInterrupt:
                # Print info + " Manual Program Termination (Ctrl + C)"
                sys.exit(1)
            except Exception as e6:
                print exc + " Could not create directory: " + xgs + XBD + xge + " error -> " + str(e6)
                print info + " Exiting..."
                sys.exit(1)
        else:
            pass
else:
    print info + " Creating directory: " + xgs + XBD + xge
    try:
        os.makedirs(XBD)
        try:
            file1.write("Directory [ Xbd (xbd)]:                 " + XBD + " created...\n")
            file1.close()
        except IOError as e46:
            print minus + " Could not write to file: " + xgs + xconfig + xge + " error -> " + str(e46)
            pass
    except Exception as e7:
        print exc + " Could not create directory: " + xgs + XBD + xge + " error -> " + str(e7)
        print info + " Exiting..."
        sys.exit(1)



# if __name__ == '__main__':
#    opts()
