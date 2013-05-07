#!/usr/bin/perl -T
use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser';
use CGI qw/:standard/;

my @currPet = cookie('ID');
my @values = split(/&/,$ENV{QUERY_STRING});
my @bathedDate = (); 

# get the values from form submitted on last page
foreach my $i (@values) 
{
	my($fieldname, $data) = split(/=/, $i);
	push(@bathedDate, $data);
}

my $lastBathed = $bathedDate[0] . "_" . $bathedDate[1] . "_" . $bathedDate[2] . "_" . $bathedDate[3];

my $cookie = cookie
(
	-name=>'ID',
	-value=>["$currPet[0]","$currPet[1]","$currPet[2]","$currPet[3]", "$currPet[4]", "$currPet[5]", "$currPet[6]", "$currPet[7]","$currPet[8]","$currPet[9]","$lastBathed"],
	-expires=>'+1y'
);
	
print header(-cookie=>$cookie);
print '<link rel="stylesheet" type="text/css" href="css/main.css">';

print start_html("PerlPets - Made Hungry");
print h1("PerlPets");
print p("The date your pet has last been bathed has been changed.");
print p('Click <a href="main.cgi">here</a> to go back to the main page.');

end_html;
exit;
	



