# Overviews

# Commands
- Check lobal IP address
    - `curl ipecho.net/plain; echo`
- Show a manager for an IP address
    - `whois -h whois.nic.ad.jp IPAddress`
- Show a manager for a domain
    - `whois -h whois.jprs.jp DomainName`
- Show the IP address from a domain name
    - `nslookup DomainName`
- Check whether my host can send IP packets to a target host
    - `ping IPAddress`
    - `ping HostName`
- Check my host name
    - `hostname`
- Read a file
    - `cat FilePath`
- Check my network
    - `netstat`
- Check how my host uses resources
    - `top`
- Check my local IP address
    - `ifconfig`
        - search `inet`
- 