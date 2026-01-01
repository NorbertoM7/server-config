  #!/bin/bash
  set -e

  echo "=== Stopping all containers ==="
  docker stop $(docker ps -aq) 2>/dev/null || true
  docker rm $(docker ps -aq) 2>/dev/null || true

  echo "=== Removing Docker ==="
  sudo apt remove docker.io docker-compose -y
  sudo apt autoremove -y

  echo "=== Removing user from docker group ==="
  sudo deluser $USER docker 2>/dev/null || true

  echo "=== Teardown complete! ==="