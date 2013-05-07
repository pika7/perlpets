#!/usr/bin/perl -T
use strict;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);

my @retrieve_cookie = cookie('ID');

my $BattleCookie = cookie
(
	#turn, EName, YourHealth, EHealth, Estrength, Eintel, Eres, Espeed 
	-name=>'BATTLE',
	-value=>['1', "SLIME", '100', '100', '3', '4','10','10'],
	-expires=>'+1y'
);



if (@retrieve_cookie) 
{	
	print header(-cookie=>$BattleCookie);
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
	print a( {-href=>"cookietest.cgi"}, "Bath"); 
	print br;
	
	print "</DIV>";
	
	
	print "<div class=\"Status\">\n";
	print p({-align=>'center'},"$retrieve_cookie[1]'s status");
	print br;
	
	print "<b>";
	print p({-align=>'center'},"---Battle Status---");
	print "</b>";
	
	print p({-align=>'center'},"STRENGTH: $retrieve_cookie[2]");
	print p({-align=>'center'},"INTELLIGENCE: $retrieve_cookie[3]");
	print p({-align=>'center'},"RESILLIENCE: $retrieve_cookie[4]");	
	print p({-align=>'center'},"SPEED: $retrieve_cookie[5]");
	print br;
	
	print "<b>";
	print p({-align=>'center'},"---Battle Record---");
	print "</b>";
	print p({-align=>'center'},"WON: $retrieve_cookie[6]");	
	print p({-align=>'center'},"LOST: $retrieve_cookie[7]");
	print br;
		
	print "<b>";
	print p({-align=>'center'},"---Personal Status---");
	print "</b>";
		
	print p({-align=>'center'},"MOOD: $retrieve_cookie[8]");
	print p({-align=>'center'},"HUNGER: $retrieve_cookie[9]");
	print p({-align=>'center'},"CLEANLINESS: $retrieve_cookie[10]");
	print "</DIV>";
	

	
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
