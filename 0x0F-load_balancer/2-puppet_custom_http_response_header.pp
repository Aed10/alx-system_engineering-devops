# A puppet manifest that automate the creating of a custom HTTP header response
#   The name of the custom HTTP header must be X-Served-By
#   The value of the custom HTTP header must be the hostname of the server Nginx is running on
#   The custom HTTP header must be added to the response of the default Nginx virtual host

exec { 'apt-update':
  command  => 'apt -y apt update && apt -y apt upgrade',
  provider => 'shell',
}
# Ensure Nginx package is installed
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
  before   => File['/etc/nginx/nginx.conf'],
}

# Add custom HTTP header to Nginx configuration
file_line { 'add_custom_header':
  ensure => present,
  line   => "add_header X-Served-By ${hostname};",
  match  => '^http {',
  after  => '^http {',
  path   => '/etc/nginx/nginx.conf',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}
