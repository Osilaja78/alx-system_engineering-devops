# This puppet scrilpt changes the ULIMIT for nginx.

file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT=\"-n 4096\"\n",
  notify  => Exec['restart-nginx'],
}

exec { 'restart-nginx':
  command => 'service nginx restart',
  path    => '/usr/bin',
}
