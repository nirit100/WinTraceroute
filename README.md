# WinTraceroute

Provides a mostly *NIX-traceroute-like -- but very basic -- `tracert`/`traceroute` UDP/IPv4 alternative built on [scapy](https://scapy.net/). Available for Windows, Linux, Mac and everything else that runs Python3 and Scapy.

The motivation for this small project was the differences in behaviour between Linux' `traceroute` and Windows' `tracert` commands, in particular that the Windows variant uses ICMP and therefore does not allow for a custom package size in the same way the Linux variant does.
I just wanted to bring a basic version of the Linux-`traceroute` to Windows, while also having this program do just the same on any other platform.

This package is meant to be used via the integrated CLI, but the `traceroute.py` module can be used to capture Scapy's results in `list`s, so that it can technically be called from Python code.

## Usage

```
$ wintraceroute
usage: traceroute [-h] [-m MAXTTL] [-f MINTTL] [-q FLEETSIZE] [-w TIMEOUT] [-p PORT] [-s SOURCE] [-M {UDP,ICMP}] host [packet_length]
```

**Note**: This program often requires higher privileges to obtain access to the network adapter because of Scapy under it. If you encounter such problems:
 * on Windows, run as administrator
 * on Linux/Mac, run with `sudo`

Example run (I redacted some IPs with `#`s):

```
$ sudo wintraceroute 8.8.8.8

  1        8.238           4.052           3.911        ###.###.###.###
  2       12.462                          12.313        62.155.###.###
                            *                            (no response)
  3       21.610          19.516          18.816        217.5.118.26
  4       19.093          19.010          20.092        87.128.238.134
  5         *               *               *            (no response)
  6       21.839          21.319          27.482        8.8.8.8

Destination '8.8.8.8' reached  in RTT min. 21.319, avg. 23.547, max. 27.482 ms  via 6 hops.
```

See also the help page, available using the `-h` or `--help` option.

## Installation and/or Download

The recommended way of installing this tool on any platform is via pip, but there are also standalone binaries available for Windows and can be built for Linux.

### Via `pip` / from PyPI

If you are running *Python 3.9* or above, you may want to install WinTraceroute via `pip`. This also tries to register the `wintraceroute` command in your system.

**Just run `pip install WinTraceroute` in your local Python environment.**

You may also want to head over to [this project on PyPI](https://pypi.org/project/WinTraceroute/).

### Windows Binary

These binaries are just plain and simple unsigned builds using PyInstaller.
They *don't* require a local Python environment, so this is the easiest way of running this program if you're on Windows and just want a simple `.exe` file.

**You can download it from the *Assets* section in the [latest Release](https://github.com/NiRit100/WinTraceroute/).**

### Linux Binary

You can **build a standalone binary from source**, if you like:
 * Install all necessary dependencies (if you don't have them already):
    * Python 3.9 or newer
    * `make`
 * Download/clone the source code and change into the directory.
 * Install all necessary python dependies in your Python environment:
    `pip install -r requirements.txt`
 * Run `make build_lnx`
   *(Note that the `clean` target might ask for your sudo password to delete everything from the `dist/` directory. If you're not okay with that, run the commands from the makefile yourself or consider installing via `pip` instead.)*
 * You can find the output binary in the `_dist_out/lnx/` directory.

Alternatively, if you want to go down the path of shame, a pre-compiled binary can be found in the release assets. It only depends on `glibc` so it is fairly portable for Linux standards, but this way of obtaining it is not recommended by any means.

### run directly from source

You can also just run this program on your *Python 3.9* or newer environment from source by cloning/downloading the code, entering the directory and then running
 * `<your_python> -m traceroute`
   ... where for example `<your_python>` == `python3`.
   (Note: `traceroute` is the "traceroute" directory in the source, *not* `traceroute.py` within that directory!)

## License

This project is published under the GPL v2.0 license.
Scapy, which this project uses, is published under the GPL v2.0 license, at the time of writing.
