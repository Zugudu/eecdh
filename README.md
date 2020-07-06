# eecdh
Utility for manual use EECDH protocol. You can use this utility if you need to manually exchange keys according to the EECDH protocol.
# Command Line Arguments
 * -dh *public_key* [*share_key*] — computate sahred key with EECDH and save to *share_key*
 * -g [name] — generate key's pair and save in *name* and *name.pub*
 * -h — help page
# Plans
 * [x] Add EEC key generation and saving
 * [ ] Add key importing from file
 * [ ] Add key importing from stdin
 * [ ] Add EECDH (_plans to use SHA256 as hash_)
 * [ ] Add ChaCha20+Poly1305
