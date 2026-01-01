#!/bin/bash
  cd "$(dirname "$0")"
  docker-compose up -d
  echo "Nginx running at http://pi.local"