#!/usr/bin/env python3.8

import base64
import hashlib

def to_raw(s):
  return b"{s}"

def generate_hash(url):
  url = to_raw(url)
  shad = hashlib.sha256()
  shad.update(url)
  return shad

def encode_hash(shad):
  return base64.b32encode(shad.digest())

def main():
  url = "https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR"
  shad = generate_hash(url)
  enc = encode_hash(shad)
  print(enc)

if __name__ == '__main__':
  main()
