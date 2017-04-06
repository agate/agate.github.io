title: ssh-keygen usage
date: 2016-05-17 10:08:39
tags:
---

生成一个 fingerprint
ssh-keygen -E md5 -lf $pubkey

生成 pub key
ssh-keygen -yf $privatekey

加密解密
xxx | openssl des3 -e -k 'pass'
xxx | openssl des3 -d -k 'pass'
