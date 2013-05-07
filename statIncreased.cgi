#!/usr/bin/perl -T
use strict;
use CGI;
use CGI::Carp 'fatalsToBrowser';
use CGI qw/:standard/;


my @values = split(/&/,$ENV{QUERY_STRING});
my @cookieVal = (); 

foreach my $i (@values) 
{
	my($fieldname, $data) = split(/=/, $i);
	push(@cookieVal, $data);
}

my $cookie = cookie
(
	-name=>'ID',
	-value=>["$cookieVal[0]","$cookieVal[1]","$cookieVal[2]","$cookieVal[3]", "$cookieVal[4]", "$cookieVal[5]", "$cookieVal[6]", "$cookieVal[7]","$cookieVal[8]","$cookieVal[9]","$cookieVal[10]"],
	-expires=>'+1y'
);
	
print header(-cookie=>$cookie);

print start_html("Perlpets- Stat increased!");
print h1("PerlPets");
print p("YOUR PET HAS BECOME STRONGER! \n");	
if($cookieVal[0] eq "puffy")
{
	print "<center>";
	print img {src=>'img/puffy/puffy_normal.png',align=>'CENTER', height=>'100', width=>'100'};
	print "</center>";
}
else
{
	print "<center>";
	print img {src=>'img/turdle/turdle_normal.png',align=>'CENTER', height=>'100', width=>'100'};
	print "</center>";
}
print br;
print br;

	print "<b>";
	print p({-align=>'center'},"$cookieVal[1]'s new battle status");
	print "</b>";

	print p({-align=>'center'},"STRENGTH: $cookieVal[2]");
	print p({-align=>'center'},"INTELLIGENCE: $cookieVal[3]");
	print p({-align=>'center'},"RESILLIENCE: $cookieVal[4]");	
	print p({-align=>'center'},"SPEED: $cookieVal[5]");
	print br;


print a( {-href=>"main.cgi"}, "Go Back to Main Menu"); 
print '<link rel="stylesheet" type="text/css" href="css/main.css">';



end_html;
exit;





