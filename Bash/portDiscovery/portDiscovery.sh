#!/bin/bash

for port in $(seq 1 65535); do
  timeout 1 bash -c "echo '' > /dev/tcp/127.0.0.1/$port" 2>/dev/null && echo "[+]Port $port Open" & 
done; wait  