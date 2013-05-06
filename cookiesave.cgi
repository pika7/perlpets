#!/usr/bin/perl -T
use strict;

use CGI qw/:standard/;

my $cookie = cookie(
	-name=>'ID',
	value=>['hahdaaa','lol'],
	-expires=>'+1y');
	
	# print header (-cookie=>$cookie);
	#start_html('CGI Cookie with Exipire Date'),
	#p("Cookie had been saved !\n"),
	#end_html;

exit;