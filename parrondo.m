epsilon=.005;
Mtotal = zeros(1,100);
for loop=1:1000
m = 0; 
samplefunction = zeros(1,100); 
for flips = 1:100 
 if rem(m,3)==0 
outcome = rand; 
if outcome < 0.1 - epsilon 
m = m +1 ; 
else 
m = m- 1; 
end 
else 
outcome = rand; 
if outcome < 0.75 - epsilon 
m = m + 1; 
else 
m = m- 1; 
end 
end 
samplefunction(flips) = m; 
i 
Mtotal = Mtotal + samplefunction; 
end 



epsilon=.005;
Mtotal = zeros(1,100);
for loop=1:1000
m = 0; 
samplefunction = zeros(1,100); 
for flips = 1:100 
whichgame=rand;
if whichgame<.5
	outcome=rand;
if outcome<.5-epsilon
m=m+1;
else
m=m-1;
end
else
 if rem(m,3)==0 
outcome = rand; 
if outcome < 0.1 - epsilon 
m = m +1 ; 
else 
m = m- 1; 
end 
else 
outcome = rand; 
if outcome < 0.75 - epsilon 
m = m + 1; 
else 
m = m- 1; 
end 
end 
samplefunction(flips) = m; 
i 
Mtotal = Mtotal + samplefunction; 
end 
Mtotal = Mtotal/1000