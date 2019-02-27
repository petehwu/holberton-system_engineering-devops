# puppet file to make sure file exist and fix typo in file
file {'/var/www/html/wp-settings.php':
  ensure => present
}
-> exec { 'fix_php':
  path    => '/bin',
  command => 'sed -i --follow-symlinks s/phpp/php/ /var/www/html/wp-settings.php'
}
