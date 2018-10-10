% Advent of Code 2015 Day 4
% https://adventofcode.com/2015/day/4

% try a parallel version

key = 'yzbqklnj';

% PART 1
tic
batch = 0;
batchsize = 10000;
found_it = ones(1,batchsize)*false;
while (any(found_it) == false)
    parfor i=1:batchsize
        ib = (batch * batchsize) + i;
        if (mod(ib,1e5)==0)
            fprintf('%10d\n', ib);
        end
        coin = [key, num2str(ib)];
        ch = md5(coin);
        if ch(1)=='0' && ch(2)=='0' && ch(3)=='0' && ch(4)=='0' && ch(5)=='0'
            found_it(i) = true;
        end
    end
    batch = batch + 1;
end
n = ((batch-1)*batchsize)+find(found_it);
ch = md5([key, num2str(n)]);
fprintf('%s\n', ch);
fprintf('lowest positive number giving five zeroes in the hash is %d\n', n);
toc

% PART 2
tic
batch = 0;
batchsize = 10000;
found_it = ones(1,batchsize)*false;
while (any(found_it) == false)
    parfor i=1:batchsize
        ib = (batch * batchsize) + i;
        if (mod(ib,1e6)==0)
            fprintf('%10d\n', ib);
        end
        coin = [key, num2str(ib)];
        ch = md5(coin);
        if ch(1)=='0' && ch(2)=='0' && ch(3)=='0' && ch(4)=='0' && ch(5)=='0' && ch(6)=='0'
            found_it(i) = true;
        end
    end
    batch = batch + 1;
end
n = ((batch-1)*batchsize)+find(found_it);
ch = md5([key, num2str(n)]);
fprintf('%s\n', ch);
fprintf('lowest positive number giving six zeroes in the hash is %d\n', n);
toc


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


