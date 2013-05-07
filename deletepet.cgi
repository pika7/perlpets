#!/usr/local/bin/perl -w
# deletes your pet
use CGI qw(:standard);
use CGI::Carp 'fatalsToBrowser';
use CGI::Cookie;
use strict;

# delete the cookie
my $q = CGI->new;
my $cookie = $q->cookie (
                -name    => 'ID',
                -value   => '',
                -path    => '/',
                -expires => '-1d'
 );

print $q->header(-cookie => $cookie);
print start_html("PerlPets - Pet Deleted");
print h1("PerlPets");
print '<link rel="stylesheet" type="text/css" href="css/main.css">';

print "</DIV>";

print p("Your pet has successfully been deleted.");
print p('Click <a href="main.cgi">here</a> to go back to the main page.');

print end_html();