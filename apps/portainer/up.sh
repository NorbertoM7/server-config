  #!/bin/bash
  cd "$(dirname "$0")"
  docker-compose up -d
  echo "Portainer running at http://pi.local:9000"
