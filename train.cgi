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
	

	
	if($retrieve_cookie[2] == '')
	{
		$retrieve_cookie[2] = '0';
	}
	if($retrieve_cookie[3] == '')
	{
		$retrieve_cookie[3] = '0';
	}
	if($retrieve_cookie[4] == '')
	{
		$retrieve_cookie[4] = '0';
	}
	if($retrieve_cookie[5] == '')
	{
		$retrieve_cookie[5] = '0';
	}
	if($retrieve_cookie[6] == '')
	{
		$retrieve_cookie[6] = '0';
	}
	if($retrieve_cookie[7] == '')
	{
		$retrieve_cookie[7] = '0';
	}
	if($retrieve_cookie[8] == '')
	{
		$retrieve_cookie[8] = '0';
	}
	if($retrieve_cookie[8] == '')
	{
		$retrieve_cookie[8] = '0';
	}
	if($retrieve_cookie[9] == '')
	{
		$retrieve_cookie[9] = '0';
	}
	if($retrieve_cookie[10] == '')
	{
		$retrieve_cookie[10] = '0';
	}
	
	print ("PETTYPE  ");
	print ("$retrieve_cookie[0] \n");
	print br;
	
	print ("NAME  ");
	print ("$retrieve_cookie[1] \n");
	print br;
	
	print ("STRENGTH  ");
	print ("$retrieve_cookie[2] \n");
	print br;
	
	print ("INTELLIGENCE  ");
	print ("$retrieve_cookie[3] \n");
	print br;
	
	print ("RESILLIENCE  ");
	print ("$retrieve_cookie[4] \n");
	print br;
	
	print ("SPEED  ");
	print ("$retrieve_cookie[5] \n");
	print br;
	
	print ("WON  ");
	print ("$retrieve_cookie[6] \n");
	print br;
	
	print ("LOST  ");
	print ("$retrieve_cookie[7] \n");
	print br;
	
	print ("MOOD  ");
	print ("$retrieve_cookie[8] \n");
	print br;
	
	print ("HUNGER  ");
	print ("$retrieve_cookie[9] \n");
	print br;
	
	print ("CLEANLINESS  ");
	print ("$retrieve_cookie[10] \n");
	print br;


	
	# print p("Cookie value is $retrieve_cookie[0], $retrieve_cookie[1], $retrieve_cookie[2], $retrieve_cookie[3], $retrieve_cookie[4], $retrieve_cookie[5],$retrieve_cookie[6],$retrieve_cookie[7] \n");
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
