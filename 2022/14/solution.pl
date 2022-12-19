use 5.34.0;
use strict;
use warnings;
use feature "signatures";
no warnings "experimental::signatures";

use File::Slurp;

sub run($mode="normal") {
    my @data = read_input($mode);
    say "hello";
    return [
        #part_1(@data),
        #part_2(@data)
    ];
}

sub read_input($mode) {
    return prepare_data(<<TEST_DATA) if $mode eq "test";
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
TEST_DATA
    my $data = read_file("input.txt");
    return prepare_data($data);
}

sub prepare_data($data) {
    return map { [ map { [split /-/, $_] } split /,/, $_] } split /\n/, $data;
}

run();
1;
