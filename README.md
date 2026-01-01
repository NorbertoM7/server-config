  # Server Config

  Pi server setup with Docker.

  ## Fresh install

  ```bash
  git clone https://github.com/YOURUSERNAME/server-config.git ~/server-config
  cd ~/server-config
  chmod +x setup.sh teardown.sh apps/*/up.sh apps/*/down.sh
  ./setup.sh
  # log out and back in

  Start apps

  cd ~/server-config/apps/nginx
  ./up.sh

  Stop apps

  cd ~/server-config/apps/nginx
  ./down.sh

  Full teardown

  cd ~/server-config
  ./teardown.sh