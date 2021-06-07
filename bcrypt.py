# This is a solver for Lunizz CTF, TryHackMe
import bcrypt
import base64
import codecs
import tqdm

# salt: 22 letters from 3rd $
salt = b'$2b$12$LJ3m4rzPGmuN1U/h0IO55.' #change this
hashed = b'$2b$12$LJ3m4rzPGmuN1U/h0IO55.3h9WhI/A0Rcbchmvk10KWRMWe4me81e' #change this

# change wordlist to your own
with codecs.open("/usr/share/wordlists/rockyou.txt",'r',encoding='utf-8',errors='ignore') as f:
        for x in tqdm.tqdm(f.readlines()):
                passd = x.strip().encode('ascii', 'ignore')
                based = base64.b64encode(passd)
                newHashed = bcrypt.hashpw(based, salt)

                if hashed == newHashed:
                        print("password: %s" % x)
                        break
