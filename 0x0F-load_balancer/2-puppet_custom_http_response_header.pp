# A puppet manifest that automate the creating of a custom HTTP header response
#   The name of the custom HTTP header must be X-Served-By
#   The value of the custom HTTP header must be the hostname of the server Nginx is running on
#   The custom HTTP header must be added to the response of the default Nginx virtual host

# Ensure Nginx package is installed
package { 'nginx':
  ensure  => present,
}

# Add custom HTTP header to Nginx configuration
file_line { 'add_custom_header':
  ensure => present,
  line   => "add_header X-Served-By ${hostname};",
  match  => '^http {',
  after  => '^http {',
  path   => '/etc/nginx/nginx.conf',
}

