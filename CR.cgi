#!/usr/bin/perl -T
use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my @retrieve_cookie = cookie('ID');

if (@retrieve_cookie) 
{
	print header;
	print start_html;
	print h1("PerlPets");
	print '<link rel="stylesheet" type="text/css" href="css/main.css">';
	
	foreach my $i (@retrieve_cookie) 
{
	if($i=='')
	{
	 $i = '0';
	}
}
	
	
	print ("$retrieve_cookie[0] \n");
	print ("$retrieve_cookie[1] \n");
	print ("$retrieve_cookie[2] \n");
	print ("$retrieve_cookie[3] \n");
	print ("$retrieve_cookie[4] \n");
	print ("$retrieve_cookie[5] \n");

	
	# print p("Cookie value is $retrieve_cookie[0], $retrieve_cookie[1], $retrieve_cookie[2], $retrieve_cookie[3], $retrieve_cookie[4], $retrieve_cookie[5] \n");
	end_html;
	exit;
}
else 
{
	print header;
	print start_html;
	print h1("PerlPets");
	print '<link rel="stylesheet" type="text/css" href="css/main.css">';
	print p("This is your first time visiting PerlPets! Make a new pet before start playing the game. \n");
	print a( {-href=>"form.cgi"}, "Make a NEW pet"); 
	end_html;
	exit;
}
