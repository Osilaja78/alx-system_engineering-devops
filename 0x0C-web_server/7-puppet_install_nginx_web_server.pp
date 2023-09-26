# This scritp configures nginx for a server.

package {'nginx':
  ensure => 'present',
}

exec {'update_and_install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello_world':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}

exec { 'sudo sed -i "/listen 80 default_server/a error_page 404 /404.html;\n \tlocation = /404.html {\n \t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}" /etc/nginx/sites-available/default':
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
