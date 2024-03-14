# httpTimeSync
## Intro
Implement linux date-time sync by using HTTP protocol instead of ntp. 
The time reference is from https://worldtimeapi.org.
Suitable for server that cannot sync directly to public NTP server due to any restrictions in internal network.

## Configuration
Please update the URL inside script with your own timezone.

example: 

* Taipei: https://worldtimeapi.org/api/timezone/Asia/Taipei.json
* Jakarta: https://worldtimeapi.org/api/timezone/Asia/Jakarta.json
* UTC: https://worldtimeapi.org/api/UTC

This script also calculate total processing time start from script run until result received from server.
This processing time then sum-up with timestamp received from time server. 

## Python implementation
```bash
python httpTimeSync.py

Return TS from server    : 1710394790
Server response time     : 1.053541660308838 seconds
Apply TS to localhost    : 1710394791.0535417
1710394791.053541700
Done.

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Thank you
