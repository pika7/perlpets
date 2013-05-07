#!/usr/bin/perl -T
use strict;
use CGI qw/:standard/;
use CGI::Carp 'fatalsToBrowser';
use URI;

my @retrieve_cookie = cookie('ID');
my @battle_cookie = cookie('BATTLE');

my $newTurn = $battle_cookie[0]+1; 
print "$newTurn";


my $BattleCookie = cookie
(
	#turn, EName, YourHealth, EHealth, Estrength, Eintel, Eres, Espeed 
	-name=>'BATTLE',
	-value=>["$newTurn", "SLIME", '100', '100', '3', '4', '10', '10'],
	-expires=>'+1y'
);

print header(-cookie=>$BattleCookie);

print start_html("Pet Battle-PERLPETS");

print '<link rel="stylesheet" type="text/css" href="css/main.css">';

print h1("PerlPets");
print h2("Pet Battle");



print p("<CENTER><b>- TURN $battle_cookie[0] - </b></CENTER>");

print p("<b>$battle_cookie[1]</b> wants to fight!");

print img {src=>'img/puffy/puffy_normal.png',align=>'LEFT', height=>'100', width=>'100'};

print img {src=>'img/turdle/turdle_normal.png',align=>'RIGHT', height=>'100', width=>'100'};
print br;
print br;
print br;
print br;
print br;
print p("<b>My Health: $battle_cookie[2]</b>");
print br;
print "<DIV align=RIGHT>";
print p("<b>Enemy Health: $battle_cookie[3]</b>");
print "</DIV>";



print br;
print br;
print br;
print p("WHAT ARE YOU GOING TO DO???????");

print p("<b>Punch</b>: Physical Damage");
print p("<b>Magic</b>: Magical damage based on intelligence");
print p("<b>Defend</b>: Counters damage based on Resillience");
print p("<b>MagicBarrier</b>: Counters magical damage based on speed ");

print hr, start_form;
print radio_group(-name=>"battleoption", -values => ["Punch", "Magic", "Defend", "MagicBarrier"]);

my $attackMode = param("battleoption");

print p(submit("TAKE YOUR ACTION!"));

if(param())
{
		my $uri = URI->new('yourAttack.cgi');
		
		$uri->query_form
		(
			attack => $attackMode
		);
		print "<META HTTP-EQUIV=refresh CONTENT=\"1 URL='$uri'\">\n";
}


print end_form, hr;
end_html;
exit;
	