#!/usr/local/bin/perl5 -w

use strict;
use CGI qw/:standard/;
use CGI::Carp 'fatalsToBrowser';
use URI;

srand;

my @retrieve_cookie = cookie('ID');
my @battle_cookie = cookie('BATTLE');
my $newTurn = $battle_cookie[0]+1; 

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



my $enemyAction =  int(rand(4));
my @actions = ("Punch", "Magic", "Defend", "MagicBarrier");

my @values = split(/&/,$ENV{QUERY_STRING});
my @cookieVal = (); 

foreach my $i (@values) 
{
	my($fieldname, $data) = split(/=/, $i);
	push(@cookieVal, $data);
}

my $enemyReaction = $actions[$enemyAction];
my $yourAction = $cookieVal[0];

	my $myStrength = $retrieve_cookie[2];
	my $myIntelligence = $retrieve_cookie[3];
	my $myResillience = $retrieve_cookie[4];
	my $mySpeed = $retrieve_cookie[5];
	
	
	my $yourStrength = $battle_cookie[5];
	my $yourIntelligence = $battle_cookie[6];
	my $yourResillience = $battle_cookie[7];
	my $yourSpeed = $battle_cookie[8];
	
	
	my $myNewHP = 100;
	my $yourNewHP = 100;
	

if($yourAction eq $enemyReaction)
{
	if($yourAction eq "Punch")
	{

		$myNewHP = $battle_cookie[2] - $yourStrength;
		$yourNewHP = $battle_cookie[3] - $myStrength;
	
	}
	if($yourAction eq "Magic")
	{
		$myNewHP = $battle_cookie[2] - $yourIntelligence;
		$yourNewHP = $battle_cookie[3] - $myIntelligence;

	}
	if($yourAction eq "Defend")
	{
		$myNewHP = $battle_cookie[2];
		$yourNewHP = $battle_cookie[3];
		
	}
	if($yourAction eq "MagicBarrier")
	{
		$myNewHP = $battle_cookie[2];
		$yourNewHP = $battle_cookie[3];
	}
	
}
if($yourAction eq "Punch")
{
	
	if($enemyReaction eq "Magic")
	{
		$myNewHP = $battle_cookie[2] - $yourIntelligence;
		$yourNewHP = $battle_cookie[3] - $myStrength;

	}
	if($enemyReaction eq "Defend")
	{
		$myNewHP = $battle_cookie[2] - $yourResillience;
		$yourNewHP = $battle_cookie[3];
		
	}
	if($enemyReaction eq "MagicBarrier")
	{
		$myNewHP = $battle_cookie[2];
		$yourNewHP = $battle_cookie[3] - $myStrength;
	}

}

if($yourAction eq "Magic")
{
	
	if($enemyReaction eq "Punch")
	{
		$myNewHP = $battle_cookie[2] - $yourStrength;
		$yourNewHP = $battle_cookie[3] - $myIntelligence;

	}
	if($enemyReaction eq "Defend")
	{
		$myNewHP = $battle_cookie[2];
		$yourNewHP = $battle_cookie[3] - $myIntelligence;
		
	}
	if($enemyReaction eq "MagicBarrier")
	{
		$myNewHP = $battle_cookie[2] - $yourSpeed;
		$yourNewHP = $battle_cookie[3];
	}

}
if($yourAction eq "Defend")
{
	
	if($enemyReaction eq "Punch")
	{
		$myNewHP = $battle_cookie[2];
		$yourNewHP = $battle_cookie[3] - $myResillience;

	}
	if($enemyReaction eq "Magic")
	{
		$myNewHP = $battle_cookie[2] - $yourIntelligence;
		$yourNewHP = $battle_cookie[3];
		
	}
	if($enemyReaction eq "MagicBarrier")
	{
		$myNewHP = $battle_cookie[2];
		$yourNewHP = $battle_cookie[3];
	}

}
if($yourAction eq "MagicBarrier")
{
	
	if($enemyReaction eq "Punch")
	{
		$myNewHP = $battle_cookie[2] - $yourStrength;
		$yourNewHP = $battle_cookie[3];

	}
	if($enemyReaction eq "Magic")
	{
		$myNewHP = $battle_cookie[2];
		$yourNewHP = $battle_cookie[3] - $mySpeed;
		
	}
	if($enemyReaction eq "Defend")
	{
		$myNewHP = $battle_cookie[2];
		$yourNewHP = $battle_cookie[3];
	}

}

if($myNewHP<0)
{
	$myNewHP =0;
}
if($yourNewHP<0)
{
	$yourNewHP=0;
}

my $BattleCookie = cookie
(
	#turn, EName, YourHealth, EHealth,E hp     Estrength, Eintel, Eres, Espeed
	# 0     1      2          3        4           5       6     7       8
	
	-name=>'BATTLE',
	-value=>["$newTurn", "SLIME", "$myNewHP", "$yourNewHP", '100', '3', '4','10','10'],
	-expires=>'+1y'
);

my $newWon = $retrieve_cookie[6];
my $newLost = $retrieve_cookie[7];

if($myNewHP ==0 )
{
	$newLost = $newLost + 1;
}
if($yourNewHP==0)
{
	$newWon = $newWon+1;
}


my $cookie = cookie
(
	-name=>'ID',
	-value=>["$retrieve_cookie[0]","$retrieve_cookie[1]","$retrieve_cookie[2]","$retrieve_cookie[3]", "$retrieve_cookie[4]", "$retrieve_cookie[5]", "$newWon", "$newLost","$retrieve_cookie[8]","$retrieve_cookie[9]","$retrieve_cookie[10]"],
	-expires=>'+1y'
);




print header(-cookie=>[$BattleCookie, $cookie]);


print start_html("Pet Battle-PERLPETS");

print '<link rel="stylesheet" type="text/css" href="css/main.css">';

print h1("PerlPets");
print h2("Pet Battle");

my @battle_cookie = cookie('BATTLE');





print p("<CENTER><b>- TURN $battle_cookie[0] - </b></CENTER>");



print p("YOU CHOSE <b>$cookieVal[0]!</b>");


print p("<b>$battle_cookie[1]</b> CHOSE <b>$actions[$enemyAction]!</b>");


if($yourAction eq $enemyReaction)
{
	if($yourAction eq "Punch")
	{
		print p("BOTH sides decide to punch each other!");
		print p ("$retrieve_cookie[1] receives  $yourStrength damage! $myNewHP");
		print p ("$battle_cookie[1] receives $myStrength damage! $yourNewHP");
			
	}
	if($yourAction eq "Magic")
	{
		print p("Both sides decide to use Magic on each other!");
		print p ("$retrieve_cookie[1] receives  $yourIntelligence damage! $myNewHP");
		print p ("$battle_cookie[1] receives $myIntelligence damage! $yourNewHP");
	}
	if($yourAction eq "Defend")
	{
		print p("Both sides decide to defend!");
		print p ("Nothing happens");
	}
	if($yourAction eq "MagicBarrier")
	{
		print p("Both sides decide to use MagicBarrier");
		print p ("Nothing happens");
	}
	
}
if($yourAction eq "Punch")
{
	
	if($enemyReaction eq "Magic")
	{
		print p ("$retrieve_cookie[1] receives  $yourIntelligence damage! $myNewHP");
		print p ("$battle_cookie[1] receives $myStrength damage! $yourNewHP")

	}
	if($enemyReaction eq "Defend")
	{
		print p ("$retrieve_cookie[1] receives  $yourResillience damage! $myNewHP");
		print p ("$battle_cookie[1] receives 0 damage! $yourNewHP")		
	}
	if($enemyReaction eq "MagicBarrier")
	{
		print p ("$retrieve_cookie[1] receives  0 damage! $myNewHP");
		print p ("$battle_cookie[1] receives $myStrength damage! $yourNewHP")
	
	}

}

if($yourAction eq "Magic")
{
	
	if($enemyReaction eq "Punch")
	{
		print p ("$retrieve_cookie[1] receives  $yourStrength damage! $myNewHP");
		print p ("$battle_cookie[1] receives $myIntelligence damage! $yourNewHP")

	}
	if($enemyReaction eq "Defend")
	{
	
		print p ("$retrieve_cookie[1] receives 0 damage! $myNewHP");
		print p ("$battle_cookie[1] receives $myIntelligence damage! $yourNewHP")
		
	}
	if($enemyReaction eq "MagicBarrier")
	{
	
		print p ("$retrieve_cookie[1] receives  $yourSpeed damage! $myNewHP");
		print p ("$battle_cookie[1] receives 0 damage! $yourNewHP")
		
	}

}
if($yourAction eq "Defend")
{
	
	if($enemyReaction eq "Punch")
	{
		print p ("$retrieve_cookie[1] receives 0 damage! $myNewHP");
		print p ("$battle_cookie[1] receives $myResillience damage! $yourNewHP")
	}
	if($enemyReaction eq "Magic")
	{
		print p ("$retrieve_cookie[1] receives $yourIntelligence damage! $myNewHP");
		print p ("$battle_cookie[1] receives 0 damage! $yourNewHP")		
	}
	if($enemyReaction eq "MagicBarrier")
	{
		print p ("$retrieve_cookie[1] receives 0 damage! $myNewHP");
		print p ("$battle_cookie[1] receives 0 damage! $yourNewHP")	
	}

}
if($yourAction eq "MagicBarrier")
{
	
	if($enemyReaction eq "Punch")
	{
		print p ("$retrieve_cookie[1] receives $yourStrength damage! $myNewHP");
		print p ("$battle_cookie[1] receives 0 damage! $yourNewHP")	

	}
	if($enemyReaction eq "Magic")
	{
		print p ("$retrieve_cookie[1] receives 0 damage! $myNewHP");
		print p ("$battle_cookie[1] receives $mySpeed damage! $yourNewHP")	
		
	}
	if($enemyReaction eq "Defend")
	{
			print p ("$retrieve_cookie[1] receives 0 damage! $myNewHP");
		print p ("$battle_cookie[1] receives 0 damage! $yourNewHP")	
	}

}






if($retrieve_cookie[0] eq "puffy")
{
	print img {src=>'img/puffy/puffy_normal.png',align=>'LEFT', height=>'100', width=>'100'};
}
else
{
print img {src=>'img/turdle/turdle_normal.png',align=>'RIGHT', height=>'100', width=>'100'};
	
}

print img {src=>'img/slime/slime_angry.jpg',align=>'RIGHT', height=>'100', width=>'100'};
print br;
print br;
print br;
print br;
print br;
print p("<b>My Health: $myNewHP</b>");
print br;
print "<DIV align=RIGHT>";
print p("<b>Enemy Health: $yourNewHP</b>");
print "</DIV>";

#$newURL = "battle.cgi?=

if($myNewHP==0 || $yourNewHP==0)
{
	if($myNewHP==0)
	{
		print p("<b>YOUR HEALTH IS 0! YOU CAN NO LONGER MOVE</b>");
		print p("<b>YOU ARE DEFEATED!</b>");
		print a( {-href=>'main.cgi'}, "Go back to main menu");
	}
	if($yourNewHP==0)
	{
		print p("<b> YOU HAVE DEFEATED $battle_cookie[1]! </b>");
		print a( {-href=>'main.cgi'}, "Go back to main menu");
	}
}
else
{
	print a( {-href=>'contBattle.cgi'}, "Next Turn");
}

end_html;
exit;
	