% Advent of Code 2015 Day 4
% https://adventofcode.com/2015/day/4

key = 'yzbqklnj';

% PART 1
i = 1;
found_it = false;
while (found_it == false)
    if (mod(i,1e5)==0)
        fprintf('%10d\n', i);
    end
    coin = [key, num2str(i)];
    ch = md5(coin);
    if ch(1)=='0' && ch(2)=='0' && ch(3)=='0' && ch(4)=='0' && ch(5)=='0'
        found_it = true;
    else
        i = i + 1;
    end
end
fprintf('%s\n', ch);
fprintf('lowest positive number giving five zeroes in the hash is %d\n', i);

% PART 2
i = 1;
found_it = false;
while (found_it == false)
    if (mod(i,1e5)==0)
        fprintf('%10d\n', i);
    end
    coin = [key, num2str(i)];
    ch = md5(coin);
    if ch(1)=='0' && ch(2)=='0' && ch(3)=='0' && ch(4)=='0' && ch(5)=='0' && ch(6)=='0'
        found_it = true;
    else
        i = i + 1;
    end
end
fprintf('%s\n', ch);
fprintf('lowest positive number giving six zeroes in the hash is %d\n', i);


% SUPPORT FUNCTION for MD5 HASH (provided by me, I found it on the interwebs)

function h = md5(s)

persistent MD5
if isempty( MD5 )
    MD5 = java.security.MessageDigest.getInstance( 'MD5' );
end

MD5.update( uint8( s(:) ) );
h = typecast( MD5.digest, 'uint8' );
h = dec2hex( h )';
h = lower( h(:) )';

end





