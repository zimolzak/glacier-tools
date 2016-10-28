#!/usr/bin/perl -w
use strict;

my $cmd_template = "aws glacier upload-archive --account-id - --vault-name ajz-media-backup --archive-description 'DDDDDDDD' --body ";

while(<>){
    chomp;
    my $filename = $_;
    my $cmd_to_run = "$cmd_template '$filename'\n";
    $cmd_to_run =~ s/DDDDDDDD/$filename/;
    print "**** FILE: $filename\n";
    print "     COMMAND: $cmd_to_run";
    system($cmd_to_run);
}
