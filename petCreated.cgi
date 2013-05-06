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
	-value=>["$cookieVal[0]","$cookieVal[1]","$cookieVal[2]","$cookieVal[3]", "$cookieVal[4]", "$cookieVal[5]", "$cookieVal[6]", "$cookieVal[7]"],
	-expires=>'+1y'
);
	
print header(-cookie=>$cookie);


print start_html;
print h1("PerlPets");
print p("Congratulations! You just finished creating a new pet! \n");	

if($cookieVal[0] eq "left")
{
	print img {src=>'img/testpet/testpet_normal.png',align=>'CENTER', height=>'100', width=>'100'};
}
else
{
	print img {src=>'img/testpet2/testpet2_normal.png',align=>'CENTER', height=>'100', width=>'100'};
}

print br;
print br;

print a( {-href=>"main.cgi"}, "Play Now"); 
print '<link rel="stylesheet" type="text/css" href="css/main.css">';



end_html;
exit;
	



print header;
print start_html;
