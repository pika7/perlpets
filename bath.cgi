#!/usr/bin/perl -T
use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my @retrieve_cookie = cookie('ID');


if (@retrieve_cookie) 
{	
	print header();
	print '<script src="js/open_window.js"></script>';
	print start_html("PerlPets - Take a bath!");
	print h1("PerlPets");
	print '<link rel="stylesheet" type="text/css" href="css/main.css">';
	
	print "<div class=\"Actions\">\n";
	print a( {-href=>"main.cgi"},"My Pet's status"); 
	print br;
	print a( {-href=>"battle.cgi"}, "Battle"); 
	print br;
	print a( {-href=>"train.cgi"}, "Train"); 
	print br;
	print a( {-href=>"eat.cgi"}, "Eat"); 
	print br;
	print a( {-href=>"bath.cgi"}, "Bath"); 
	print br;
	
	print "</DIV>";
	

	if($retrieve_cookie[0] eq "puffy")
	{
		print "<center>";
		print img {src=>'img/puffy/puffy_normal.png'};
		print "</center>";
	}
	else
	{
		print "<center>";
		print img {src=>'img/turdle/turdle_normal.png'};
		print "</center>";
	}

	# stuff
	print p('<a href=\'javascript:open_window("PerlPets - Bath Time!", "bath.html", 100, 100, 500, 400, 0, 0, 0, 0, 0)\'>Click here to take a bath.</a>');

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
