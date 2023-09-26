# This script configures a server with nginx.

package { 'nginx':
    provider => 'apt-get',
}

exec { 'allow_nginx':
  command => 'ufw allow "Nginx Full"',
  require => [Package['ufw'], Service['ufw']],
}

exec { 'hello_world':
  command => 'echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html > /dev/null',
  creates => '/var/www/html/index.nginx-debian.html',
  require => [Package['nginx'], Service['nginx']],
}

exec { '404_file':
  command => 'echo "Ceci n'est pas une page" | sudo tee /usr/share/nginx/html/404.html',
  creates => '/usr/share/nginx/html/404.html',
  require => Package['nginx'],
}

exec { 'configure_redirection':
  command => 'sudo sed -i "/listen 80 default_server/a location /redirect_me {\n  return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n}" /etc/nginx/sites-available/default',
  require => Package['nginx'],
}

exec { 'configure_404':
  command => 'sudo sed -i '/listen 80 default_server/a error_page 404 /404.html;\n \tlocation = /404.html {\n \t\troot /usr/share/nginx/html; \n\t\tinternal;\n    \t}' /etc/nginx/sites-available/default',
  require => Package['nginx'],
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}
