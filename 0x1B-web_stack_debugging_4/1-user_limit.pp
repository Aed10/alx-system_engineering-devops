# Ensure that the 'holberton' user has sufficient file limits

# Add or modify the hard file limit for the 'holberton' user
exec { 'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/^holberton hard/ {s/^[^ ]* [^ ]* /holberton hard nofile /; s/[0-9][0-9]* /50000 /}" /etc/security/limits.conf',
  path    => '/usr/bin/',  # Assuming sed is in /usr/bin/
}

# Add or modify the soft file limit for the 'holberton' user
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/ {s/^[^ ]* [^ ]* /holberton soft nofile /; s/[0-9][0-9]* /50000 /}" /etc/security/limits.conf',
  path    => '/usr/bin/',  # Assuming sed is in /usr/bin/
}
