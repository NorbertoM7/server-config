  #!/bin/bash
  cd "$(dirname "$0")"
  docker-compose up -d
  echo "Trilium running at http://pi.local:8080"
