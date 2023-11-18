# Changes user limit for holberton user.

exec { 'increase-hard-for-holberton':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/bin',
}

exec { 'increase-soft-for-holberton':
  command => "sed -i '/^holberton soft/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/bin',
}
