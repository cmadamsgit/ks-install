# NAME

ks-libvirt - Take a Fedora/CentOS/RHEL kickstart file and make a VM

# SYNOPSIS

ks-libvirt \[options\] `kickstart-file`

At the end of install, if the VM is not shut down with --off and the guest
agent is not excluded with --noaddga, the script waits until the VM is up and
an IPv4 address is configured; it will clean any previous SSH host keys for
that IP and then print the IP, so if you have an SSH key defined, you can do:

> ssh -l root $(ks-libvirt `kickstart-file`)

# OPTIONS

- **--addga | -a**

    Add qemu-guest-agent to %packages; default is to do this, use **--noaddga** to
    disable. Without the agent, the hypvervisor cannot get the IP of the VM (or do
    other VM management).

- **--anaconda | -A** _arguments_

    Additional anaconda boot arguments

- B{--config | -C> `config`

    Config file for defaults; default is $HOME/.virtinst.cf

- **--cpu | -c** _count_

    VM CPU cores; default is 1

- **--disk | -d** _GB_

    VM disk size in gigabytes; default is 6

- **--disk2** _GB_

    VM second disk size in gigabytes; default is to not use a second disk (this is
    mostly just useful for testing kickstart RAID handling)

- **--dns** _DNS-IPs_

    Set the DNS server(s) (comma separated); default: copy host DNS config when
    IPv4 address is set

- **--dumpks | -D**

    Generate a modified kickstart file and dump to standard out (don't build VM)

- **--gw** _IPv4-gateway_

    Set the IPv4 gateway

- **--hostname | -h** _FQDN_

    Set the hostname; default is to not set unless network is set, then use the
    VM name

- **--ip** _IPv4-address/mask_

    Set the IPv4 address and netmask (in bits, e.g. 10.0.0.1/24); default is to try
    DHCP (if network needed)

- **--iso | -i** `ISO`

    ISO to boot from; default is pulled from KS or to use URL instead.  Handles a
    local ISO file (will be uploaded to same pool as VM storage if needed), or
    `pool/volume` for an ISO already in a storage pool.

- **--libvirt | -l** _URL_

    Connection to libvirt; default is $VIRTSH\_DEFAULT\_CONNECT\_UID or qemu:///system

- **--mapfile | -m** `file`

    URL map file to use different source repos.  The format of the file is one
    entry per line with a pair of URLs separated by a space.  The first URL is the
    original (which can be a mirrorlist or metalink) followed by a target URL to
    replace it with (mirrorlist/metalink are turned into direct url entries).  The
    default is `$HOME/.virtinst-map`

- **--name | -n** _name_

    VM name; default is KS file name minus any leading "ks-"

- **--net | -N** _interface_

    Bridge network interface to attach to; default is interface with default route

- **--off | -O**

    Leave the VM off at the end of install

- **--pool | -p** _pool_

    Storage pool name; use pool _default_ by default

- **--os | -o** _OS_

    OS name, used to set VM hardware config; default is autodetect

- **--quiet | -q**

    Be very quiet - only show errors and IP at end

- **--ram | -r** _MB_

    VM RAM size in megabytes; default is 2048 unless specified in the KS

- **--screen | -s**

    Open the VM console screen during install

- **--serial | -S**

    Add a serial console; default is to do this, use **--noserial** to disable

- **--ssh**

    Add found SSH key(s) to the installed system; default is to do this, use
    **--nossh** to disable

- **--tpm**

    Add TPM device

- **--uefi | -u**

    Use UEFI boot instead of BIOS

- **--vdelete**

    Delete an existing VM with the same name before creating new (**NOTE**: will not
    ask for confirmation!)

- **--verbose | -v**

    Be more verbose

- **--virtinst | -V** _arguments_

    Additional virt-install arguments (can be used more than once)

# SPECIAL KICKSTART FILE LINES

The KS file is parsed for lines that look like
_#&lt;tag>:&lt;value>_.  #include pulls in additional files, while the
other options set default values (that can still be overridden on the command
line).

Supported tags:

- **#include**:`file`

    Include another file - this can be a full path or relative to the kickstart
    file itself.  HTTP/HTTPS URLs are also supported.  Includes can appear more
    than once, including in included files.

- **#CPU**:_cores_

    Number of CPU cores

- **#RAM**:_MB_

    RAM size in megabytes

- **#DISK**:_GB_

    Disk size in gigabytes

- **#DISK2**:_GB_

    Second disk size in gigabytes

- **#ISO**:`[pool/]file`

    ISO file/volume to use for install

- **#OS**:_OS string_

    Operating system (only needed if not autodetected)

- **#(NO)SSH**:_1_

    Add/don't add SSH keys

- **#(NO)TPM**:_1_

    Add/don't add TPM device

- **#(NO)UEFI**:_1_

    Use/don't use UEFI boot

# AUTHOR

Written by Chris Adams

# COPYRIGHT

Copyright 2022 Chris Adams. License: GPLv3
