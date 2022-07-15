from requests import request
import uncurl
import pytest

request = "curl -i -s -k -X $'GET' \
    -H $'Host: www.shodan.io' -H $'Sec-Ch-Ua: \"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"' -H $'Sec-Ch-Ua-Mobile: ?0' -H $'Sec-Ch-Ua-Platform: \"Linux\"' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: %Mozilla%/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-User: ?1' -H $'Sec-Fetch-Dest: document' -H $'Referer: https://www.shodan.io/' -H $'Accept-Encoding: %gzip%, deflate' -H $'Accept-Language: en-US,en;q=0.9' \
    $'https://www.shodan.io/search?query=%solid-snake%'"

marker = "%"
r = uncurl.parse_context(request)

payloads = ["/home/lucio/InfoSec/LISTS/digits.txt"]

def test_sum():
    
    assert (1 == 2)
    
