#!/usr/bin/perl -T
use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my @retrieve_cookie = cookie('ID');


if (@retrieve_cookie) 
{	
	print header();
	print start_html("PerlPets - Take a bath!");
	print h1("PerlPets");
	print '<link rel="stylesheet" type="text/css" href="css/main.css">';
	
	
	if($retrieve_cookie[0] eq "puffy")
	{
		print "<center>";
		print img {src=>'img/puffy/puffy_normal.png', height=>'100', width=>'100',align=>"CENTER"};
		print "</center>";
	}
	else
	{
		print "<center>";
		print img {src=>'img/turdle/turdle_normal.png', height=>'100', width=>'100'};
		print "</center>";
	}
	
	print "<div class=\"Actions\">\n";
	print a( {-href=>"main.cgi"},"My Pet's status"); 
	print br;
	print a( {-href=>"battle.cgi"}, "Battle"); 
	print br;
	print a( {-href=>"train.cgi"}, "Train"); 
	print br;
	print a( {-href=>"main.cgi"}, "Eat"); 
	print br;
	print a( {-href=>"bath.cgi"}, "Bath"); 
	print br;
	
	print "</DIV>";
	
	# stuff


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
