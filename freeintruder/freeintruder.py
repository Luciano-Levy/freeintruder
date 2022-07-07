#! usr/bin/env python3

from argparse import ArgumentParser,RawDescriptionHelpFormatter
import requests
import platform

module_name = "FreeIntruder: quickly and free http request parametrizer"
__version__ = "0.0.1"

def print_banner():
        banner = '''

    ___                       _                                  _               
   / __)                     | |          _                     | |              
 _| |__   ____  _____  _____ | | ____   _| |_   ____  _   _   __| | _____   ____ 
(_   __) / ___)| ___ || ___ || ||  _ \ (_   _) / ___)| | | | / _  || ___ | / ___)
  | |   | |    | ____|| ____|| || | | |  | |_ | |    | |_| |( (_| || ____|| |    
  |_|   |_|    |_____)|_____)|_||_| |_|   \__)|_|    |____/  \____||_____)|_|    
                                                                                 

Version: 0.0.1
Creator: lmtlevie
                                                              '''

        print(banner)


def main():
    # agregate all dependencies
    version_string = f"%(prog)s {__version__}\n" + \
                     f"{requests.__description__}:  {requests.__version__}\n" + \
                     f"Python:  {platform.python_version()}"

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            description=print_banner())
    parser.add_argument("request",
                        nargs="+",metavar="REQUEST",
                        action="store",
                        help="The request to be parameterized,")
    parser.add_argument("payloads",
                        nargs="+",metavar="PAYLOADS",
                        action="store",
                        help="One or more payloads sets")
    parser.add_argument("--version",
                        action="version", version=version_string,
                        help="Display version information and dependencies."
                        )
    parser.add_argument("--verbose", "-v", "-d", "--debug",
                        action="store_true", dest="verbose", default=False,
                        help="Display extra debugging information and metrics."
                        )
    parser.add_argument("--format","-f",
                        action="store",dest="format",
                        choices=["curl","file","text"],default="curl",
                        help="Select in wich format the request is")
    parser.add_argument("-t","--marker",
                        action="store",
                        dest="marker",default="$",
                        help="Marker where the text inside is parameterized, default $")
    parser.add_argument("--match","-m",
                        action="store",dest="match_string",
                        help="Match text in response")
    parser.add_argument("attack",
                        action="store",
                        choices=["sniper","parallel","pitchfork","cluster"],
                        default="sniper",
                        help="Select attack type")
    parser.add_argument("--no-content-lenght",
                        action="store_true",dest="no-content-lenght",
                        default=False,
                        help="Dont auto update Content-Lenght header")
    parser.add_argument("--redirections",
                        action="store_true",dest="redirections",
                        default=False,
                        help="Follow redirections")
    parser.add_argument("--concurrents",
                        action="store",
                        help="How many concurrent requests")
    parser.add_argument("--delay",
                        action="store",
                        help="Delay between requests")
    args = parser.parse_args()

if __name__ == "__main__":
    main()
