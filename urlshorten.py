#!/usr/bin/env python3.8

import base64
import hashlib
import sqlite3

def to_raw(s):
  return b"{s}"

def generate_hash(url):
  url = to_raw(url)
  shad = hashlib.sha256()
  shad.update(url)
  return shad

def encode_hash(shad):
  return base64.b64encode(shad.digest())

def key_from_url(url, length=10):
  hash = generate_hash(url)
  ehash = encode_hash(hash)
  return ehash[:length]

def add_url(url):
  key = key_from_url(url)
  conn = sqlite3.connect("sql/urls.db")
  curs = conn.cursor()
  sql = "insert into URLS values ('" + key + "', '" + url + "');"
  print(sql)
  conn.close()

def main():
  url = "https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR"
  add_url(url)

if __name__ == '__main__':
  main()
