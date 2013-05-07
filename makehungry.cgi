#!/usr/bin/perl -T
use strict;
use CGI qw/:standard/;
use CGI::Carp 'fatalsToBrowser';
use URI;


print header;
print start_html("PerlPets - Make your pet hungry");
print h1("PerlPets");
print '<link rel="stylesheet" type="text/css" href="css/main.css">';

	
print "<div class=\"Actions\">\n";
print a( {-href=>"main.cgi"},"My Pet's status"); 
print br;
print a( {-href=>"battle.cgi"}, "Battle"); 
print br;
print a( {-href=>"train.cgi"}, "Train"); 
print br;
print a( {-href=>"main.cgi"}, "Eat"); 
print br;
print a( {-href=>"bath.cgi"}, "Bath"); 
print br;
print "</DIV>";

print start_form;
print p("Enter the date you want your pet last fed by.");
print p("Hour: ", textfield("hour"));
print p("Day: ", textfield("day"));
print p("Month: ", textfield("month"));
print p("Year: ", textfield("year"));
print p(submit());
print end_form;

if(param())
{	
	# make sure all fields filled
	if (param("hour") and param("day") and param("month") and param("year")) {
		my $uri = URI->new('madehungry.cgi');
		$uri->query_form (
			hour => param("hour"),
			day => param("day"),
			month => param("month"),
			year => param("year") - 1900
		);

		print "<META HTTP-EQUIV=refresh CONTENT=\"1 URL='$uri'\">\n";
	}
	else {
		print p("Please fill all fields.");
	}
	
}

end_html;
exit;
