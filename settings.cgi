#!/usr/bin/perl -T
use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my @retrieve_cookie = cookie('ID');


if (@retrieve_cookie) 
{	
	print header();
	print start_html("PerlPets - Demo settings");
	print h1("PerlPets");
	print '<link rel="stylesheet" type="text/css" href="css/main.css">';

	# stuff
	print p("These are for demo purposes only.");
	print p('<a href="deletepet.cgi">Delete pet</a>');
	print p('<a href="makehungry.cgi">Make pet hungry</a>');
	print p('<a href="makedirty.cgi">Make pet dirty</a>');
	print p('<a href="main.cgi">Back to main</a>');

	# end stuff
	

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
