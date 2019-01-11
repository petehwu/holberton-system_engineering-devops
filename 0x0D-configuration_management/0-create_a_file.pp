# puppet manifest file to create a temporary file
file { '/tmp/holberton':
  ensure    => file,
  path      => '/tmp/holberton',
  mode      => '0744',
  owner     => 'www-data',
  group     => 'www-data',
  content   => 'I love Puppet'
}
