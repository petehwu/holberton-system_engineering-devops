# Puppet manifest file that installs a package
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
  name     => 'puppet-lint',
}
