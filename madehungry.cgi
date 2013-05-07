#!/usr/bin/perl -T
use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser';
use CGI qw/:standard/;

my @currPet = cookie('ID');
my @values = split(/&/,$ENV{QUERY_STRING});
my @fedDate = (); 

# get the values from form submitted on last page
foreach my $i (@values) 
{
	my($fieldname, $data) = split(/=/, $i);
	push(@fedDate, $data);
}

my $lastFed = $fedDate[0] . "_" . $fedDate[1] . "_" . $fedDate[2] . "_" . $fedDate[3];

my $cookie = cookie
(
	-name=>'ID',
	-value=>["$currPet[0]","$currPet[1]","$currPet[2]","$currPet[3]", "$currPet[4]", "$currPet[5]", "$currPet[6]", "$currPet[7]","$currPet[8]","$lastFed","$currPet[10]"],
	-expires=>'+1y'
);
	
print header(-cookie=>$cookie);
print '<link rel="stylesheet" type="text/css" href="css/main.css">';

print start_html("PerlPets - Made Hungry");
print h1("PerlPets");
print p("The date your pet has last been fed has been changed.");
print p('Click <a href="main.cgi">here</a> to go back to the main page.');

end_html;
exit;
	



