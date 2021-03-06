#!/usr/bin/perl -T
use strict;
use CGI qw/:standard/;
use CGI::Carp 'fatalsToBrowser';
use URI;


print header;
print start_html("PERLPETS - Registration form");
print h1("PerlPets");
print '<link rel="stylesheet" type="text/css" href="css/main.css">';
print p("Welcome to PerlPets! \n");
print p("Choose your pet! \n");
print p(
	img {src=>'img/puffy/puffy_normal.png'},
	img {src=>'img/turdle/turdle_normal.png'}
);

print br;
print br;
print br;
print br;

print hr, start_form;
print p(radio_group(-name=>"petimage", -values => ["puffy", "turdle"]));

print p("Give it a name \n");
print p ("Name: ", textfield("name",""));

print br;
print br;

print p("Enter the stats. Must add up to 20 \n");
print p("Strength :", textfield("Strength", ""));
print p("Intelligence :", textfield("Intelligence", ""));
print p("Resillience :", textfield("Resillience", ""));
print p("Speed :", textfield("Speed", ""));
print p(submit("create a new pet"), reset("clear"));


if(param())
{
	# get date and time
	my ( $sec, $min, $hr, $mday, $mon, $year, $wday, $yday, $isdst ) = localtime(time);
	
	my $strength = param("Strength");
	my $intelligence = param("Intelligence");
	my $resillience = param("Resillience");
	my $speed= param("Speed");
	my $total = $strength + $intelligence + $resillience + $speed;
	my $petPic = param("petimage");
	my $petName = param("name");
	my $won = '0';
	my $lost = '0';
	my $mood = "normal";
	my $hunger = $hr . "_" . $mday . "_" . $mon . "_" . $year;
	my $cleanliness = $hr . "_" . $mday . "_" . $mon . "_" . $year;
	
	if($total == 20)
	{
		
		my $uri = URI->new('petCreated.cgi');
		$uri->query_form
		(
			petpic => $petPic,
			name => $petName,
			strength => $strength,
			intelligence => $intelligence,
			resillience  => $resillience,
			speed => $speed,
			won => $won,
			lost => $lost,
			mood => $mood,
			hunger => $hunger,
			cleanliness => $cleanliness
		);
	
	print $uri, "\n";

	print "<META HTTP-EQUIV=refresh CONTENT=\"1 URL='$uri'\">\n";
	}
	else
	{
		print p("The sum of values must be equal to 20");
	}
	
	
}



print end_form, hr;

end_html;
exit;
	