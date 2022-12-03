#!/usr/bin/env ruby

LOOKUP_TABLE = Hash[(Array('a'..'z') + Array('A'..'Z')).zip(1..52)]

class String
    def to_array
        self.split('')
    end
end


def main
    lines = File.readlines('demo-input.txt').map(&:chomp)
    
    puts first_task lines
    puts second_task lines
end


def first_task(lines)
    lines.map do |line|
        size = line.length/2
        first = line[..size-1].to_array
        second = line[size..].to_array
        first.intersection(second).first
    end.map do |char|
        LOOKUP_TABLE[char]
    end.sum
end


def second_task(lines)
    lines.each_slice(3)
         .map { |a, b, c| [ a.to_array, b.to_array, c.to_array ] }
         .map { |a, b, c| a.intersection(b).intersection(c).first }
         .map { |key| LOOKUP_TABLE[key] }
         .sum
end


main if __FILE__ == $0
