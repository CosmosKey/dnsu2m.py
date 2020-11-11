#!/usr/bin/env python3
import socket
import dnslib

# Global variables
IP = socket.gethostbyname(socket.gethostname()) 
PORT = 53

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))
    print("DNS Listening on {0}:{1} ...".format(IP, PORT))
    while True:
        data, address = sock.recvfrom(650)
        d = dnslib.DNSRecord.parse(data)
        print('\n')

        print(d)
        try:
            r = socket.gethostbyname(d.q.qname.__str__())
            if d.a.rtype != dnslib.QTYPE.A:
                continue
        except:
            
            dr = dnslib.DNSRecord(dnslib.DNSHeader(qr=1,aa=0,ra=0,id=d.header.id),q=d.q, a=None)
            p = dr.pack()
            print('\n')
            print('Send:')
            print(dr)
            sock.sendto(p, address)
            continue
        dr = dnslib.DNSRecord(
                dnslib.DNSHeader(qr=1,aa=1,ra=1,id=d.header.id),
                q=d.q,
                a=dnslib.RR(d.q.qname.__str__(),rdata=dnslib.A(r)))
        p = dr.pack()
        print('\n')
        print('Send:')
        print(dr)
        sock.sendto(p, address)
        


if __name__ == "__main__":
    main()
