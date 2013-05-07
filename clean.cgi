#!/usr/bin/perl -T
use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my @retrieve_cookie = cookie('ID');


if (@retrieve_cookie) 
{	
	# get current date and time
	my ($sec, $minute, $hour, $day, $month, $year, $wday, $yday, $isdst) = localtime(time);
	my $currDate = $hour . "_" . $day . "_" . $month . "_" . $year;
	
	my $cookie = cookie
	(
		-name=>'ID',
		-value=>["$retrieve_cookie[0]","$retrieve_cookie[1]","$retrieve_cookie[2]","$retrieve_cookie[3]", "$retrieve_cookie[4]", "$retrieve_cookie[5]", "$retrieve_cookie[6]", "$retrieve_cookie[7]","$retrieve_cookie[8]","$retrieve_cookie[9]","$currDate"],
		-expires=>'+1y'
	);

	print header(-cookie=>$cookie);
	print '<script src="js/open_window.js"></script>';
	print start_html("PerlPets - Your pet is clean!");
	print h1("PerlPets");
	print '<link rel="stylesheet" type="text/css" href="css/main.css">';

	
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
	
	if($retrieve_cookie[0] eq "puffy")
	{
		print "<center>";
		print img {src=>'img/puffy/puffy_happy.png'};
		print "</center>";
	}
	else
	{
		print "<center>";
		print img {src=>'img/turdle/turdle_happy.png'};
		print "</center>";
	}

	print "</DIV>";
	
	# stuff
	print p("Your pet is now clean!");
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
