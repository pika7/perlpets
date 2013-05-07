#!/usr/bin/perl -T
use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser';
use CGI qw(:standard);
use URI;

my @retrieve_cookie = cookie('ID');

if (@retrieve_cookie) 
{
	print header;
	print start_html;
	print h1("PerlPets");
	print "<b>";
	print p("Train your pet");
	print "</b>";
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
	
	print hr, start_form;
	print radio_group(-name=>"stats", -values => ["Strength", "Intelligence", "Resillience", "Speed"]);
	print p(submit("TRAIN!"));
	my $chosenStat =  param("stats");
	my $newStrength=$retrieve_cookie[2];
	my $newIntel=$retrieve_cookie[3];
	my $newRes=$retrieve_cookie[4];
	my $newSpeed=$retrieve_cookie[5];
	
	if(param())
	{
		my $statVal = param("stats");
		if($statVal eq "Strength")
		{
			$newStrength = $newStrength + 5;
		}
		if($statVal eq "Intelligence")
		{
			 $newIntel = $newIntel + 5;

		}
		if($statVal eq "Resillience")
		{
			$newRes = $newRes + 5;
		}
		if($statVal eq "Speed")
		{
			$newSpeed= $newSpeed + 5;
		}
		
		
		my $uri = URI->new('statIncreased.cgi');
		$uri->query_form
		(
			petpic => $retrieve_cookie[0],
			name => $retrieve_cookie[1],
			strength => $newStrength,
			intelligence => $newIntel,
			resillience  => $newRes,
			speed => $newSpeed,
			won => $retrieve_cookie[6],
			lost => $retrieve_cookie[7],
			mood => $retrieve_cookie[8],
			hunger => $retrieve_cookie[9],
			cleanliness => $retrieve_cookie[10]
		);	

	print "<META HTTP-EQUIV=refresh CONTENT=\"1 URL='$uri'\">\n";
		
		
		
		
	}
	# print "<META HTTP-EQUIV=refresh CONTENT=\"1 URL='$uri'\">\n";
	print end_form, hr;
		
	
	end_html;
	exit;
}

