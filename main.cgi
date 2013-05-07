#!/usr/bin/perl -T
use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my @retrieve_cookie = cookie('ID');

my $BattleCookie = cookie
(
	#turn, EName, YourHealth, EHealth, Estrength, Eintel, Eres, Espeed, damagetoYOu, damagetoE
	-name=>'BATTLE',
	-value=>['1', "SLIME", '100', '100', '3', '4','10','10'],
	-expires=>'+1y'
);

if (@retrieve_cookie) 
{	
	print header(-cookie=>$BattleCookie);
	print start_html("PerlPets - Main page");
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
	
	my $moodIndicator = "Normal";
	if($retrieve_cookie[8]==0)
	{
		$moodIndicator = "Normal";
	}
	

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
	print a( {-href=>"settings.cgi"}, "Demo settings"); 

	if($retrieve_cookie[0] eq "puffy")
	{
		print "<center>";
		if($retrieve_cookie[6] > $retrieve_cookie[7])
		{
			$moodIndicator = "HAPPY";
			print img {src=>'img/puffy/puffy_happy.png'};
		}
		else
		{
			$moodIndicator = "NORMAL";
			print img {src=>'img/puffy/puffy_normal.png'};
		}
		print "</center>";
	}
	else
	{
		print "<center>";
		if($retrieve_cookie[6] > $retrieve_cookie[7])
		{
			$moodIndicator = "HAPPY";
			print img {src=>'img/turdle/turdle_happy.png'};
		}
		else
		{
			$moodIndicator = "NORMAL";
			print img {src=>'img/turdle/turdle_normal.png'};
		}
		print "</center>";
	}
	
	print "</DIV>";
	
	
	print "<div class=\"Status\">\n";
	print p({-align=>'center'}, h2("$retrieve_cookie[1]'s status"));
	print br;
	
	print "<b>";
	print p({-align=>'center'}, h3("Battle Status"));
	print "</b>";
	
	print p({-align=>'center'},"STRENGTH: $retrieve_cookie[2]");
	print p({-align=>'center'},"INTELLIGENCE: $retrieve_cookie[3]");
	print p({-align=>'center'},"RESILLIENCE: $retrieve_cookie[4]");	
	print p({-align=>'center'},"SPEED: $retrieve_cookie[5]");
	print br;
	
	print "<b>";
	print p({-align=>'center'}, h3("Battle Record"));
	print "</b>";
	print p({-align=>'center'},"WON: $retrieve_cookie[6]");	
	print p({-align=>'center'},"LOST: $retrieve_cookie[7]");
	print br;
		
	print "<b>";
	print p({-align=>'center'}, h3("Personal Status"));
	print "</b>";
	print p({-align=>'center'},"MOOD: $moodIndicator ");

	# get current date and time
	my ($sec, $minute, $hour, $day, $month, $year, $wday, $yday, $isdst) = localtime(time);

	# calculate hunger and cleanliness by how long ago the pet was last fed or bathed
	# hunger
	my ($lastFedHour, $lastFedDay, $lastFedMonth, $lastFedYear) = split('_', $retrieve_cookie[9]);
	my $hunger;

	if ($year > $lastFedYear) {
		$hunger = "Starving";
	}
	elsif ($month > $lastFedMonth) {
		$hunger = "Starving";
	}
	elsif ($day - $lastFedDay >= 2) {
		$hunger = "Starving";
	}
	else {
		# calculate how many hours passed since pet last fed
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

		# set the hunger level
		if ($hoursPassed >= 12) {
			$hunger = "Starving";
		}
		elsif ($hoursPassed >= 9) {
			$hunger = "Very hungry";
		}
		elsif ($hoursPassed >= 6) {
			$hunger = "Hungry"
		}
		elsif ($hoursPassed >= 3) {
			$hunger = "Fine"
		}
		elsif ($hoursPassed >= 2) {
			$hunger = "Full"
		}
		elsif ($hoursPassed >= 0) {
			$hunger = "Stuffed"
		}
		else {
			$hunger = "Error";
		}
	}

	print p({-align=>'center'},"HUNGER: $hunger");

	# cleanliness
	my ($lastBathedHour, $lastBathedDay, $lastBathedMonth, $lastBathedYear) = split('_', $retrieve_cookie[10]);
	my $cleanliness;

	if ($year > $lastBathedYear) {
		$cleanliness = "Filthy";
	}
	elsif ($month > $lastBathedMonth) {
		$cleanliness = "Filthy";
	}
	elsif ($day - $lastBathedDay >= 2) {
		$cleanliness = "Filthy";
	}
	else {
		# calculate how many hours passed since pet last fed
		my $hoursPassed;

		# day change
		if ($day - $lastBathedDay == 1) {
			$hoursPassed = $hour + (23 - $lastBathedHour);
		}
		# same day
		elsif ($day == $lastBathedDay) {
			$hoursPassed = $hour - $lastBathedHour;
		}
		else {
			$hoursPassed = -1;
		}

		# set the cleanliness level
		if ($hoursPassed >= 12) {
			$cleanliness = "Filthy";
		}
		elsif ($hoursPassed >= 9) {
			$cleanliness = "Very dirty";
		}
		elsif ($hoursPassed >= 6) {
			$cleanliness = "Dirty"
		}
		elsif ($hoursPassed >= 3) {
			$cleanliness = "Normal"
		}
		elsif ($hoursPassed >= 2) {
			$cleanliness = "Clean"
		}
		elsif ($hoursPassed >= 0) {
			$cleanliness = "Sparkling"
		}
		else {
			$cleanliness = "Error";
		}
	}

	print p({-align=>'center'},"CLEANLINESS: $cleanliness");

	print "</DIV>";
	

	
	end_html;
	exit;
}
else 
{
	print header;
	print start_html("PERLPETS-Main Page");
	print h1("PerlPets");
	print '<link rel="stylesheet" type="text/css" href="css/main.css">';
	print p("This is your first time visiting PerlPets! Make a new pet before start playing the game. \n");
	print a( {-href=>"form.cgi"}, "Make a NEW pet"); 
	end_html;
	exit;
}
