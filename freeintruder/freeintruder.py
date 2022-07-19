#! usr/bin/env python3

from argparse import ArgumentParser,RawDescriptionHelpFormatter
from nis import match
import requests
import platform
import uncurl
import attacks
import async_req
import match

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
Author: lmtlevie
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
                        metavar="REQUEST",
                        action="store",
                        help="The request to be parameterized,") # multiple in the future
    parser.add_argument("attack",
                        action="store",
                        choices=["sniper","parallel","pitchfork","cluster"],
                        default="sniper",
                        help="Select attack type")
    parser.add_argument("payloads",
                        nargs="+",metavar="PAYLOADS",
                        action="extend",
                        help="""One or more payloads sets file,
                        notice the order that follows: method,
                        url,
                        data,
                        headers,
                        cookies,
                        verify,
                        auth""")
    parser.add_argument("--version",
                        action="version", version=version_string,
                        help="Display version information and dependencies."
                        )
    parser.add_argument("--verbose", "-v", "-d", "--debug",
                        action="store_true", dest="verbose", default=False,
                        help="Display extra debugging information and metrics."
                        )
    parser.add_argument("-t","--marker",
                        action="store",
                        dest="marker",default="%",
                        help="Marker where the text inside is parameterized, default %%")
    parser.add_argument("--match","-m",
                        action="extend",nargs="+",dest="match_string",
                        help="Match text in response")
   
    parser.add_argument("--no-content-lenght",
                        action="store_true",
                        default=False,
                        help="Dont auto update Content-Lenght header") # Todo
    parser.add_argument("--redirections",
                        action="store_true",
                        default=False,
                        help="Follow redirections")
    parser.add_argument("--concurrents",
                        action="store",
                        help="How many concurrent requests",default=10)
    parser.add_argument("--delay",
                        action="store",
                        help="Delay between requests in ms",default=0)
    parser.add_argument("--char",
                        action="store",default="",
                        help="Delete trailing character") # BURP add $ 
    
    args = parser.parse_args()
    
    args.request = (args.request).replace(args.char,"")
    
    r = uncurl.parse_context(args.request)
    
    total_reqs = attacks.attack_starter(r._asdict(),args.attack,args.payloads,args.marker)

    responses = async_req.main(total_reqs,args.concurrents,args.delay,args.redirections)
    
    match.matcher(responses,args.match_string)
      
    
if __name__ == "__main__":
    main()

