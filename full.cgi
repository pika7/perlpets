#!/usr/bin/perl -T
use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my @retrieve_cookie = cookie('ID');


if (@retrieve_cookie) 
{	
	my $doEat = 0;

	# get current date and time
	my ($sec, $minute, $hour, $day, $month, $year, $wday, $yday, $isdst) = localtime(time);
	my $currDate = $hour . "_" . $day . "_" . $month . "_" . $year;

	# get the time pet was last fed
	my ($lastFedHour, $lastFedDay, $lastFedMonth, $lastFedYear) = split('_', $retrieve_cookie[9]);
	
	if ($year > $lastFedYear or $month > $lastFedMonth or $day - $lastFedDay >= 2) {
		# do nothing	
	}
	else {
		# calculate how many hours ago pet was fed
		my $hoursPassed;

		# day change
		if ($day - $lastFedDay == 1) {
			$hoursPassed = $hour + (23 - $lastFedHour);
		}
		# same day
		elsif ($day == $lastFedDay) {
			$hoursPassed = $hour - $lastFedHour;
		}
		else {
			$hoursPassed = -1;
		}

		if ($hoursPassed >= 3) {
			$doEat = 1;
		}
	}

	if ($doEat) {
		# set cookie
		my $cookie = cookie
		(
			-name=>'ID',
			-value=>["$retrieve_cookie[0]","$retrieve_cookie[1]","$retrieve_cookie[2]","$retrieve_cookie[3]", "$retrieve_cookie[4]", "$retrieve_cookie[5]", "$retrieve_cookie[6]", "$retrieve_cookie[7]","$retrieve_cookie[8]","$currDate","$retrieve_cookie[10]"],
			-expires=>'+1y'
		);

		print header(-cookie=>$cookie);
	}
	else {
		print header();
	}

	print start_html("PerlPets - Your pet is full!");
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
	

	if($retrieve_cookie[0] eq "puffy")
	{
		print "<center>";
		if ($doEat) {
			print img {src=>'img/puffy/puffy_happy.png'};
			print img {src=>'img/meat.png'};
		}
		else {
			print img {src=>'img/puffy/puffy_normal.png'};
		}
		print "</center>";
	}
	else
	{
		print "<center>";
		if ($doEat) {
			print img {src=>'img/turdle/turdle_happy.png'};
			print img {src=>'img/meat.png'};
		}
		else {
			print img {src=>'img/turdle/turdle_normal.png'};
		}
		print "</center>";
	}

	print "</DIV>";
	
	# stuff
	if ($doEat) {
		print p("$retrieve_cookie[1] enjoyed its meal!");
	}
	else {
		print p("$retrieve_cookie[1] is too full to eat!");
	}
	# end stuff	

	end_html;
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
