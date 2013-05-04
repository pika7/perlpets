#!/usr/local/bin/perl -w
# sortTable.cgi
# URL: http://ihome.ust.hk/~cs_lcxae/cgi-bin/sortTable.cgi
use CGI qw(:standard);
use CGI::Carp 'fatalsToBrowser';
use strict;
use DBI;

# connect to database -- just copy and paste this? isnt there a better way?
my $mysql_hostname = 'ihomedb.ust.hk'; 
my $user = '94360';
my $password = 'admin'; 
my $db_name = '94360db';

my $dsn = "DBI:mysql:$db_name:$mysql_hostname";
my $dbh = DBI->connect($dsn, $user, $password);
if ( !defined $dbh ) { die "Cannot connect to MySQL server: $DBI::errstr\n"; }

print header();
print start_html("PerlPets - Login");
print '<link rel="stylesheet" type="text/css" href="css/main.css">';

print h1("PerlPets");
print h2("Login");

print start_form();
print p(
		"Username: ", textfield("username"), "<br />",
		"Password: ", password_field("password"), "<br />",
		submit()
	);
print end_form();

# if both fields are filled
if (param("username") && param("password")) {
	# validate username
	if (!(param("username") =~ /^\w+$/)) {
		print p("wrong name");
	}

	my $username = param("username");
	my $password = param("password");

	# check for username and password match in the database
	my $sql_checkuser = $dbh->prepare('SELECT * FROM `users` WHERE username="$username" AND password="$password";') or die("Could not prepare SQL statement");
	$sql_checkuser->execute() or die("Could not execute query");

	# if a record is returned, then password/username is correct
	print p($sql_checkuser->fetchrow_array());

	if ($sql_checkuser->fetchrow_array()) {
		print p("good");
	}
	else {
		print '<p id="error">Incorrect username or password.</p>';
	}
}

print end_html();