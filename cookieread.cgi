#!/usr/local/bin/perl -w
use CGI qw(:standard);
use CGI::Carp 'fatalsToBrowser';
use CGI::Cookie;
use strict;

# see if you can read a cooie

# send the cookie to the browser
print header();

print start_html("Cookie read");

my %cookies = CGI::Cookie->fetch;
	for (keys %cookies) {
	   print($cookies{$_});
    }

print end_html();