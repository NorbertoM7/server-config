  #!/bin/bash
  set -e

  echo "=== Updating system ==="
  sudo apt update && sudo apt upgrade -y

  echo "=== Installing packages ==="
  sudo apt install docker.io docker-compose git -y

  echo "=== Adding $USER to docker group ==="
  sudo usermod -aG docker $USER

  echo "=== Setup complete! ==="
  echo "Log out and back in for docker group to take effect."
  echo "Then run: cd ~/server-config/apps/nginx && ./up.sh"