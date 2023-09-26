# This script configures an nginx server.

package { 'nginx':
    ensure => installed
}

file {'/usr/share/nginx/html/404.html':
    content => 'Ceci n\'est pas une page',
    mode    => '0644'
}

file { '/etc/nginx/sites-available/default':
    content => "server {
    	listen 80 default_server;

    	root /usr/share/nginx/html;
    	index index.html index.htm;

    	location / {
        	try_files \$uri \$uri/ =404;
    	}

    	error_page 404 /404.html;
    	location = /404.html {
		root /usr/share/nginx/html;
        	internal;
    	}

    	location /redirect_me {
        	return 301 https://www.example.com/; # Change this URL to your desired destination
    	}
	}
	",
    notify  => Service['Nginx']
}

service {'nginx':
    ensure => running,
    enable => true
}
