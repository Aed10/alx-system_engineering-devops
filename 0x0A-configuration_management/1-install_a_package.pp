# Ensure Flask and Werkzeug are installed via pip3
package { 'pip3':
  ensure   => installed,
}

exec { 'install_flask_and_werkzeug':
  command     => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path        => ['/usr/bin', '/usr/local/bin'],
  environment => 'PATH=/usr/bin:/usr/local/bin',
  unless      => '/usr/bin/pip3 freeze | grep -q "Flask==2.1.0" && /usr/bin/pip3 freeze | grep -q "Werkzeug==2.1.1"',
}
