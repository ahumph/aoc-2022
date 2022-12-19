use 5.34.0;
use strict;
use warnings;
use feature "signatures";
no warnings "experimental::signatures";

use File::Slurp;
use Time::HiRes qw( time );

sub run($mode="normal") {
    my $data = read_input($mode);
    return [
        part_1($data),
        part_2($data)
    ];
}

sub read_input($mode) {
    my $data = read_file("input.txt");
    return prepare_data($data);
}

sub prepare_data($data) {
    return $data;
}

sub build_regex($n) {
    my $regex = "(.)";
    foreach my $i (1..$n-1) {
        $regex .= "(?!";
        foreach my $j (1..$i) {
            $regex .= "\\$j";
            if ($j < $i) {
                $regex .= "|";
            }
        }
        $regex .= ($i == $n-1) ? ")." : ")(.)";
    }
    return $regex;
}

sub part_1($data) {
    my $begin_time = time();
    my $regex = build_regex(4);
    $data =~ /$regex/g;
    say "Part 1: " . pos($data);
    my $end_time = time();
    printf("Part 1 Executed in: %fs\n", $end_time - $begin_time);
}

sub part_2($data) {
    my $begin_time = time();
    my $regex = build_regex(14);
    $data =~ /$regex/g;
    say "Part 2: " . pos($data);
    my $end_time = time();
    printf("Part 2 Executed in: %fs\n", $end_time - $begin_time);
}

run();
1;
