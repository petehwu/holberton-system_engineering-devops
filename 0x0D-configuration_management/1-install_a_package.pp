# Puppet manifest file that installs a package
package { 'puppet-lint':
  provider        => 'gem',
  name            => 'puppet-lint',
  ensure          => '2.1.1'
}
