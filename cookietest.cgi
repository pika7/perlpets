#!/usr/local/bin/perl -w
use CGI qw(:standard);
use CGI::Carp 'fatalsToBrowser';
use CGI::Cookie;
use strict;

# just randomly add some cookie to the browser as a test and have a link to bath
# this cookie determines the pet type
my $cookie = CGI::Cookie->new(-name => 'pet_type',
	-value   =>  'testpet',
	-expires =>  '+12M', # 12 months
	);

# send the cookie to the browser
print header(-cookie=>$cookie);
print '<script src="js/open_window.js"></script>';

print start_html("Cookie test");

# create a link to the bath game
print '<a href=\'javascript:open_window("PerlPets - Bath Time!", "bath.html", 100, 100, 500, 400, 0, 0, 0, 0, 0)\'>bath time</a>';

print end_html();