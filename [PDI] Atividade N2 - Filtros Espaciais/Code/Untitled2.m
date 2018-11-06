clear all
close all
clc

Original = imread('Suavizar_(2).jpg');
vetor = zeros(size(Original,1)*size(Original,2),1);

for x = 1:size(Original,1)
    for y = 1:size(Original,2)
        vetor(x*y) = Original(x,y);
    end
end

%{
while a > 1
    for j=1:48
        if t(j) > t(j+1)
            aux = t(j);
            t(j) = t(j+1);
            t(j+1) = aux;
        end
    end
    a= a -1;
end
%}