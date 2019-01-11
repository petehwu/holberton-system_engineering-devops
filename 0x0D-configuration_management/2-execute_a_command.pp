# puppet manifest file that issues a pkill command
exec { 'killmenow':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  returns => '0'
}
