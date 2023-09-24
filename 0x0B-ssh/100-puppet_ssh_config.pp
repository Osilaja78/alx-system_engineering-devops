# Define SSH client configuration file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Disable password authentication and configure identity file
file_line { 'Turn off passwd auth':
  path   => $ssh_config_file,
  line   => 'PasswordAuthentication no',
  match  => '^PasswordAuthentication',
  ensure => present,
}

file_line { 'Declare identity file':
  path   => $ssh_config_file,
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?\s*IdentityFile',
  ensure => present,
}
