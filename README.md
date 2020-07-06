# eecdh
Utility for manual use EECDH protocol. You can use this utility if you need to manually exchange keys according to the EECDH protocol.
# Command Line Arguments
 * -dh *public_key* [*share_key*] — computate sahred key with EECDH and save to *share_key*
 * -g — generate key's pair and save in *name* and *name.pub*
 * -h — help page
 * -t [PEM|DER] — set output format
 * -n name — set output file name
# Plans
 * [x] Add EEC key generation and saving
 * [x] Add key importing
 * [x] Add ECDH
 * [ ] Add HKDF with SHA256 v2
 * [ ] Add ChaCha20+Poly1305
