## Installation

```console
# clone the repo
$ git clone https://github.com/luciano-levy/freeintruder

# change the working directory
$ cd freeintruder

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage

```console
$ python3 freeintruder.py --help


    ___                       _                                  _               
   / __)                     | |          _                     | |              
 _| |__   ____  _____  _____ | | ____   _| |_   ____  _   _   __| | _____   ____ 
(_   __) / ___)| ___ || ___ || ||  _ \ (_   _) / ___)| | | | / _  || ___ | / ___)
  | |   | |    | ____|| ____|| || | | |  | |_ | |    | |_| |( (_| || ____|| |    
  |_|   |_|    |_____)|_____)|_||_| |_|   \__)|_|    |____/  \____||_____)|_|    
                                                                                 

Version: 0.0.1
Creator: lmtlevie
                                                              
usage: freeintruder.py [-h] [--version] [--verbose] [--format {curl,file,text}]
                       [-t MARKER] [--match MATCH_STRING] [--no-content-lenght]
                       [--redirections] [--concurrents CONCURRENTS] [--delay DELAY]
                       REQUEST [REQUEST ...] PAYLOADS [PAYLOADS ...]
                       {sniper,parallel,pitchfork,cluster}

positional arguments:
  REQUEST               The request to be parameterized,
  PAYLOADS              One or more payloads sets
  {sniper,parallel,pitchfork,cluster}
                        Select attack type

optional arguments:
  -h, --help            show this help message and exit
  --version             Display version information and dependencies.
  --verbose, -v, -d, --debug
                        Display extra debugging information and metrics.
  --format {curl,file,text}, -f {curl,file,text}
                        Select in wich format the request is
  -t MARKER, --marker MARKER
                        Marker where the text inside is parameterized, default $
  --match MATCH_STRING, -m MATCH_STRING
                        Match text in response
  --no-content-lenght   Dont auto update Content-Lenght header
  --redirections        Follow redirections
  --concurrents CONCURRENTS
                        How many concurrent requests
  --delay DELAY         Delay between requests
```
