# eecdh
Utility for manual use EECDH protocol. You can use this utility if you need to manually exchange keys according to the EECDH protocol.
# Command Line Arguments

 * -dh [-k -i -n -t -l] — computate shared key with ECDH+HKDF and save to *name*
 * -pdh [-k -i -n -t] — computate shared key with pure ECDH and save to *name*
 * -g — generate key's pair and save it DEFAULT=key[.pub]
 * -h — help page
 * -t [PEM|DER] — set output/imported key type DEFAULT=PEM
 * -n name	— set output file name
 * -i peer_key	— import peer public key from peer_key
 * -k key — import private key DEFAULT=key
 * -l key_length — set key length in bytes for KDF DEFAULT=32
# Plans
 * [x] Add EEC key generation and saving
 * [x] Add key importing
 * [x] Add ECDH
 * [x] Add HKDF with SHA256 v2
 * [ ] Add ChaCha20+Poly1305
